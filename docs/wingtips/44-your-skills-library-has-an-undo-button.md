# Hermes Wingtips #44: your skills library has an undo button

posted 2026-08-12. original: [https://x.com/witcheer/status/2087482141118435477](https://x.com/witcheer/status/2087482141118435477)

Hermes Wingtips #44: your skills library has an undo button.

the curator is a background pass that tidies the skills your agent creates for itself: stale ones get archived, overlapping ones get merged.  

worried it might archive a skill you cared about? it snapshots your whole skills folder before every pass, automatically.

`hermes curator rollback --list` shows every snapshot.

`hermes curator rollback` restores the newest one, and even the rollback takes a snapshot first, so you cannot lose anything trying.
