# Hermes Wingtips #11: toolsets: all doesn't include the kanban tools

posted 2026-07-02. original: [https://x.com/witcheer/status/2072698059788562587](https://x.com/witcheer/status/2072698059788562587)

Hermes Wingtips #11: toolsets: all doesn't include the kanban tools

you want a Hermes agent to manage your kanban board for you, creating and moving tasks itself? it needs the kanban tools.

here is what you need to understand:

you give that agent's profile toolsets: [all] in ~/.hermes/config.yaml, figuring "all" covers everything, and the agent still turns up with no kanban tools at all.

the reason is that the kanban toolset is opt-in. all loads the everyday tools, but a few specialist ones (kanban is one) are left out on purpose, so a normal chat is not cluttered with board commands it will never use. you have to ask for kanban by name.

the fix is to add it to that profile's toolsets, spelled out:

```
toolsets:
- kanban
```

you need to do this only when you set up an agent to drive the board. the workers the board spawns on its own to run a task already get the tools automatically. this is just for the driver.
