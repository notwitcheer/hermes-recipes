# release explainer #4: live subagent steering

posted 2026-09-03. original: [https://x.com/witcheer/status/2095466188822237649](https://x.com/witcheer/status/2095466188822237649)

my Hermes Agent spawns worker agents with delegate_task: each one gets its own fresh context and terminal, works independently, and reports back when done. 

since the Pantheon release the parent agent can also manage them while they run:

(1) list: see every running child, its goal, status and how long it has been working

(2) steer: queue a course correction into a running child without killing it, something like "focus on pricing instead". it lands at the child's next step and the in-flight work survives

(3) stop: end a child early, the partial result still comes back

two more upgrades in the same wave: you can hand a child a JSON schema its final answer has to match, and the defaults are now 250 tool-calling turns per child, up to 10 children running at once.

https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
