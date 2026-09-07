# Hermes Wingtips #64: `AGENTS.override.md`

posted 2026-09-06. original: [https://x.com/witcheer/status/2096481734388858931](https://x.com/witcheer/status/2096481734388858931)

Hermes Wingtips #64: `AGENTS.override.md`

when you open Hermes Agent inside a project, it reads the project's AGENTS.md on every turn. that file is where a team keeps its rules: how the code is laid out, what to never touch, which commands to run.

but what if you want your own rules in that project? 

maybe you prefer shorter answers, or you want the agent to always run the tests before it reports back. editing the shared AGENTS.md pushes your habits onto everyone else.

this file is the way round it. put an `AGENTS.override.md` next to the team's AGENTS.md and Hermes loads yours instead of theirs. the tracked file stays exactly as your teammates wrote it.

`touch AGENTS.override.md`

add it to .gitignore and it never leaves your machine. it works in any folder that has an AGENTS.md, including subfolders the agent walks into during a session.
