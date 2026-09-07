# Hermes Wingtips #65: `hermes sessions import`

posted 2026-09-07. original: [https://x.com/witcheer/status/2096849498173530284](https://x.com/witcheer/status/2096849498173530284)

Hermes Wingtips #65: `hermes sessions import`

if you have a conversation going in Claude Code or Codex CLI, you can carry it on in Hermes Agent.

say you spent an hour with another coding agent on a feature, and now you want Hermes to take the next step with all of that context. instead of explaining it again from scratch, you bring the conversation over.

`hermes sessions import`

it lists the sessions it finds on your machine, newest first. pick one and it becomes a Hermes session you can resume like any other.

what comes across is the conversation itself: your messages, the answers, and a short note wherever a tool ran. your other agent's files are only read, never changed.

this is different from `hermes import-agent`, which moves your setup (instructions, skills). this one moves the chat.
