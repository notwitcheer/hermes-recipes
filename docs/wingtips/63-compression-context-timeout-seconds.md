# Hermes Wingtips #63: `compression.context_timeout_seconds`

posted 2026-09-05. original: [https://x.com/witcheer/status/2096128698147557524](https://x.com/witcheer/status/2096128698147557524)

Hermes Wingtips #63: `compression.context_timeout_seconds`

when a chat gets long, Hermes summarises the older messages to free up room. a separate model writes that summary in the background while your conversation keeps going.

but what if that summary model hangs? without a guard, your whole session would sit there waiting on it.

this setting is that guard. if the summary model goes quiet for 120 seconds, Hermes stops waiting: it tries one backup model, and if that fails too it skips the summary, keeps all your messages and tells you.

`hermes config set compression.context_timeout_seconds <seconds>`

the guard only counts silence. a model that is slow but still writing gets all the time it needs. raise the number if your summary model runs on slower hardware, or set 0 to switch the guard off.
