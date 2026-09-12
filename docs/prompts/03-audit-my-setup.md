# Hermes Autopilot #3: audit my own setup

posted 2026-09-12. original: [https://x.com/witcheer/status/2098769643599020208](https://x.com/witcheer/status/2098769643599020208)

want to know what your Hermes Agent would change about its own setup? paste this prompt into a fresh chat. it runs hermes doctor and hermes dump, reads the report against how you actually use it, and hands you three changes with the exact line for each. it changes nothing: you run the commands yourself.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Audit your own setup on this machine and tell me what to change. Read, do not change.
</role>

<principles>
<principle name="Read only">
Run hermes doctor and hermes dump, read the output, and stop there. Change nothing: no files, no config, no installs.
</principle>
<principle name="Three changes, not thirty">
Pick the three findings that matter most for how I use you. One line each. Everything else is a footnote.
</principle>
<principle name="Exact commands">
For each change, give the one hermes config set line that makes it, and say what it does in plain words.
</principle>
</principles>

<instructions>
1. Run hermes doctor. Note every check that is not a pass.
2. Run hermes dump. Note the model, the provider, and the settings that differ from defaults.
3. Match what you found against how I actually use you in this session history.
4. Write the three changes: the finding, why it matters to me, and the exact command to run.
5. Show me the list and wait. I will run the commands myself.
</instructions>

<task>
Start with step one now.
</task>
```
