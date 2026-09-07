# Hermes Wingtips #13: keep your Hermes session db lean

posted 2026-07-05. original: [https://x.com/witcheer/status/2073728504869396765](https://x.com/witcheer/status/2073728504869396765)

Hermes Wingtips #13: keep your Hermes session db lean

your Hermes agent keeps every session in one SQLite db at ~/.hermes/state.db, and we ship auto-prune off by default, so none of your history disappears: it all stays searchable.

we keep it lean: hundreds of sessions sit in
