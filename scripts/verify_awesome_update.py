#!/usr/bin/env python3
"""Verify structure and English/Chinese parity for the awesome list."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_FILES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]
ENTRY_RE = re.compile(
    r"^- \[[^\]]+\]\((https://github\.com/[^)\s]+)\) - .+"
)


def read_entries(path: Path) -> tuple[list[str], list[str]]:
    urls: list[str] = []
    errors: list[str] = []
    in_fence = False
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not line.startswith("- [") or "github.com/" not in line:
            continue
        match = ENTRY_RE.match(line)
        if not match:
            errors.append(f"{path.name}:{lineno}: malformed GitHub entry")
            continue
        if line.count("`") % 2:
            errors.append(f"{path.name}:{lineno}: unbalanced code spans")
        urls.append(match.group(1).rstrip("/"))

    seen: set[str] = set()
    for url in urls:
        if url in seen:
            errors.append(f"{path.name}: duplicate GitHub URL: {url}")
        seen.add(url)
    return urls, errors


def main() -> int:
    parsed = [read_entries(path) for path in README_FILES]
    errors = [error for _, file_errors in parsed for error in file_errors]
    english, chinese = parsed[0][0], parsed[1][0]

    if english != chinese:
        english_only = sorted(set(english) - set(chinese))
        chinese_only = sorted(set(chinese) - set(english))
        if english_only:
            errors.append("English-only URLs: " + ", ".join(english_only))
        if chinese_only:
            errors.append("Chinese-only URLs: " + ", ".join(chinese_only))
        if not english_only and not chinese_only:
            errors.append("English and Chinese entries use different ordering")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"verified {len(english)} bilingual GitHub entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
