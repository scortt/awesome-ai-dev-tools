#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/scortt/project/awesome-ai-dev-tools"
CRON_LINE="30 20 * * * cd ${ROOT} && /bin/bash scripts/daily_starred_codex_update.sh >> reports/daily-starred-codex.log 2>&1"

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

if crontab -l >"$tmp" 2>/dev/null; then
  if grep -Fq "$CRON_LINE" "$tmp"; then
    echo "daily starred Codex cron is already installed"
    exit 0
  fi
else
  : >"$tmp"
fi

printf '\n%s\n' "$CRON_LINE" >>"$tmp"
crontab "$tmp"
echo "installed daily starred Codex cron:"
echo "$CRON_LINE"
