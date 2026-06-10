# hermes-recipes

working configs and scripts from my [hermes agent](https://github.com/NousResearch/hermes-agent) walkthroughs. everything here ran on real hardware before it landed: a mac mini m4 that runs hermes agent 24/7, and an rtx 5090 linux box for local inference.

hermes agent is nous research's open-source agent: autonomous skill creation, persistent memory with cross-session recall, cron jobs, mcp support, 20+ messaging gateways. docs: https://hermes-agent.nousresearch.com

## how this repo works

- `recipes/` has one folder per walkthrough: the exact configs and scripts i used, plus a readme with the commands and what they produced
- `CHANGELOG.md` tracks what shipped in hermes agent and how to use it, in plain words
- if a step has not been tested on real hardware, it does not ship here

## walkthroughs

coming first:

- hermes agent on a cheap vps: zero to telegram gateway
- 24/7 hermes agent on a mac mini m4: crons and approval flows
- extending hermes agent with a custom mcp server (typescript)
- persistent memory and fts5 recall in practice

watch the repo for new recipes. found a problem with one? open an issue, i fix what i ship.
