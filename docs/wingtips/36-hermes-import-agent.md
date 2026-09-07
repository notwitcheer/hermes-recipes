# Hermes Wingtips #36: hermes import-agent

posted 2026-08-01. original: [https://x.com/witcheer/status/2083360088593776765](https://x.com/witcheer/status/2083360088593776765)

Hermes Wingtips #36: hermes import-agent

if you already run Claude Code or Codex CLI, your setup can move over to Hermes Agent in one command:

`hermes import-agent`

it auto-detects `~/.claude` or `~/.codex` and maps everything to its Hermes equivalent: 

global instructions become memories, skills come across as skills, MCP servers goes in your config, and Claude's permission rules become the command allowlist. API keys and credentials are never touched.

it always shows you the full plan before writing anything, and `--dry-run` previews without touching disk at all.

there is no need rebuilding the setup you already tuned!
