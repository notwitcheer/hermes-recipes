# Hermes Wingtips #33: checkpoints

posted 2026-07-28. original: [https://x.com/witcheer/status/2082169101913604120](https://x.com/witcheer/status/2082169101913604120)

Hermes Wingtips #33: checkpoints

checkpoints snapshot your project before Hermes Agent writes, patches or runs a destructive command, and `/rollback` puts things back.

(1) `hermes chat --checkpoints`

you can turns them on for one session, or keep them on with `checkpoints: enabled: true` in config.yaml.

(2) `/rollback`

lists every snapshot; `/rollback diff <N>` previews the change and `/rollback <N> <file>` restores a single file. everything lives under `~/.hermes/checkpoints/`.

turning this on is great before a big refactor, before letting an agent loose on an unfamiliar repo, or before trying yolo mode!

as an example, here is a live recovery on my own box:
