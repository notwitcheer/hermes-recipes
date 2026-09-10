# Hermes Wingtips #68: /skill-name

posted 2026-09-10. original: [https://x.com/witcheer/status/2097944804084556003](https://x.com/witcheer/status/2097944804084556003)

Hermes Wingtips #68: `/skill-name`

you installed a skill, told your agent to use it, and the replies still come back the same.

every installed skill is also a slash command. `/humanizer rewrite this reply in my voice` loads the skill for that turn and then runs your request with it. the bare name on its own loads it and the agent asks what you need.

several skills stack in one message: every leading `/skill` is loaded, the rest of the line is the instruction.

for the agent to pick a skill without being told, it reads a short index of every description. a description that opens with when to use the skill gets picked up. one that opens with background does not get that far.

`/humanizer <your request>`
