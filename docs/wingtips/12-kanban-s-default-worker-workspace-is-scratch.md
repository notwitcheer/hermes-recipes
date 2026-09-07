# Hermes Wingtips #12: kanban's default worker workspace is scratch

posted 2026-07-03. original: [https://x.com/witcheer/status/2073051003482456511](https://x.com/witcheer/status/2073051003482456511)

Hermes Wingtips #12: kanban's default worker workspace is scratch

you're handing a kanban task to a Hermes agent and want to keep the files it writes? one thing to know before you run it.

by default each kanban worker runs in a scratch workspace, and Hermes clears that workspace the moment the task completes. indeed, throwaway chores should not leave directories behind.

to keep the output, give the task its own workspace when you create it:

```
hermes kanban create "your task" --workspace dir:/absolute/path
```

two things to get right:

(1) name the workspace with dir: for anything you want to survive the run. no flag means scratch, cleared on completion.

(2) make the path absolute. Hermes accepts a relative path at create with no error, then rejects it when the worker spawns.
