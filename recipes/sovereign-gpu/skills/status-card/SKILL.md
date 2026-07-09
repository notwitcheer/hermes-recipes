---
name: status-card
description: "THE way to make a branded image card for a result, finding, leaderboard or quote. Runs a tested local Pillow renderer -> ready PNG. ALWAYS use this for cards; never hand-roll Pillow or HTML (a headless server has no browser)."
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [design, card, branding, sovereign]
    category: creative
---
# Status Card

## When to Use
When the operator wants an image card for a result, a finding/stat, a leaderboard or a quote,
e.g. to attach to a post. Fully local (Pillow), no cloud, no API key. Cards auto-fit height.

## Setup (once)
This skill ships with a dedicated venv pattern: Hermes' own venv is pip-less, so give the
skill its own environment with uv:

```
cd ~/.hermes/skills/creative/status-card
uv venv .venv && uv pip install --python .venv/bin/python pillow
```

Edit the brand config block at the top of `scripts/render_card.py` (colors, font path,
default footer) once. If the font files are missing the renderer falls back to Pillow's
default font instead of crashing.

## Procedure
Run the renderer with the terminal tool, using THIS skill's dedicated venv python:

```
~/.hermes/skills/creative/status-card/.venv/bin/python \
  ~/.hermes/skills/creative/status-card/scripts/render_card.py \
  --type <finding|leaderboard|quote> --title "..." [--subtitle "..."] \
  [--body "..."] [--rows '[["label","value"],...]'] --out /tmp/card.png
```

- `finding` / `quote`: use `--title`, optional `--subtitle`, `--body`.
- `leaderboard`: use `--title`, optional `--subtitle`, and `--rows` (JSON list of
  [label, value]); row 1 is highlighted.
Then attach `/tmp/card.png` in the reply.

## Pitfalls
- Keep titles short (<~60 chars); the renderer wraps but a very long title looks cramped.
- Never put the operator's real identity on a card; the footer is the public handle.
- `leaderboard` rows are strictly 2 columns ([label, value]) — 3+ columns crash with
  `ValueError: too many values to unpack`. For multi-column comparisons use `finding`
  with the comparison formatted as plain text lines in `--body`.

## Verification
`file /tmp/card.png` should report `PNG image data, 1200 x <auto-height>`.
