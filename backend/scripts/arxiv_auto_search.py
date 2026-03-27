#!/usr/bin/env python3
"""
Daily arXiv paper search for The-Library-of-AI-Scientist.

Two-phase retrieval:
  1. Crawl papers.cool for recent papers from top AI conferences
  2. Supplement with direct arXiv keyword search for today's submissions

New papers are appended to data/update_paper_list.md if not already present.
"""

import json
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import arxiv
import httpx
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent
PAPER_LIST = ROOT / "data" / "update_paper_list.md"
CACHE_DIR = ROOT / "data" / ".cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ────────────────────────────────────────────────────────────────────
PAPERS_COOL_BASE = "https://papers.cool"

# Conferences to crawl on papers.cool
CONFERENCES = ["NeurIPS", "ICML", "ICLR", "AAAI", "IJCAI", "ACL", "EMNLP", "NAACL", "COLM"]

# arXiv categories to search
ARXIV_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL", "cs.MA"]

# Keywords that make a paper relevant (title match, word-boundary)
TITLE_KEYWORDS = [
    "ai scientist", "ai-scientist",
    "automated research", "autonomous research",
    "scientific discovery", "scientific agent",
    "hypothesis generation", "hypothesis-driven",
    "automated experiment", "autonomous experiment",
    "literature review automation", "automated literature",
    "research automation", "research agent",
    "llm scientist", "llm for science",
    "ai for science",
    "automated hypothesis",
    "autonomous scientist",
    "self-driven research",
    "automated scientific",
]

# Phrases checked in abstract (substring match)
ABSTRACT_PHRASES = [
    "ai scientist",
    "automated scientific discovery",
    "autonomous scientific",
    "hypothesis generation",
    "automated research",
    "scientific agent",
    "llm for science",
    "ai for science",
    "automated experiment",
    "research automation",
]

# arXiv search queries for direct daily search
ARXIV_QUERIES = [
    "ti:\"AI scientist\"",
    "ti:\"scientific discovery\" AND ti:\"language model\"",
    "ti:\"automated research\"",
    "ti:\"autonomous research\"",
    "ti:\"hypothesis generation\" AND ti:agent",
    "ti:\"research agent\"",
    "ti:\"AI for science\"",
    "ti:\"automated scientific\"",
]

# Topic classification rules (first match wins)
TOPIC_RULES = [
    ("AI Scientist",          ["ai scientist", "ai-scientist", "autonomous scientist"]),
    ("Hypothesis Generation", ["hypothesis generation", "hypothesis-driven", "automated hypothesis"]),
    ("Literature Review",     ["literature review", "automated literature"]),
    ("Data Analysis",         ["data analysis", "automated analysis"]),
    ("Multi-Agent",           ["multi-agent", "multi agent", "multiagent"]),
    ("Machine Learning",      ["machine learning", "deep learning", "neural network"]),
    ("Scientific Discovery",  ["scientific discovery", "scientific agent", "autonomous discovery"]),
    ("Misc",                  []),  # fallback
]

# Keyword tags
KEYWORD_RULES = {
    "llm":         ["language model", "llm", "gpt", "claude", "gemini"],
    "agent":       ["agent", "agentic"],
    "automation":  ["automat", "autonomous"],
    "framework":   ["framework", "system", "platform", "pipeline"],
    "benchmark":   ["benchmark", "evaluation", "dataset", "leaderboard"],
    "dataset":     ["dataset", "corpus", "data collection"],
    "discovery":   ["discovery", "discover"],
    "experiment":  ["experiment", "experimental"],
    "hypothesis":  ["hypothesis", "hypothes"],
    "reasoning":   ["reasoning", "reason", "inference"],
    "survey":      ["survey", "review", "overview"],
    "multi-agent": ["multi-agent", "multiagent", "multi agent"],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_existing_titles() -> set[str]:
    """Return lowercase titles already in update_paper_list.md."""
    if not PAPER_LIST.exists():
        return set()
    text = PAPER_LIST.read_text(encoding="utf-8")
    return {m.group(1).lower() for m in re.finditer(r"^\- \[(.+?)\]\(", text, re.MULTILINE)}


def _is_relevant(title: str, abstract: str | None) -> bool:
    t = title.lower()
    for kw in TITLE_KEYWORDS:
        if re.search(r"\b" + re.escape(kw) + r"\b", t):
            return True
    if abstract:
        a = abstract.lower()
        for phrase in ABSTRACT_PHRASES:
            if phrase in a:
                return True
    return False


def _classify_topic(title: str, abstract: str | None) -> str:
    text = (title + " " + (abstract or "")).lower()
    for topic, phrases in TOPIC_RULES:
        if not phrases:
            return topic  # fallback
        for p in phrases:
            if p in text:
                return topic
    return "Misc"


def _extract_keywords(title: str, abstract: str | None) -> list[str]:
    text = (title + " " + (abstract or "")).lower()
    tags = []
    for tag, phrases in KEYWORD_RULES.items():
        for p in phrases:
            if p in text:
                tags.append(tag)
                break
    return tags or ["framework"]


def _format_date(dt: datetime | None) -> str:
    if dt is None:
        return datetime.now(timezone.utc).strftime("%B %d, %Y")
    return dt.strftime("%B %d, %Y")


def _paper_to_md(p: dict) -> str:
    authors_str = ", ".join(p.get("authors", []))
    if len(p.get("authors", [])) > 6:
        authors_str = ", ".join(p["authors"][:6]) + ", et al."
    institutions = p.get("institutions", "")
    inst_line = f"    - 🏛️ Institutions: {institutions}\n" if institutions else ""
    keys = "".join(f"[{k}], " for k in p["keywords"]).rstrip(", ")
    tldr = (p.get("abstract") or "").replace("\n", " ").strip()
    return (
        f"- [{p['title']}]({p['url']})\n"
        f"    - {authors_str}\n"
        f"{inst_line}"
        f"    - 📅 Date: {p['date']}\n"
        f"    - 📑 Publisher: arXiv\n"
        f"    - 💻 Topic: [{p['topic']}]\n"
        f"    - 🔑 Key: {keys}\n"
        f"    - 📖 TLDR: {tldr}\n"
    )


# ── Phase 1: papers.cool crawler ──────────────────────────────────────────────

class PapersCoolCrawler:
    def __init__(self):
        self._last = 0.0

    def _rate_limit(self):
        elapsed = time.time() - self._last
        if elapsed < 1.5:
            time.sleep(1.5 - elapsed)
        self._last = time.time()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((httpx.HTTPError, httpx.TimeoutException)),
    )
    def _get(self, url: str) -> str:
        self._rate_limit()
        with httpx.Client(timeout=20, follow_redirects=True) as client:
            r = client.get(url, headers={"User-Agent": "Mozilla/5.0 (research-crawler/1.0)"})
            r.raise_for_status()
            return r.text

    def _cache_path(self, key: str) -> Path:
        safe = re.sub(r"[^\w\-]", "_", key)
        return CACHE_DIR / f"{safe}.json"

    def _load_cache(self, key: str):
        p = self._cache_path(key)
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                pass
        return None

    def _save_cache(self, key: str, data) -> None:
        self._cache_path(key).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def get_volumes(self, conference: str) -> list[dict]:
        key = f"volumes_{conference}"
        cached = self._load_cache(key)
        if cached is not None:
            return cached
        try:
            html = self._get(f"{PAPERS_COOL_BASE}/")
        except Exception as e:
            print(f"[papers.cool] Failed to fetch homepage: {e}")
            return []
        soup = BeautifulSoup(html, "lxml")
        volumes, seen = [], set()
        for a in soup.select("a[href]"):
            href = a.get("href", "")
            if re.match(rf"^/venue/{re.escape(conference)}\.\d{{4}}$", href):
                url = PAPERS_COOL_BASE + href
                if url not in seen:
                    seen.add(url)
                    year = int(re.search(r"(\d{4})$", href).group(1))
                    volumes.append({"volume_id": href.split("/")[-1], "year": year, "url": url})
        self._save_cache(key, volumes)
        return volumes

    def get_papers_from_volume(self, volume: dict) -> list[dict]:
        key = f"papers_{volume['volume_id']}"
        cached = self._load_cache(key)
        if cached is not None:
            return cached
        page_size, skip, all_papers = 25, 0, []
        while True:
            url = f"{volume['url']}?skip={skip}&show={page_size}"
            try:
                html = self._get(url)
            except Exception as e:
                print(f"[papers.cool] Failed at {url}: {e}")
                break
            soup = BeautifulSoup(html, "lxml")
            page = self._parse_page(soup, volume)
            if not page:
                break
            all_papers.extend(page)
            if len(page) < page_size:
                break
            skip += page_size
        self._save_cache(key, all_papers)
        return all_papers

    def _parse_page(self, soup: BeautifulSoup, volume: dict) -> list[dict]:
        papers = []
        for card in soup.select("div.paper"):
            title_el = card.select_one("a.title-link")
            if not title_el:
                continue
            title = title_el.get_text(strip=True)
            if not title:
                continue
            href = title_el.get("href", "")
            paper_url = (PAPERS_COOL_BASE + href) if href and not href.startswith("http") else href
            authors = [a.get_text(strip=True) for a in card.select("a.author")]
            summary_el = card.select_one("p.summary")
            abstract = summary_el.get_text(strip=True) if summary_el else None
            papers.append({
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "year": volume.get("year"),
                "paper_url": paper_url,
                "volume_id": volume["volume_id"],
            })
        return papers

    def crawl_recent(self, conferences: list[str], current_year: int) -> list[dict]:
        """Crawl current and previous year volumes for all conferences."""
        results = []
        for conf in conferences:
            volumes = self.get_volumes(conf)
            recent = [v for v in volumes if v.get("year") in (current_year, current_year - 1)]
            print(f"[papers.cool] {conf}: {len(recent)} recent volume(s)")
            for vol in recent:
                papers = self.get_papers_from_volume(vol)
                for p in papers:
                    p["conference"] = conf
                results.extend(papers)
        return results


# ── Phase 2: arXiv title matcher ──────────────────────────────────────────────

class ArxivMatcher:
    def __init__(self):
        self._client = arxiv.Client()
        self._last = 0.0

    def _rate_limit(self):
        elapsed = time.time() - self._last
        if elapsed < 3.0:
            time.sleep(3.0 - elapsed)
        self._last = time.time()

    def search_by_title(self, title: str) -> dict | None:
        self._rate_limit()
        for query in [f'ti:"{title}"', " ".join(title.split()[:8])]:
            try:
                results = list(self._client.results(
                    arxiv.Search(query=query, max_results=5, sort_by=arxiv.SortCriterion.Relevance)
                ))
            except Exception:
                continue
            best, best_score = None, 0.0
            for r in results:
                score = fuzz.token_sort_ratio(title.lower(), r.title.lower())
                if score > best_score:
                    best_score, best = score, r
            if best and best_score >= 60:
                return {
                    "arxiv_id": best.get_short_id(),
                    "title": best.title,
                    "abstract": best.summary,
                    "authors": [str(a) for a in best.authors],
                    "categories": best.categories,
                    "published": best.published,
                    "url": best.entry_id,
                }
        return None


# ── Phase 2b: arXiv daily keyword search ─────────────────────────────────────

def arxiv_daily_search(days_back: int = 2) -> list[dict]:
    """Search arXiv directly for recent papers matching our topic queries."""
    client = arxiv.Client()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    found = []
    seen_ids = set()

    for query in ARXIV_QUERIES:
        time.sleep(3)
        try:
            results = list(client.results(
                arxiv.Search(
                    query=query,
                    max_results=50,
                    sort_by=arxiv.SortCriterion.SubmittedDate,
                )
            ))
        except Exception as e:
            print(f"[arxiv] Query failed '{query}': {e}")
            continue

        for r in results:
            if r.published and r.published < cutoff:
                continue
            aid = r.get_short_id()
            if aid in seen_ids:
                continue
            seen_ids.add(aid)
            found.append({
                "arxiv_id": aid,
                "title": r.title,
                "abstract": r.summary,
                "authors": [str(a) for a in r.authors],
                "categories": r.categories,
                "published": r.published,
                "url": r.entry_id,
            })

    print(f"[arxiv daily] Found {len(found)} candidate papers")
    return found


# ── Main pipeline ─────────────────────────────────────────────────────────────

def build_paper_entry(arxiv_data: dict) -> dict:
    title = arxiv_data["title"]
    abstract = arxiv_data.get("abstract", "")
    topic = _classify_topic(title, abstract)
    keywords = _extract_keywords(title, abstract)
    published = arxiv_data.get("published")
    return {
        "title": title,
        "authors": arxiv_data.get("authors", []),
        "institutions": "",
        "date": _format_date(published),
        "url": arxiv_data["url"],
        "topic": topic,
        "keywords": keywords,
        "abstract": abstract,
    }


def main():
    today = datetime.now(timezone.utc)
    current_year = today.year
    existing_titles = _load_existing_titles()
    print(f"[main] {len(existing_titles)} existing papers loaded")

    new_papers: list[dict] = []
    seen_titles: set[str] = set()

    # ── Phase 1: papers.cool crawl ────────────────────────────────────────────
    print("\n=== Phase 1: papers.cool crawl ===")
    crawler = PapersCoolCrawler()
    matcher = ArxivMatcher()
    cool_papers = crawler.crawl_recent(CONFERENCES, current_year)
    print(f"[phase1] {len(cool_papers)} papers from papers.cool")

    for p in cool_papers:
        title = p.get("title", "").strip()
        if not title:
            continue
        tl = title.lower()
        if tl in existing_titles or tl in seen_titles:
            continue
        abstract = p.get("abstract")
        if not _is_relevant(title, abstract):
            continue

        # Try to get arXiv metadata
        arxiv_data = matcher.search_by_title(title)
        if arxiv_data:
            entry = build_paper_entry(arxiv_data)
        else:
            # Use papers.cool data directly
            topic = _classify_topic(title, abstract)
            keywords = _extract_keywords(title, abstract)
            entry = {
                "title": title,
                "authors": p.get("authors", []),
                "institutions": "",
                "date": _format_date(None),
                "url": p.get("paper_url", ""),
                "topic": topic,
                "keywords": keywords,
                "abstract": abstract or "",
            }

        if entry["url"]:
            seen_titles.add(tl)
            new_papers.append(entry)
            print(f"  [+] {title[:80]}")

    # ── Phase 2: arXiv daily search ───────────────────────────────────────────
    print("\n=== Phase 2: arXiv daily search ===")
    arxiv_candidates = arxiv_daily_search(days_back=2)

    for r in arxiv_candidates:
        title = r["title"].strip()
        tl = title.lower()
        if tl in existing_titles or tl in seen_titles:
            continue
        if not _is_relevant(title, r.get("abstract")):
            continue
        entry = build_paper_entry(r)
        seen_titles.add(tl)
        new_papers.append(entry)
        print(f"  [+] {title[:80]}")

    # ── Append to paper list ──────────────────────────────────────────────────
    if not new_papers:
        print("\n[main] No new relevant papers found today.")
        return

    print(f"\n[main] Appending {len(new_papers)} new papers to {PAPER_LIST}")
    PAPER_LIST.parent.mkdir(parents=True, exist_ok=True)

    existing_content = PAPER_LIST.read_text(encoding="utf-8") if PAPER_LIST.exists() else ""
    new_blocks = "\n".join(_paper_to_md(p) for p in new_papers)

    with PAPER_LIST.open("w", encoding="utf-8") as f:
        f.write(existing_content.rstrip() + "\n\n" + new_blocks + "\n")

    print(f"[main] Done. {len(new_papers)} papers added.")


if __name__ == "__main__":
    main()
