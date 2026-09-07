# Hermes Wingtips #45: if you ever want to bring an existing OpenClaw setup into Hermes Agent, there is a command for that

posted 2026-08-13. original: [https://x.com/witcheer/status/2087812081110147134](https://x.com/witcheer/status/2087812081110147134)

Hermes Wingtips #45: if you ever want to bring an existing OpenClaw setup into Hermes Agent, there is a command for that.

`hermes claw migrate` imports your settings, memories and skills. you can add `--dry-run` and it only shows you the plan, nothing is touched.

worth knowing: 

(1) API keys and tokens stay behind unless you explicitly pass `--migrate-secrets`

(2) before anything is applied a restore-point zip of your Hermes home is written, so the move itself is undoable.
