# changelog

what shipped in Hermes Agent and how to use it, in my words. updated when a loop closes publicly: feature ships, walkthrough lands, configs arrive here.

## 2026-07-09

- fourth recipe shipped: [the sovereign GPU agent](recipes/sovereign-gpu/). the generalised version of my own 24/7 deployment on an RTX 5090: llama-server and the gateway as boot-persistent systemd services (with the context-sizing arithmetic and the `--parallel 1` slot gotcha), SOUL/USER/MEMORY identity templates carrying the directive patterns that stop an agent freelancing, a starter skill pack (a morning brief whose news digest only writes from machine-dated candidates, a Pillow card renderer for a browserless box, a markdown memory vault with CPU semantic search), a trap-guarded drain/restore script with a one-service sudoers scope, and the zero-inbound-ports security posture. every script re-tested in its generalised form on the same box before landing here. tested on Ubuntu Server 26.04, an RTX 5090 32GB, Hermes Agent v0.15+.

## 2026-06-17

- first recipe shipped: [24/7 Hermes Agent on a Mac Mini M4](recipes/mac-mini-24-7/). running Hermes 24/7 under launchd with a watchdog, scheduled jobs that only ping you when it matters (the `[SILENT]` pattern), a git-synced workspace, and a hard human-in-the-loop approval rule. includes the macOS launchd gotcha where `hermes gateway start` can silently downgrade supervision (exit 5) and the two-line launchctl fix. tested on Hermes Agent v0.16.0, macOS 15.

## 2026-06-10

- repo initialised. structure: `recipes/` holds one folder per walkthrough with runnable configs and scripts. nothing lands here until it has run on real hardware.
