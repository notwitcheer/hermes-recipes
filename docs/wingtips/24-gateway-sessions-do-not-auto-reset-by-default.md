# Hermes Wingtips #24: gateway sessions do not auto-reset by default

posted 2026-07-18. original: [https://x.com/witcheer/status/2078481963040530769](https://x.com/witcheer/status/2078481963040530769)

Hermes Wingtips #24: gateway sessions do not auto-reset by default.

the default is `session_reset: mode: none`, so a Telegram or Discord chat keeps its history across restarts until you say otherwise. if you want a clean slate on a schedule, opt in:

(1) `idle` resets after `idle_minutes` of quiet (default 1440, so 24h)

(2) `daily` resets once a day at `at_hour` (default 4, local time)

(3)  `both` resets on whichever comes first

before any auto-reset it saves memories and skills first.
