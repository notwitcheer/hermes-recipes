<!--
USER.md is the agent's facts-about-the-operator bucket. it lives at
~/.hermes/memories/USER.md and the agent's own tools manage it — expect it
to be edited BY the agent, and expect a character budget (~1400 chars by
default in current Hermes builds). that budget is the design constraint:

- facts only, not policy. behaviour rules belong in SOUL.md or MEMORY.md;
  this file is what the agent knows about YOU.
- if it's derivable from a longer document, put the document in the memory
  vault and keep one pointer line here.
- one line per fact. the budget goes fast.

replace everything in <angle brackets>.
-->

# Operator

- Public identity: **<public handle>**. Use it in anything public. Real
  identity is private — never publish it.
- **Primary focus: <the current project, one line>.**
- <how you like to work with the agent: e.g. "hands-dirty learner — explain
  commands and the why", or "just give me the command".>
- <where you publish: platforms + handles the agent may reference.>

## Machines

- **<this box>**: <GPU, role>. The agent lives here.
- **<other machine>**: <role>. <reachable from here or not — say it
  explicitly, agents will happily try to ssh somewhere they shouldn't.>

## Style

- <output preferences: e.g. terse status updates, bullets over prose.>
- <brand details the agent needs for artifacts: colors, fonts — or "none".>
