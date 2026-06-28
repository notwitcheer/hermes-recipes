# hermes recipes

working configs and scripts from my [Hermes Agent](https://github.com/NousResearch/hermes-agent) walkthroughs. everything here ran on real hardware before it landed: a Mac Mini M4 that runs Hermes Agent 24/7, and an RTX 5090 Linux box for local inference.

Hermes Agent is Nous Research's open-source agent: autonomous skill creation, persistent memory with cross-session recall, cron jobs, MCP support, 20+ messaging gateways. [docs](https://hermes-agent.nousresearch.com).

## the almanac

these recipes usually start as posts in the witcheer almanac, my weekly notes from running local AI on my own hardware. read the back issues or subscribe at [buttondown.com/witcheer](https://buttondown.com/witcheer).

## the bar

every command in a recipe ran on real hardware before publishing. no copy-paste from docs, no untested steps, no "should work". if a step has not been tested, it does not ship here.

## recipes

- [24/7 Hermes Agent on a Mac Mini M4](recipes/mac-mini-24-7/README.md): the launchd gotcha and watchdog, the `[SILENT]` cron pattern, a git-synced workspace, the human-in-the-loop approval rule
- [Hermes Agent on a cheap VPS](recipes/cheap-vps/README.md): the secure-box hardening script, the install one-liner, driving it over tmux, the systemd setup that survives a reboot
- [lock down a self-hosted Hermes Agent](recipes/secure-hermes/README.md): what the gateway, dashboard, and API server expose, secret hygiene, backup/restore, least-privilege scoping, an exposure-audit script

## also here

- [threads & cards](threads.md): the Wingtips tips, heads-up cards, and builder spotlights, collected in one place
- [changelog](changelog.md): what shipped in Hermes Agent and how to use it, in my words

found a problem with a recipe? open an issue. I fix what I ship.
