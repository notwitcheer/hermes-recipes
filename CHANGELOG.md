# changelog

what shipped in Hermes Agent and how to use it, in my words. updated when a loop closes publicly: feature ships, walkthrough lands, configs arrive here.

## 2026-06-17

- first recipe shipped: [24/7 Hermes Agent on a Mac Mini M4](recipes/mac-mini-24-7/). running Hermes 24/7 under launchd with a watchdog, scheduled jobs that only ping you when it matters (the `[SILENT]` pattern), a git-synced workspace, and a hard human-in-the-loop approval rule. includes the macOS launchd gotcha where `hermes gateway start` can silently downgrade supervision (exit 5) and the two-line launchctl fix. tested on Hermes Agent v0.16.0, macOS 15.

## 2026-06-10

- repo initialised. structure: `recipes/` holds one folder per walkthrough with runnable configs and scripts. nothing lands here until it has run on real hardware.
