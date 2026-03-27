#!/usr/bin/env python3
"""
Parse update_paper_list.md, sort all papers by date (newest first),
and write back the sorted result.
"""

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
PAPER_LIST = ROOT / "data" / "update_paper_list.md"

# Month name -> number
MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12,
}


def _parse_date(date_str: str) -> datetime:
    """Parse 'Month DD, YYYY' -> datetime. Returns epoch on failure."""
    try:
        return datetime.strptime(date_str.strip(), "%B %d, %Y")
    except ValueError:
        pass
    # Try partial: 'Month YYYY'
    try:
        parts = date_str.strip().split()
        if len(parts) == 2:
            month = MONTHS.get(parts[0].lower(), 1)
            return datetime(int(parts[1]), month, 1)
    except Exception:
        pass
    return datetime(1970, 1, 1)


def _split_into_entries(text: str) -> list[str]:
    """Split markdown text into individual paper entry blocks."""
    entries = []
    current = []
    for line in text.splitlines(keepends=True):
        if line.startswith("- [") and current:
            entries.append("".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        entries.append("".join(current))
    return entries


def _get_entry_date(entry: str) -> datetime:
    m = re.search(r"📅 Date:\s*(.+)", entry)
    if m:
        return _parse_date(m.group(1))
    return datetime(1970, 1, 1)


def main():
    if not PAPER_LIST.exists():
        print("[sort] No paper list found, skipping.")
        return

    text = PAPER_LIST.read_text(encoding="utf-8")
    entries = [e for e in _split_into_entries(text) if e.strip().startswith("- [")]

    if not entries:
        print("[sort] No entries found.")
        return

    entries.sort(key=_get_entry_date, reverse=True)

    sorted_text = "\n".join(e.rstrip() for e in entries) + "\n"
    PAPER_LIST.write_text(sorted_text, encoding="utf-8")
    print(f"[sort] Sorted {len(entries)} papers by date.")


if __name__ == "__main__":
    main()
