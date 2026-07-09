---
name: daily-brief
description: "Compose the operator's morning brief: stack health + a dated news digest + a kickoff nudge. Triggered by the morning cron. OUTPUT: terse — bullet points, minimal prose, scannable. Under ~25 lines."
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [productivity, briefing, cron, monitoring]
    category: productivity
---
# Daily Brief

## When to Use
Triggered by the morning cron job (`hermes cron add` — see the recipe README). Produce ONE
concise message with three sections, in the agent's voice. Keep the whole thing under ~35 lines.

## Procedure
1. **Stack health** (local, via terminal tool — run these and summarize in 3-4 lines):
   - `nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,memory.used,memory.total --format=csv,noheader`
   - `systemctl is-active llama-server; systemctl is-active hermes-gateway`
   - `df -h / | tail -1`
   - `grep -iE "error|traceback|exception" ~/.hermes/logs/*.log 2>/dev/null | tail -5` (say "clean" if none)
   Flag anything red: a service not "active", disk >85%, GPU temp >80C.
2. **News digest** (local script — every candidate carries a machine-verified date):
   run `~/.hermes/scripts/news_digest.sh` via the terminal tool. It prints dated
   candidates from configured sources (community threads ranked by real vote counts,
   fresh GitHub releases). Pick 2-3 genuinely interesting items FROM THAT LIST ONLY.
   For EACH item:
   - write ONE complete sentence, grounded only in what the candidate line actually
     says — no invented numbers or claims;
   - KEEP THE ITEM'S [date] in your line, e.g. "(Jul 7)" — never say "just released"
     or "new" for anything older than yesterday; the date decides, not you;
   - end the line with the item's real `https://...` source URL.
   You may `web_extract` a chosen item's URL to enrich the sentence, but never to add
   new items. If the script prints "no dated candidates", write "digest: quiet night"
   and continue — never block the brief, never fabricate sources.
3. **Kickoff nudge**: one short line — what's worth building today, or a question.

## Why the digest is a script and not web search
An agent-driven web search returns undated snippets, and the model will narrate anything
as fresh news — a month-old release reads exactly like yesterday's. The architecture rule
this skill encodes: **the model WRITES, it never researches.** Machine-dated candidates
come from a deterministic read-only script; the model's job is selection and one good
sentence per item.

## Pitfalls
- The high GPU utilization you see during this run is YOUR OWN inference generating
  this brief — never flag it as a runaway process.
- This runs unattended; if a command errors, note it briefly and move on rather than
  aborting.
- After `timedatectl set-timezone`, restart the gateway or this cron fires on the old
  timezone.
