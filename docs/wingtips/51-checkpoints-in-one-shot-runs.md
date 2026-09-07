# Hermes Wingtips #51: checkpoints in one-shot runs

posted 2026-08-22. original: [https://x.com/witcheer/status/2091175733750124856](https://x.com/witcheer/status/2091175733750124856)

Hermes Wingtips #51: checkpoints in one-shot runs

your Hermes Agent snapshots files before it changes them, and that safety net is not limited to interactive sessions. a scripted run gets it too:

(1) hermes chat --checkpoints -q "your task"

the run snapshots each working directory before its first file change, exactly like a live session would. next time you open a session in that folder, /rollback lists those snapshots and can restore from them.

(2) hermes checkpoints status

shows every project the store knows about, with sizes and last touch, from any shell.
