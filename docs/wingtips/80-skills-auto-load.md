# Hermes Wingtips #80: skills.auto_load, the skills you want in every session, pinned

posted 2026-09-22. original: [https://x.com/witcheer/status/2102275176138178793](https://x.com/witcheer/status/2102275176138178793)

Hermes Agent loads a skill when a task calls for it. some skills you want in every session whatever the task: a house style, a review checklist, the way you write commits.

new in Hermes Agent (v0.21.4 and newer): this key pins them. every name on the list is fully loaded at the start of every new session, on the CLI, on every gateway platform, in cron jobs.

```yaml
skills:
  auto_load:
    - my-workflow
    - github-pr-workflow
```

resolved once, when the prompt is first built, so the prompt stays cache-stable. an edit to the skill shows up in the next session.

`hermes -s <skill>` does the same for one launch. per profile, empty by default.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auto-loading-skills-every-session](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auto-loading-skills-every-session)
