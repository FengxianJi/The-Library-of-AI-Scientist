#!/usr/bin/env python3
"""
Regenerate all markdown views from update_paper_list.md:
  - data/all_papers.md
  - paper_by_topic/paper_*.md
  - paper_by_key/paper_*.md
  - paper_by_author/paper_*.md
  - data/topic_grouping.md
  - data/keyword_grouping.md
  - data/author_grouping.md
  - README.md
"""

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
PAPER_LIST = ROOT / "data" / "update_paper_list.md"
README_TEMPLATE = ROOT / "data" / "update_readme_template.md"
README = ROOT / "README.md"

TOPIC_DIR = ROOT / "paper_by_topic"
KEY_DIR = ROOT / "paper_by_key"
AUTHOR_DIR = ROOT / "paper_by_author"

TOP_AUTHOR_COUNT = 20


# ── Parsing ───────────────────────────────────────────────────────────────────

def _split_entries(text: str) -> list[str]:
    entries, current = [], []
    for line in text.splitlines(keepends=True):
        if line.startswith("- [") and current:
            entries.append("".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        entries.append("".join(current))
    return [e for e in entries if e.strip().startswith("- [")]


def _parse_field(entry: str, emoji: str) -> str:
    m = re.search(re.escape(emoji) + r"\s*(?:\w+:)?\s*(.+)", entry)
    return m.group(1).strip() if m else ""


def _parse_topics(entry: str) -> list[str]:
    m = re.search(r"💻 Topic:\s*(.+)", entry)
    if not m:
        return ["Misc"]
    return re.findall(r"\[([^\]]+)\]", m.group(1)) or ["Misc"]


def _parse_keywords(entry: str) -> list[str]:
    m = re.search(r"🔑 Key:\s*(.+)", entry)
    if not m:
        return []
    return re.findall(r"\[([^\]]+)\]", m.group(1))


def _parse_authors(entry: str) -> list[str]:
    lines = entry.splitlines()
    # Authors are on the second line (after title line)
    for line in lines[1:]:
        line = line.strip()
        if line.startswith("- 🏛️") or line.startswith("- 📅") or line.startswith("- 📑"):
            break
        if line.startswith("- "):
            raw = line[2:].strip()
            # Remove "et al." suffix
            raw = re.sub(r",?\s*et al\.?$", "", raw)
            return [a.strip() for a in raw.split(",") if a.strip()]
    return []


def _slug(name: str) -> str:
    return re.sub(r"[^\w]", "_", name.lower()).strip("_")


# ── Writers ───────────────────────────────────────────────────────────────────

def _write_category_file(path: Path, title: str, entries: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {title}\n\nTotal: {len(entries)} papers\n\n"
    content += "\n".join(e.rstrip() for e in entries) + "\n"
    path.write_text(content, encoding="utf-8")


def main():
    if not PAPER_LIST.exists():
        print("[readme] No paper list found.")
        return

    text = PAPER_LIST.read_text(encoding="utf-8")
    entries = _split_entries(text)
    print(f"[readme] Parsed {len(entries)} papers")

    # ── Group by topic ────────────────────────────────────────────────────────
    by_topic: dict[str, list[str]] = defaultdict(list)
    for e in entries:
        for t in _parse_topics(e):
            by_topic[t].append(e)

    TOPIC_DIR.mkdir(exist_ok=True)
    # Remove old topic files
    for f in TOPIC_DIR.glob("paper_*.md"):
        f.unlink()

    for topic, topic_entries in sorted(by_topic.items()):
        fname = f"paper_{_slug(topic)}.md"
        _write_category_file(TOPIC_DIR / fname, f"{topic} Papers", topic_entries)

    # ── Group by keyword ──────────────────────────────────────────────────────
    by_key: dict[str, list[str]] = defaultdict(list)
    for e in entries:
        for k in _parse_keywords(e):
            by_key[k].append(e)

    KEY_DIR.mkdir(exist_ok=True)
    for f in KEY_DIR.glob("paper_*.md"):
        f.unlink()

    for key, key_entries in sorted(by_key.items()):
        fname = f"paper_{_slug(key)}.md"
        _write_category_file(KEY_DIR / fname, f"{key.title()} Papers", key_entries)

    # ── Group by author (top N) ───────────────────────────────────────────────
    author_count: dict[str, int] = defaultdict(int)
    author_entries: dict[str, list[str]] = defaultdict(list)
    for e in entries:
        for a in _parse_authors(e):
            author_count[a] += 1
            author_entries[a].append(e)

    top_authors = sorted(author_count.items(), key=lambda x: x[1], reverse=True)[:TOP_AUTHOR_COUNT]

    AUTHOR_DIR.mkdir(exist_ok=True)
    for f in AUTHOR_DIR.glob("paper_*.md"):
        f.unlink()

    for author, _ in top_authors:
        fname = f"paper_{_slug(author)}.md"
        _write_category_file(AUTHOR_DIR / fname, f"Papers by {author}", author_entries[author])

    # ── data/all_papers.md ────────────────────────────────────────────────────
    all_md = ROOT / "data" / "all_papers.md"
    all_md.write_text(
        "\n".join(e.rstrip() for e in entries) + "\n",
        encoding="utf-8",
    )

    # ── Grouping index files ──────────────────────────────────────────────────
    topic_lines = "\n".join(
        f"- [{t}](paper_by_topic/paper_{_slug(t)}.md) ({len(v)} papers)"
        for t, v in sorted(by_topic.items())
    )
    (ROOT / "data" / "topic_grouping.md").write_text(topic_lines + "\n", encoding="utf-8")

    key_lines = "\n".join(
        f"- [{k.title()}](paper_by_key/paper_{_slug(k)}.md) ({len(v)} papers)"
        for k, v in sorted(by_key.items())
    )
    (ROOT / "data" / "keyword_grouping.md").write_text(key_lines + "\n", encoding="utf-8")

    author_lines = "\n".join(
        f"- [{a}](paper_by_author/paper_{_slug(a)}.md) ({author_count[a]} papers)"
        for a, _ in top_authors
    )
    (ROOT / "data" / "author_grouping.md").write_text(author_lines + "\n", encoding="utf-8")

    # ── README ────────────────────────────────────────────────────────────────
    if README_TEMPLATE.exists():
        template = README_TEMPLATE.read_text(encoding="utf-8")
        all_papers_md = "\n".join(e.rstrip() for e in entries)
        readme = (
            template
            .replace("{{insert_topic_groups_here}}", topic_lines)
            .replace("{{insert_keyword_groups_here}}", key_lines)
            .replace("{{insert_author_groups_here}}", author_lines)
            .replace("{{insert_all_papers_here}}", all_papers_md)
        )
        README.write_text(readme, encoding="utf-8")
        print(f"[readme] README.md regenerated ({len(entries)} papers)")
    else:
        print("[readme] No template found, skipping README generation.")

    print(f"[readme] Topics: {len(by_topic)}, Keywords: {len(by_key)}, Authors: {len(top_authors)}")


if __name__ == "__main__":
    main()
