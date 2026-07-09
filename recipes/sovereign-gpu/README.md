# the sovereign GPU agent: your own Hermes on one consumer card, end to end

I run Hermes Agent 24/7 on a headless Ubuntu server with one RTX 5090. the model weights are on my disk, inference happens on my card, the agent's memory is markdown files I can read, and the box needs zero inbound ports. this recipe is the generalised version of that deployment: the systemd units, the identity files, the starter skills and the ops lessons, so you can stand up your own without repeating my debugging.

everything here is layered on stock Hermes Agent: no fork, no gateway patches. and everything was extracted from a deployment that has been running since June 2026; the scripts were re-tested in their generalised form on the same box before publishing. tested on Ubuntu Server 26.04, an RTX 5090 32GB, Hermes Agent v0.15+. if a step is not in here, I have not tested it.

## what you get

- a model server and the Hermes gateway as boot-persistent system services, sized so a 27B model with 64K context fits a 32GB card with margin
- an identity layer that steers the model: SOUL/USER/MEMORY templates carrying the directive patterns that stop an agent from freelancing
- a starter skill pack: a morning brief with a machine-dated news digest (the "model writes, never researches" architecture), a local card renderer for a headless box, and a markdown memory vault with CPU semantic search
- the drain/restore pattern: borrow the whole GPU for a training run or benchmark and guarantee the agent comes back, safe to run from cron
- the security posture for all of it: long-polling (zero inbound ports), a platform allowlist, and a sudoers rule scoped to exactly one service

## the layout

```
identity/   SOUL.template.md, USER.template.md, MEMORY.template.md
serving/    llama-server.service, hermes-gateway.service,
            sudoers-llama-server, drain-restore.sh
skills/     daily-brief/, status-card/, vault/
scripts/    news_digest.py, news_digest.sh
```

## prerequisites

- a Linux box with an NVIDIA card that fits your chosen model (worked example throughout: 27B Q6_K + 64K context ≈ 26GB of a 32GB card)
- llama.cpp built with CUDA (`-DGGML_CUDA=ON`), and a GGUF you've picked
- Hermes Agent installed and a messaging platform configured: follow the official docs at https://hermes-agent.nousresearch.com; this recipe starts where the installer ends
- `uv` for the skill venvs (Hermes' own venv is pip-less by design; every skill that needs a dependency gets its own environment)

## part 1: serving, two system services

install `serving/llama-server.service` and `serving/hermes-gateway.service` (instructions in each file's header). the choices that matter, learned the slow way:

- **`--parallel 1`.** each extra slot divides the context between slots. one agent, one slot, the whole window.
- **stable symlink, never the blob path.** `--model` points at `~/models/current-model.gguf`, a symlink you control. model swaps become `ln -sf` + restart; the agent config never changes. `--alias` pins the API-reported name for the same reason.
- **size the context against nvidia-smi, not hope.** model file + KV cache (grows with `--ctx-size`; `q8_0` cache types halve it) + ~1GB margin.
- **the Environment= block in the gateway unit is load-bearing.** a system service has no login shell; without explicit HOME/PATH/VIRTUAL_ENV hermes resolves nothing.
- **check for squatters.** a leftover service from an earlier experiment (in my case a crash-looping vllm unit) can grab 16GB of VRAM at boot before your model server starts. `systemctl list-units --state=running | grep -iE "vllm|llama|sglang"` once, then disable what you don't recognise.

reboot test: both services come back, the agent answers on your platform, `nvidia-smi` shows the model resident. mine has survived every reboot since June.

## part 2: identity, the files that steer the model

the three templates in `identity/` are the structure of my agent's actual identity stack, with the personal config stripped and the lessons kept as comments. the load-bearing ones:

- **SOUL.md is a session-start snapshot.** edits do not reach running conversations: send `/new` or restart the gateway. if the agent "ignores" your SOUL change, this is why.
- **agents freelance unless the always-loaded memory MANDATES the exact command.** a skill that exists but is not mandated gets ignored under pressure: the model hand-rolls its own script instead of running yours, or answers from training data instead of searching its vault. the MEMORY template shows the directive shape that fixed it for me: task, arrow, skill name, exact command, and the freelance behaviour you're killing, by name.
- **USER.md is a budget-capped facts bucket** (~1400 chars in current builds), managed by the agent's own tools. facts about you, one line each. policy goes in SOUL.md; anything longer goes in the vault with a pointer line here.

## part 3: the starter skills

each skill dir drops into `~/.hermes/skills/<category>/<name>/`. setup commands are in each SKILL.md; they follow one pattern, `uv venv` per skill, because the Hermes venv is pip-less.

- **daily-brief**: one morning message: stack health (GPU temp/VRAM, services, disk, log errors), a news digest, and a kickoff nudge. the digest is the part worth stealing: an agent-driven web search returns undated snippets and the model will narrate a month-old release as breaking news (mine did, confidently). the fix is architectural: a deterministic read-only script (`scripts/news_digest.py`) collects candidates with machine-verified dates from source APIs: community threads ranked by real vote counts from the matured 12-48h window, newest GitHub release per watched repo, keyword-filtered HF daily papers. the model's entire job is picking 2-3 and writing one grounded sentence each, date kept. **the model writes; it never researches.**
- **status-card**: a Pillow card renderer for results and leaderboards. exists because a headless server has no browser: no HTML-to-screenshot path. palette and font are one config block; it ships neutral, you brand it once.
- **vault**: the agent's memory as plain markdown, Obsidian-compatible, with wikilinks, readable and editable by you, no memory-provider dependency. plus CPU semantic search (multilingual-e5-small, brute-force cosine): a few hundred chunks answer in milliseconds without touching the GPU, and it matches by meaning: in my re-test, "how much video memory does the GPU have" retrieved the note saying "RTX 5090 with 32GB VRAM" at 0.84 similarity with zero shared keywords. the skill mandates search-before-"I don't know" and write-the-note-in-the-same-turn capture.

wire the brief to a cron: `hermes cron add` with your schedule (mine fires 08:00). two gotchas from running it: after `timedatectl set-timezone` restart the gateway or crons fire on the old timezone, and after any gateway reinstall run `hermes cron list`: a reinstall can silently wipe your jobs (mine were gone for a week before I noticed; the brief just stopped arriving).

## part 4: borrowing the GPU back

`serving/drain-restore.sh` wraps any heavy job: stop the model server, run the job, and restore the server on EVERY exit path via a shell trap: success, crash, ctrl-C or timeout, the agent comes back. `serving/sudoers-llama-server` is the companion: a NOPASSWD rule scoped to starting and stopping exactly that one service, so the wrapper runs from cron without a password and without handing the agent general root. install it with `visudo -f` only (a broken sudoers file locks you out of sudo), and verify the scoping: the two allowed commands run with `sudo -n`, any other service must still prompt.

this pattern has run my unattended overnight training jobs for weeks: the agent is drained at 23:00, trains all night, and is back serving before the morning brief fires.

## part 5: the security posture

- **long-polling means zero inbound ports.** the gateway polls out to your messaging platform; nothing connects in. no reverse proxy and no port forwarding, so there is nothing exposed to keep patched. resist the urge to "improve" this.
- **allowlist your platform.** e.g. `TELEGRAM_ALLOWED_USERS=<your numeric id>` in `~/.hermes/.env` (mode 600). a negative test matters here: message the bot from a second account and confirm silence.
- **the model server binds 127.0.0.1.** the only consumer is the gateway on the same box.
- **secrets live in `.env`, mode 600**, and `.env` edits need a gateway restart to load: the gateway reads it at start, not per message.
- **privacy split by construction:** the vault holds private context and is local-only; anything the agent publishes carries your public handle. the identity templates encode the rule; the vault skill enforces it at recall time.

## what this costs to run

holding the model resident is nearly free: with the 27B loaded (24.8GB) and the agent idle, my card reports 6.5-7.8W (`nvidia-smi --query-gpu=power.draw`, sampled 2026-07-09). VRAM is the real cost, not watts: the resident model owns the card, which is exactly what the drain/restore pattern is for.
