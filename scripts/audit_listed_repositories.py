#!/usr/bin/env python3
"""Audit GitHub repositories already listed in the English README."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ENTRY_URL_RE = re.compile(r"^- \[[^\]]+\]\((https://github\.com/[^)\s]+)\) - ")


def listed_repositories() -> tuple[list[tuple[str, str]], list[str]]:
    urls: list[str] = []
    in_fence = False
    for line in (ROOT / "README.md").read_text().splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = ENTRY_URL_RE.match(line)
        if match:
            urls.append(match.group(1).rstrip("/"))
    repositories: list[tuple[str, str]] = []
    skipped: list[str] = []
    seen: set[tuple[str, str]] = set()

    for url in urls:
        parts = [part for part in urlparse(url).path.split("/") if part]
        if len(parts) != 2:
            skipped.append(url)
            continue
        repo = (parts[0], parts[1])
        if repo not in seen:
            repositories.append(repo)
            seen.add(repo)
    return repositories, skipped


def fetch_repository(owner: str, name: str) -> dict:
    result = subprocess.run(
        ["gh", "api", f"repos/{owner}/{name}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
    )
    if result.returncode != 0:
        error = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "unknown error"
        status = "unavailable" if re.search(r"(?:HTTP\s+404|not found)", error, re.IGNORECASE) else "query_error"
        return {
            "requested": f"{owner}/{name}",
            "status": status,
            "error": error,
        }

    payload = json.loads(result.stdout)
    return {
        "requested": f"{owner}/{name}",
        "status": "ok",
        "full_name": payload.get("full_name"),
        "html_url": payload.get("html_url"),
        "archived": bool(payload.get("archived")),
        "disabled": bool(payload.get("disabled")),
        "description": payload.get("description"),
        "language": payload.get("language"),
        "license": (payload.get("license") or {}).get("spdx_id"),
        "pushed_at": payload.get("pushed_at"),
        "updated_at": payload.get("updated_at"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=".maintenance/listed-repository-health.json")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    repositories, skipped = listed_repositories()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(lambda repo: fetch_repository(*repo), repositories))
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repository_count": len(repositories),
        "unavailable_count": sum(item["status"] == "unavailable" for item in results),
        "query_error_count": sum(item["status"] == "query_error" for item in results),
        "archived_count": sum(bool(item.get("archived")) for item in results),
        "disabled_count": sum(bool(item.get("disabled")) for item in results),
        "skipped_non_repository_urls": skipped,
        "repositories": results,
    }
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(
        f"audited {payload['repository_count']} repositories: "
        f"{payload['unavailable_count']} unavailable, "
        f"{payload['query_error_count']} query errors, "
        f"{payload['archived_count']} archived, "
        f"{payload['disabled_count']} disabled"
    )
    if payload["query_error_count"]:
        print("repository audit incomplete because GitHub queries failed", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
