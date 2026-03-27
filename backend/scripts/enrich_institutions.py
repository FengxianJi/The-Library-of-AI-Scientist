#!/usr/bin/env python3
"""
Enrich institution data for papers missing the Institutions field.
Uses OpenAlex API (free, no key required) to look up author affiliations by arXiv ID.
"""

import re
import time
from pathlib import Path

import httpx

ROOT = Path(__file__).parent.parent.parent
PAPER_LIST = ROOT / "data" / "update_paper_list.md"

OPENALEX_BASE = "https://api.openalex.org"
HEADERS = {"User-Agent": "mailto:research@example.com"}


def _get_arxiv_id(url: str) -> str | None:
    m = re.search(r"arxiv\.org/abs/([\d.]+)", url)
    return m.group(1) if m else None


def _fetch_institutions(arxiv_id: str) -> str:
    """Query OpenAlex for institution names via arXiv ID."""
    try:
        with httpx.Client(timeout=15) as client:
            r = client.get(
                f"{OPENALEX_BASE}/works/https://arxiv.org/abs/{arxiv_id}",
                headers=HEADERS,
            )
            if r.status_code != 200:
                return ""
            data = r.json()
            insts = set()
            for authorship in data.get("authorships", []):
                for inst in authorship.get("institutions", []):
                    name = inst.get("display_name", "")
                    if name:
                        insts.add(name)
            return ", ".join(sorted(insts)[:4])  # cap at 4
    except Exception:
        return ""


def main():
    if not PAPER_LIST.exists():
        print("[enrich] No paper list found, skipping.")
        return

    text = PAPER_LIST.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    updated = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        # Find paper entries missing institution line
        if line.startswith("- [") and "arxiv.org" in line:
            url_match = re.search(r"\((https://arxiv\.org/abs/[\d.]+)\)", line)
            if url_match:
                arxiv_id = _get_arxiv_id(url_match.group(1))
                # Check if next few lines already have Institutions
                snippet = "".join(lines[i:i+6])
                if arxiv_id and "🏛️ Institutions:" not in snippet:
                    # Find the authors line (i+1) and insert institution after it
                    inst = _fetch_institutions(arxiv_id)
                    if inst:
                        # Insert institution line after authors line
                        insert_pos = i + 2  # after title line and authors line
                        lines.insert(insert_pos, f"    - 🏛️ Institutions: {inst}\n")
                        updated += 1
                        print(f"  [+] {arxiv_id}: {inst[:60]}")
                        time.sleep(0.5)
        i += 1

    if updated:
        PAPER_LIST.write_text("".join(lines), encoding="utf-8")
        print(f"[enrich] Updated {updated} papers with institution data.")
    else:
        print("[enrich] No papers needed institution enrichment.")


if __name__ == "__main__":
    main()
