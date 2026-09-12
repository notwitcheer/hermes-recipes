# Hermes Wingtips #70: `skills.external_dirs`, one shared skills folder

posted 2026-09-12. original: [https://x.com/witcheer/status/2098679753960034724](https://x.com/witcheer/status/2098679753960034724)

you keep your skills in one folder for every agent tool you use, or your team keeps them in a shared repo.

Hermes Agent can scan those folders too.

add `external_dirs` under `skills` in config.yaml and every skill it finds there joins the index, shows up in `hermes skills list`, and answers to its `/skill-name` slash command, the same as a skill you installed yourself.

if a skill with the same name lives in both places, your local copy wins.

```yaml
skills:
  external_dirs:
    - /home/shared/team-skills
    - ${SKILLS_REPO}/skills
```

or from the terminal:

```
hermes config set skills.external_dirs '["/home/shared/team-skills"]'
```

paths take `~` and environment variables; a folder that does not exist is skipped. a writable external folder can be edited by the agent's `skill_manage` tool, so use filesystem permissions if the shared set must stay read-only.

docs: [external skill directories](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#external-skill-directories)

hand this to your agent: "list every folder on this machine that holds SKILL.md files outside ~/.hermes/skills and tell me which ones are worth adding to skills.external_dirs. change nothing."
