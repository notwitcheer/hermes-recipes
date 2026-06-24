# lock down a self-hosted Hermes Agent: what it exposes, and how to keep it shut

a governance write-up went round recently framing a self-hosted Hermes Agent as a wide-open box. I run one 24/7, so I checked what it actually exposes, on my own hardware. the short version: the default Telegram gateway opens no inbound port, and the current release will not even let you serve the web dashboard on a public address without authentication. the real surface is two opt-in servers, and both already fail safe. this recipe is the runnable lockdown.

it complements the cheap-vps recipe, which hardens the BOX (firewall, key-only ssh, no root login). this one hardens what Hermes Agent itself exposes. tested on Hermes Agent v0.17.0, on a throwaway Hetzner x86 box (Ubuntu 24.04) for the live server steps and a Mac Mini (macOS) for the default-posture check.

## the real threat model

the Telegram (and Discord, etc.) gateway is outbound polling: it dials out to the platform, nothing dials in, so it opens no inbound port. I confirmed this on both boxes: a fresh install listens on ssh only. the surface a governance audit worries about is two opt-in servers:

1. the web **dashboard** (port 9119), which reads your `.env`.
2. the **API server** (port 8642), the OpenAI-compatible endpoint, which is a full control point into your agent and its tools.

neither runs unless you start it, and the current release guards both: the dashboard **refuses to start on a non-loopback bind unless an auth provider is registered** (there is no longer an insecure override), and the API server is off by default, binds localhost, and needs an explicit key to expose. the only way to get burned is to override those defaults yourself.

## step 1: audit your own exposure

see what Hermes actually listens on. expected: ssh only.

```bash
ss -tlnp        # linux
lsof -nP -iTCP -sTCP:LISTEN   # macOS
```

the `hermes-exposure-audit.sh` in this folder rolls this plus the checks below into one read-only command (listeners, `.env` perms, `.env`-in-git, forced `0.0.0.0` binds, the allowlist, a recent backup). on a locked-down box it prints all green.

## step 2: keep the gateway safe

the gateway needs no inbound port, so the box firewall should allow only ssh (the cheap-vps `secure-box.sh` sets exactly this). confirm:

```bash
sudo ufw status        # expect: 22/ssh ALLOW, nothing else
```

## step 3: the web dashboard, safely

the dashboard (`hermes dashboard`, port 9119) reads your `.env` and has no built-in password. it binds `127.0.0.1` by default. the rules:

- leave the default. do not pass `--host 0.0.0.0`, do not Docker-map its port to a public host, do not put it behind a public reverse proxy without auth.
- you cannot accidentally serve it unauthenticated: on v0.17.0 the old `--insecure` flag is a deprecated no-op, and a non-loopback bind with no auth provider is refused at startup:

```
Refusing to bind dashboard to 0.0.0.0 — the auth gate engages on non-loopback
binds, but no auth providers are registered. ... There is no unauthenticated
public-bind option — to keep it local, bind 127.0.0.1 and tunnel in.
```

reach it remotely over an ssh tunnel and browse localhost:

```bash
ssh -L 9119:127.0.0.1:9119 user@<your-box-ip>
# then open http://localhost:9119 on your machine
```

the tunnel means the dashboard is reachable only by someone who already has ssh to the box. if you do want it on the network, register an auth provider first (`hermes dashboard register` for Nous Portal OAuth, or a `dashboard.basic_auth` password in config.yaml).

## step 4: the API server (port 8642), safely

the OpenAI-compatible API server is **off by default** (`API_SERVER_ENABLED`); a fresh box has nothing on 8642. when on, it binds `127.0.0.1`. it is a full control point into your agent and tools, so treat it like a root shell:

- exposing it beyond localhost takes BOTH `API_SERVER_HOST=0.0.0.0` and an `API_SERVER_KEY` (8+ chars; `openssl rand -hex 32`). the key requirement is a guard, not a licence to expose. keep the host on localhost and reach it over the same ssh tunnel as the dashboard:

```bash
ssh -L 8642:127.0.0.1:8642 user@<your-box-ip>
```

## step 5: secret hygiene

```bash
ls -l ~/.hermes/.env     # expect -rw------- (600)
```

`.env` is `600` on a fresh install (confirmed on both boxes). keep it that way, never commit it (gitignore it), and rotate any key that was ever on an exposed surface. the dashboard reads `.env`, which is the other reason to keep the dashboard local.

## step 6: backup and restore

an update once wiped `~/.hermes`, so a tested backup is part of the security posture. back up the **data**, not the reinstallable agent code: the secrets, memory, and config.

```bash
mkdir -p ~/hermes-backups
tar czf ~/hermes-backups/hermes-$(date +%F).tar.gz \
  -C ~/.hermes .env config.yaml memories
# restore (after simulating loss):
tar xzf ~/hermes-backups/hermes-<date>.tar.gz -C ~/.hermes
```

I tested the round-trip: backed up, deleted `config.yaml`, restored, confirmed it came back byte-for-byte. (backing up the whole `~/.hermes` works too but it is large, since the agent install lives there; the three paths above are what you actually cannot regenerate.)

## step 7: least privilege at the action layer

network lockdown is half of it; scope what the agent can DO.

- **the approval gate.** the terminal tool routes *dangerous* commands through an approval prompt, and in unattended runs the default is deny (set `approvals.cron_mode: deny`). benign commands run freely; the gate is for the destructive ones.
- **`command_allowlist` is a pre-approval list, use it sparingly.** every pattern in it is a dangerous command that will run WITHOUT asking. keep entries specific (`git status`, a named script), and never add a catch-all like a bare shell-via-`-c` entry: that re-permits everything and defeats the gate.
- **scope tools per task with `-t <toolset>`.** an image-only job runs `-t image_gen` and cannot touch the terminal. I use this for unattended card generation: the agent has no shell to misuse.
- keep the human-in-the-loop rule: no autonomous public actions.

## step 8: what the deployment layer can't fix

binding localhost does not stop prompt injection or persistent-memory poisoning. least-privilege tools and the approval gate are the mitigations, not a fix. the full mental model (untrusted content + injection, memory poisoning, provider / MCP / profile trust) is the companion "running Hermes securely" writeup, kept separate from this recipe because it has no tested commands.

## verify your setup

run `./hermes-exposure-audit.sh`. green means: nothing inbound but ssh, the dashboard/API not on `0.0.0.0`, `.env` is `600` and not in git, a recent backup exists, and a `command_allowlist` is set. then spot-check the tunnel: from your machine, `curl http://<your-box-ip>:9119` should fail (connection refused / timeout), while the tunnelled `localhost:9119` works.

## cost

the box: reuse the cheap-vps figures (a few euros a month, billed hourly, so pennies for the throwaway box I tested this on). the hardening itself: nothing.
