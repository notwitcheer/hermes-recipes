<!--
MEMORY.md is the agent's always-loaded lessons file. it lives at
~/.hermes/memories/MEMORY.md, the agent's tools append to it, and it is
budget-capped — so every line has to earn its place.

the single most important lesson from running an agent 24/7: agents
freelance unless the always-loaded memory MANDATES the exact command. a
skill that exists but isn't mandated here gets ignored under pressure — the
model improvises its own Pillow script instead of running your renderer,
"remembers" a fact instead of searching the vault, answers from training
data instead of checking. the fix is directive lines shaped like this:

  **<task> -> `<skill>` only.** Run `<exact command>`. Never <the freelance
  behaviour you're killing>.

write the mandate, not the suggestion. examples below are real patterns;
adapt the commands to your skill paths.
-->

# Lessons

- **Rendered cards/charts -> `status-card` skill only.** Run
  `~/.hermes/skills/<category>/status-card/.venv/bin/python scripts/render_card.py`.
  No hand-rolled Pillow, no HTML-to-screenshot: a headless server has no browser.

- **Operator knowledge -> `vault` skill.** Search
  `~/.hermes/skills/<category>/vault/scripts/search.py --q "<query>"` BEFORE
  saying "I don't know". On "remember <fact>": write the vault note with file
  tools THE SAME TURN — replying "noted" without writing the file is a failure.

- **<recurring heavy task> -> <skill> only, DETACHED.** <e.g. benchmarks run
  via the runner script, never inline: an inline model download can blow the
  conversation's timeout and half-finish.> WARN the operator first.

- **No AI slop in writing.** <point to the writing rules in SOUL.md, or
  inline your banned-vocabulary list here.>

- **Crons (<n>, all no-agent):** <list your scheduled jobs and their times in
  one line each. the agent should know what fires when, so it doesn't
  double-do a job or flag its own cron as an anomaly.>
