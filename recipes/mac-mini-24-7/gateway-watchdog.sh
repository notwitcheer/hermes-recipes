#!/usr/bin/env bash
# restart the hermes gateway if it has died. runs from cron every 5 min.
# tries launchd first (supervised), falls back to a background process.
# install: (crontab -l; echo '*/5 * * * * $HOME/scripts/gateway-watchdog.sh >/dev/null 2>&1') | crontab -
# usage: gateway-watchdog.sh [--dry-run]

set -u

HERMES_PY="$HOME/.hermes/hermes-agent/venv/bin/python"
LOG="$HOME/.hermes/logs/gateway-watchdog.log"

if pgrep -f "hermes_cli.main gateway run" >/dev/null; then
  [[ "${1:-}" == "--dry-run" ]] && echo "[dry-run] gateway alive, nothing to do"
  exit 0
fi

if [[ "${1:-}" == "--dry-run" ]]; then
  echo "[dry-run] gateway DOWN, would: launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.hermes.gateway.plist, else nohup gateway run --replace"
  exit 0
fi

echo "$(date -u +%FT%TZ) gateway down, restarting" >> "$LOG"
launchctl bootout "gui/$(id -u)/ai.hermes.gateway" 2>/dev/null
if launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/ai.hermes.gateway.plist" 2>>"$LOG"; then
  echo "$(date -u +%FT%TZ) restarted via launchd" >> "$LOG"
else
  nohup "$HERMES_PY" -m hermes_cli.main gateway run --replace >> "$HOME/.hermes/logs/gateway.log" 2>&1 &
  echo "$(date -u +%FT%TZ) restarted as background process (launchd refused)" >> "$LOG"
fi
