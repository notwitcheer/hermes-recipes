# Hermes Agent on a cheap VPS: zero to a Telegram gateway that survives reboot

I put Hermes Agent on a fresh cloud VPS, talked to it over Telegram, set it a goal and watched it work, then made it come back on its own after a reboot. this recipe is the whole path, from an empty Ubuntu box to a gateway running unattended under systemd, including the install gotcha that bites every unattended setup and the one-line way around it.

everything below ran on my own box: a Hetzner CX23 (x86, 2 vCPU, 4GB RAM, 40GB disk) on Ubuntu 24.04.4 LTS, running Hermes Agent v0.16.0 (release 2026.6.5, the Surface Release). if a step is not in here, I have not tested it.

## what you get

- Hermes Agent installed on a cheap Linux VPS with one command, running as a non-root user
- a Telegram gateway you talk to from your phone, locked to your account only
- the interactive agent reachable over tmux, so a dropped ssh session does not kill your work
- the gateway running under systemd, so it comes back on its own after a crash or reboot
- a hardened box: key-only ssh, no root login, a firewall, swap

## prerequisites

- a VPS that stays on. mine is a Hetzner CX23; any x86 box with 4GB RAM and ~10GB free disk works (see the cost section for why x86 and why 10GB).
- an ssh key on your own machine (`ssh-keygen -t ed25519` if you do not have one)
- a Telegram account
- a model for the agent. this recipe uses Nous Portal (`hermes setup --portal`), which is OAuth, no API key to manage. any provider Hermes supports works.

## part 1: spin up and secure the box

create the server at your provider: Ubuntu 24.04, an **x86** instance (not Arm, see the cost section), and paste your ssh public key at create time. on Hetzner that is a CX23.

a fresh public box needs a few minutes of hardening before you put an agent on it. the `secure-box.sh` in this folder does it in one pass: apt upgrade, a 2GB swapfile, a non-root sudo user with your key, key-only ssh with no root login, and a firewall that allows only ssh. edit the two variables at the top (`NEW_USER` and `SSH_PUBKEY`), copy it over, and run it as root:

```bash
scp secure-box.sh root@<your-vps-ip>:
ssh root@<your-vps-ip> 'bash secure-box.sh'
```

one thing worth knowing: this image shipped with `PasswordAuthentication` set to **yes**, even though I created the box with an ssh key. the script sets it to no. before you close the root session, open a second terminal and confirm the new user works, so a mistake cannot lock you out:

```bash
ssh hermes@<your-vps-ip>
```

from here on you are `hermes`, not root.

## part 2: install Hermes Agent

one command, run as your non-root user:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
hermes --version
```

the installer detects Ubuntu and uses apt; there is no Homebrew assumption on Linux. it pulls its own toolchain (uv, Python 3.11, Node.js 22, ripgrep, ffmpeg, and a Playwright Chromium for browser tools) into `~/.hermes`, so it does not touch your system Python. on my box it landed `Hermes Agent v0.16.0`, Python 3.11.15.

this is the heavy step: it took the disk from 1.2GB used to 7.8GB, about 6.6GB, most of it the browser engine and node. plan for ~10GB free. run over a plain ssh command (no terminal), the installer prints `Setup wizard skipped (no terminal available)`, which is fine: the next step is the setup.

## part 3: point it at a model

```bash
hermes setup --portal
```

this is OAuth against Nous Portal: it prints a URL and a code, you approve it in your browser, and the box is wired to a model with no API key sitting in a file. (if you would rather bring your own provider, run `hermes model` and pick one; the key goes in `~/.hermes/.env`.) Hermes needs a model with at least 64k context.

## part 4: talk to it over tmux

on a box you sit next to, you run `hermes`. on a VPS, the moment your ssh drops, a foreground session dies with it. tmux fixes that: start the session inside tmux, detach, and it keeps running.

```bash
sudo apt-get install -y tmux
tmux new -s hermes        # then, inside:  hermes
```

to leave it running, detach with `Ctrl-b` then `d`. reconnect later from anywhere:

```bash
ssh hermes@<your-vps-ip>
tmux attach -t hermes
```

first boot of the interactive agent takes a moment (mine spent ~29 seconds loading the model and skills before the prompt appeared). once it is up you can chat, and the slash commands work. `/goal` is the one worth showing: it sets a standing goal the agent works on across turns, with a judge model checking after each turn whether it is done.

```
/goal check this VPS total RAM and free disk using shell tools, then report both on one line and mark the goal done
```

mine ran the shell command itself and came back with `VPS total RAM: 3.7Gi, free disk space: 28G` in about 12 seconds. that is the agent using its own tools on the box, not me.

keep the two ideas separate: **tmux** keeps an interactive session alive across a dropped ssh connection, but not across a reboot. for the unattended gateway that must survive a reboot, you want systemd, which is the next part.

## part 5: the Telegram gateway

create a bot: message `@BotFather` on Telegram, `/newbot`, and copy the token. get your numeric user id from `@userinfobot`. then configure the gateway:

```bash
hermes gateway setup
```

pick Telegram, paste the token, and set the allowed users to your numeric id so only you can talk to it. the token lives in `~/.hermes/.env`, the rest in `~/.hermes/gateway.json`.

`setup` only writes config. it does not start anything, so the bot will not answer yet. that catches people out: the bot is silent because nothing is polling Telegram. start it in the foreground once to check it connects:

```bash
hermes gateway run
```

you want to see, in the log:

```
gateway.run: Connecting to telegram...
[Telegram] Connected to Telegram (polling mode)
gateway.run: ✓ telegram connected
```

polling mode means the gateway reaches out to Telegram; nothing connects in to your box, which is why the firewall needs no inbound port beyond ssh. send your bot a message; it should answer. then stop the foreground gateway with `Ctrl-C`, because you cannot have two things polling the same bot token at once, and the next step does it as a service.

## part 6: make it survive reboot

`hermes gateway install` registers the gateway as a systemd service so it restarts on crash and comes back after a reboot.

here is the gotcha. on this version the installer asks two `[Y/n]` questions, and there is no flag to skip them. if you run it over a non-interactive ssh command (the natural thing when scripting a box), it gets no answer, aborts, and installs nothing (Hermes issue #42065). the fix is to feed the answers in on stdin:

```bash
printf 'n\nY\n' | hermes gateway install
```

the two questions are "start the gateway now?" and "start automatically on login/boot?". the `n` then `Y` above says: do not start it this second, but do enable it on boot. the installer also turns on user-session lingering for you, which is what lets a user service run before you have logged in. confirm linger is on (this is what makes "survives reboot" true, not only "survives logout"):

```bash
loginctl show-user $USER -p Linger     # want: Linger=yes
```

start it and check it:

```bash
hermes gateway start
systemctl --user status hermes-gateway
```

you want `active (running)` and `NRestarts=0`. on my box the gateway used about 280MB and the whole machine sat at ~556MB, comfortable on 4GB.

now the real test. reboot the box and do not touch it:

```bash
sudo reboot
```

mine came back in about 12 seconds, the gateway had started on its own, reconnected to Telegram, and answered the next message I sent, with the conversation history from before the reboot intact. that is the whole point of this recipe.

## the approval rule, and what is next

the gateway runs the agent unattended, so be deliberate about what it is allowed to do on its own. on my own setup the rule I never break is that the agent has no path to post anywhere public by itself: it drafts, I approve on Telegram, and publishing is a thing only I do. if you wire this box into anything that can post, keep a human in that loop.

for the patterns that sit on top of a running gateway, scheduled jobs that only message you when something matters, a git-synced workspace, the draft-and-approve flow, see the companion recipe, [24/7 Hermes Agent on a Mac Mini](../mac-mini-24-7/). they are platform-agnostic; the only thing the Mac recipe does differently is the part where it keeps the gateway alive, which on Linux is the systemd service above instead of launchd.

## verify your setup

1. `systemctl --user status hermes-gateway`: `active (running)`, `NRestarts=0`
2. message your bot from Telegram: it answers, and ignores anyone not in your allowed users
3. `loginctl show-user $USER -p Linger`: `Linger=yes`
4. reboot the box, wait, message the bot again without logging in: it answers

## what breaks first (and the fix)

- **the bot is silent after `gateway setup`**: setup only writes config. start the service (`hermes gateway start`) or run it in the foreground to see why.
- **`gateway install` does nothing over ssh**: the non-interactive prompt abort (#42065). use `printf 'n\nY\n' | hermes gateway install`, or run it from an interactive shell.
- **gateway is up but dies on reboot**: linger is off. `sudo loginctl enable-linger $USER`.
- **a `RuntimeError: There is no current event loop` in the logs on shutdown**: harmless on this version. it fires as the process is torn down on a `SIGTERM` reboot; the gateway still drains cleanly and restarts. it is noise, not a failure.
- **install runs out of disk**: the install needs ~10GB free. a 1GB-disk box will not fit it.

## cost

the box is the only spend here. mine is a Hetzner CX23 at $0.012/hour, capped at $7.79/month (Hetzner's US pricing as of 2026-06-18; the EU CX22 is the same shape, cheaper). the model is whatever you point it at; Nous Portal has a free tier, and I ran the whole thing on a free model.

two notes on "a $5 VPS", which Hermes' own docs suggest:

- **memory is not the limit.** the gateway used ~280MB, the whole box ~556MB. 1GB of RAM is enough.
- **disk is the limit.** the install is ~6.6GB (browser engine, node, Python). a 1GB or 10GB disk image is tight; give it ~20GB and stop worrying.
- **use x86, not Arm.** there is an open report of the gateway crash-looping under systemd on Arm/aarch64 after an update (Hermes issue #42126). I ran x86 with auto-update off and never saw it. until that closes, x86 is the safe pick for an unattended box.
