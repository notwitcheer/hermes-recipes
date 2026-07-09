# hermes-recipes

browse it as a searchable site: **https://notwitcheer.github.io/hermes-recipes/**

working configs and scripts from my [Hermes Agent](https://github.com/NousResearch/hermes-agent) walkthroughs. everything here ran on real hardware before it landed: a Mac Mini M4 that runs Hermes Agent 24/7, and an RTX 5090 Linux box for local inference.

Hermes Agent is Nous Research's open-source agent: autonomous skill creation, persistent memory with cross-session recall, cron jobs, mcp support, 20+ messaging gateways. docs: https://hermes-agent.nousresearch.com

## how this repo works

- `recipes/` has one folder per walkthrough: the exact configs and scripts I used, plus a readme with the commands and what they produced
- `CHANGELOG.md` tracks what shipped in Hermes Agent and how to use it, in plain words
- if a step has not been tested on real hardware, it does not ship here

## walkthroughs

live:

- [24/7 Hermes Agent on a Mac Mini M4: crons, approvals, and a gateway that stays up](recipes/mac-mini-24-7/): the launchd gotcha and watchdog, the `[SILENT]` cron pattern, a git-synced workspace, and the human-in-the-loop approval rule
- [Hermes Agent on a cheap VPS: zero to a Telegram gateway that survives reboot](recipes/cheap-vps/): the secure-box hardening script, the install one-liner, driving it interactively over tmux, and the systemd setup (with the #42065 install gotcha) that brings it back after a reboot
- [lock down a self-hosted Hermes Agent: what it exposes and how to keep it shut](recipes/secure-hermes/): the gateway opens no inbound port, the dashboard refuses a public bind without auth, the API server is off by default, plus secret hygiene, backup/restore, and least-privilege scoping, with an exposure-audit script
- [the sovereign GPU agent: your own Hermes on one consumer card, end to end](recipes/sovereign-gpu/): fully local serving (llama.cpp + systemd, sized for a 27B at 64K on 32GB), identity templates that stop an agent freelancing, a starter skill pack (machine-dated news digest, headless card renderer, markdown memory vault with CPU semantic search), and the drain/restore pattern for borrowing the GPU back

coming next:
- extending Hermes Agent with a custom mcp server (TypeScript)
- persistent memory and fts5 recall in practice

watch the repo for new recipes. found a problem with one? open an issue, I fix what I ship.
