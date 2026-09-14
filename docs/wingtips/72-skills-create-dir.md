# Hermes Wingtips #72: `skills.create_dir`, where new skills land

posted 2026-09-14. original: [https://x.com/witcheer/status/2099370347153805667](https://x.com/witcheer/status/2099370347153805667)

your agent writes itself a new skill after a good session, and it lands in the profile's own skills folder, on that machine, for that profile.

`create_dir` under `skills` in config.yaml moves that.

every skill the agent creates from then on is written to the folder you name, a shared repo or a folder every profile can see. the agent's own instructions follow the setting, so it knows where new skills go without being told each time.

skills you already have stay where they are and are edited in place.

```
# in ~/.hermes/config.yaml
skills:
  create_dir: /opt/brain/skills

# or from the terminal
hermes config set skills.create_dir /opt/brain/skills
```

the folder is created on the first write. skills under it still show in `hermes skills list`, `skill_view` and as `/skill-name` slash commands. `~` and `${VAR}` expand, and a relative path resolves against your Hermes home. this is the write side of [#70 `skills.external_dirs`](70-skills-external-dirs.md), which is where Hermes also reads skills from; point both at the same shared folder and you have one place for everything.

docs: [redirecting skill creation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#redirecting-skill-creation-skillscreate_dir)

hand this to your agent: "set skills.create_dir to a folder of my choice, then create a two-line test skill and tell me the path you wrote it to."
