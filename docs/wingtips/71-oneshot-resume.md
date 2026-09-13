# Hermes Wingtips #71: `hermes -z --resume`, one-shot calls that keep the thread

posted 2026-09-13. original: [https://x.com/witcheer/status/2099034806466015383](https://x.com/witcheer/status/2099034806466015383)

you call Hermes Agent from a script or a cron job with `hermes -z`: one prompt in, the final answer out, nothing else printed.

the next call can continue that same conversation. add `--resume latest` and the earlier turns come back with it, so a second prompt can build on the first answer. a session id or a session title works in place of `latest`.

it is the same agent, the same tools and the same skills as your normal chat, with the interactive layer stripped off.

```
hermes -z "summarise the open pull requests on this repo"

hermes -z "now list the three that touch the gateway" --resume latest
```

the prompt goes straight after `-z`; put `--resume` before `-z` or after the prompt. `-z` also reads stdin (`hermes -z "summarise this" < notes.txt`), and `--usage-file report.json` writes tokens, api calls and an estimated cost after the run. tool output stays out of the answer; `hermes chat --oneshot -q "..."` keeps it in the transcript.

docs: [hermes -z, scripted one-shot](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes--z-prompt--scripted-one-shot)

hand this to your agent: "write me a shell script that asks you three follow-up questions about this repo with hermes -z, each call resuming the previous one, and prints the three answers. show it before saving."
