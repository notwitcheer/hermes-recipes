# hermes-recipes

working configs and scripts from my [Hermes Agent](https://github.com/NousResearch/hermes-agent) walkthroughs. everything here ran on real hardware before it landed: a Mac Mini M4 that runs Hermes Agent 24/7, and an RTX 5090 Linux box for local inference.

Hermes Agent is Nous Research's open-source agent: autonomous skill creation, persistent memory with cross-session recall, cron jobs, mcp support, 20+ messaging gateways. docs: https://hermes-agent.nousresearch.com

## how this repo works

- `recipes/` has one folder per walkthrough: the exact configs and scripts I used, plus a readme with the commands and what they produced
- `CHANGELOG.md` tracks what shipped in Hermes Agent and how to use it, in plain words
- if a step has not been tested on real hardware, it does not ship here

## walkthroughs

live:

- [24/7 Hermes Agent on a Mac Mini M4: crons, approvals, and a gateway that stays up](recipes/mac-mini-24-7/): the launchd gotcha and watchdog, the `[SILENT]` cron pattern, a git-synced workspace, and the human-in-the-loop approval rule

coming next:

- Hermes Agent on a cheap vps: zero to Telegram gateway
- extending Hermes Agent with a custom mcp server (TypeScript)
- persistent memory and fts5 recall in practice

watch the repo for new recipes. found a problem with one? open an issue, I fix what I ship.
