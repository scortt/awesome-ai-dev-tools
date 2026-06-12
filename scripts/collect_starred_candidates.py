#!/usr/bin/env python3
"""Generate curated candidates from a GitHub user's starred repositories.

The script intentionally writes a review report instead of editing README files.
An awesome list is curated, so automation should find candidates and preserve a
human/agent review step before entries are merged.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_FILES = [ROOT / "README.md", ROOT / "README.zh-CN.md"]

KEYWORDS_BY_CATEGORY = {
    "Coding Agents And AI IDEs": [
        "coding agent",
        "code assistant",
        "ai developer",
        "autonomous agent",
        "copilot",
        "claude code",
        "codex",
    ],
    "Agent Operations And Maintenance": [
        "skill",
        "agentic skills",
        "claude.md",
        "context usage",
        "token consumption",
        "handoff",
    ],
    "Agent Runtimes And Frameworks": [
        "agentic workflow",
        "multi-agent",
        "workflow automation",
        "agent framework",
        "autonomous task",
    ],
    "Model Context Protocol": [
        "mcp",
        "model context protocol",
    ],
    "Codebase Search And Indexing": [
        "code search",
        "codebase",
        "semantic search",
        "code index",
        "incremental index",
        "developer search",
    ],
    "Developer CLI And Terminal Tools": [
        "cli",
        "terminal",
        "command line",
        "proxy",
        "trace",
        "profile",
        "debug",
        "deploy",
        "git push",
    ],
    "Review And Change-Inspection UI": [
        "code review",
        "pull request",
        "file tree",
        "diff rendering",
    ],
    "Design, Prototyping, And Artifacts": [
        "design",
        "prototype",
        "slides",
        "ppt",
        "office",
        "screenshot to code",
        "ai-first design",
        "ai-generated",
        "design system",
        "artifact",
        "diagram",
    ],
    "3D And Asset Generation": [
        "3d",
        "asset",
        "scene",
        "mesh",
        "glb",
    ],
    "Browser And UI Automation": [
        "browser",
        "playwright",
        "automation",
        "computer-using",
        "vnc",
        "desktop",
        "e2e",
    ],
    "Testing, Evals, And Benchmarks": [
        "eval",
        "benchmark",
        "test",
        "verification",
    ],
    "Local Models And Inference": [
        "inference",
        "local model",
        "llm inference",
        "llm training",
        "mlx",
        "cuda",
        "serving",
    ],
    "Audio And Multimodal Workflows": [
        "voice",
        "speech",
        "tts",
        "subtitle",
        "multimodal",
        "ocr",
    ],
    "Prompt, Context, And Memory": [
        "prompt",
        "context engineering",
        "memory",
        "llm generation",
    ],
    "Docs, Knowledge, And RAG": [
        "rag",
        "document",
        "markdown",
        "pdf",
        "ocr",
        "scrape",
        "crawler",
        "knowledge",
        "semantic search",
        "web search",
        "dataset",
    ],
    "Sandboxes And Secure Execution": [
        "sandbox",
        "secure execution",
        "environment",
        "nix",
    ],
}

EXCLUDE_TERMS = [
    "awesome list",
    "course",
    "curriculum",
    "beginner",
    "font",
    "game clone",
    "personal finance",
    "commerce",
    "cms",
    "erp",
    "marketing automation",
]


def run_gh_api(user: str) -> list[dict]:
    cmd = [
        "gh",
        "api",
        "--paginate",
        "--header",
        "Accept: application/vnd.github.star+json",
        f"/users/{user}/starred?per_page=100",
        "--jq",
        ".[] | @json",
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        print("error: gh CLI is required", file=sys.stderr)
        raise SystemExit(1)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip(), file=sys.stderr)
        raise SystemExit(exc.returncode)

    repos: list[dict] = []
    for line in result.stdout.splitlines():
        if line.strip():
            repos.append(json.loads(line))
    return repos


def repo_payload(item: dict) -> dict:
    """Handle both GitHub's star+json envelope and plain repository payloads."""
    repo = item.get("repo")
    if isinstance(repo, dict):
        normalized = dict(repo)
        normalized["starred_at"] = item.get("starred_at")
        return normalized
    return item


def existing_urls() -> set[str]:
    urls: set[str] = set()
    pattern = re.compile(r"https://github\.com/[^)\s]+")
    for path in README_FILES:
        if path.exists():
            urls.update(pattern.findall(path.read_text()))
    return urls


def repo_text(repo: dict) -> str:
    fields = [
        repo.get("full_name") or "",
        repo.get("description") or "",
        repo.get("language") or "",
    ]
    return " ".join(fields).lower()


def classify(repo: dict) -> tuple[str | None, list[str]]:
    text = repo_text(repo)
    if any(term in text for term in EXCLUDE_TERMS):
        return None, []

    matches: list[tuple[int, str, list[str]]] = []
    for category, keywords in KEYWORDS_BY_CATEGORY.items():
        found = [keyword for keyword in keywords if keyword in text]
        if found:
            matches.append((len(found), category, found))

    if not matches:
        return None, []
    matches.sort(reverse=True)
    _, category, found = matches[0]
    return category, found


def license_text(repo: dict) -> str:
    license_info = repo.get("license") or {}
    spdx = license_info.get("spdx_id")
    if spdx and spdx != "NOASSERTION":
        return spdx
    return "License: see repository"


def language_text(repo: dict) -> str:
    return repo.get("language") or "Language: see repository"


def render_report(user: str, repos: list[dict]) -> str:
    candidates, summary = collect_candidates(repos)
    rows_by_category: dict[str, list[dict]] = {}
    for candidate in candidates:
        rows_by_category.setdefault(candidate["category"], []).append(candidate)

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Starred Repository Candidates",
        "",
        f"- GitHub user: `{user}`",
        f"- Generated: `{now}`",
        f"- Candidate count: `{summary['candidate_count']}`",
        f"- Already listed and skipped: `{summary['skipped_known']}`",
        f"- Archived or disabled skipped: `{summary['skipped_archived']}`",
        "",
        "Review these manually before adding them to `README.md` and `README.zh-CN.md`.",
        "The generator uses keyword hints only; final inclusion must follow `CONTRIBUTING.md`.",
        "",
    ]

    for category in KEYWORDS_BY_CATEGORY:
        rows = rows_by_category.get(category, [])
        if not rows:
            continue
        lines.extend([f"## {category}", ""])
        for candidate in rows:
            starred_at = candidate.get("starred_at") or "unknown"
            reason_text = ", ".join(candidate["matched_keywords"])
            lines.append(
                f"- [{candidate['full_name']}]({candidate['html_url']}) - "
                f"{candidate['description']} `{candidate['language']}` "
                f"`{candidate['license']}` _(starred: {starred_at}; matched: {reason_text})_"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def collect_candidates(repos: list[dict]) -> tuple[list[dict], dict]:
    known = existing_urls()
    candidates: list[dict] = []
    skipped_known = 0
    skipped_archived = 0

    for raw_repo in repos:
        repo = repo_payload(raw_repo)
        url = repo.get("html_url") or ""
        if url in known:
            skipped_known += 1
            continue
        if repo.get("archived") or repo.get("disabled"):
            skipped_archived += 1
            continue
        category, reasons = classify(repo)
        if not category:
            continue
        candidates.append(
            {
                "full_name": repo.get("full_name") or "unknown",
                "html_url": url,
                "description": (repo.get("description") or "No description.").strip(),
                "language": language_text(repo),
                "license": license_text(repo),
                "category": category,
                "matched_keywords": reasons,
                "starred_at": repo.get("starred_at"),
                "pushed_at": repo.get("pushed_at"),
                "updated_at": repo.get("updated_at"),
                "homepage": repo.get("homepage"),
                "topics": repo.get("topics") or [],
            }
        )

    candidates.sort(
        key=lambda candidate: (
            1 if candidate.get("starred_at") else 0,
            candidate.get("starred_at") or "",
            candidate.get("full_name") or "",
        ),
        reverse=True,
    )
    summary = {
        "candidate_count": len(candidates),
        "skipped_known": skipped_known,
        "skipped_archived": skipped_archived,
    }
    return candidates, summary


def render_json(user: str, repos: list[dict]) -> str:
    candidates, summary = collect_candidates(repos)
    payload = {
        "github_user": user,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        **summary,
        "candidates": candidates,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default="scortt")
    parser.add_argument(
        "--output",
        default="reports/starred-candidates.md",
        help="Path relative to repository root.",
    )
    parser.add_argument(
        "--json-output",
        default="reports/starred-candidates.json",
        help="Machine-readable candidate output path relative to repository root.",
    )
    args = parser.parse_args()

    repos = run_gh_api(args.user)
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(args.user, repos))
    print(f"wrote {output}")
    json_output = ROOT / args.json_output
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(render_json(args.user, repos))
    print(f"wrote {json_output}")


if __name__ == "__main__":
    main()
