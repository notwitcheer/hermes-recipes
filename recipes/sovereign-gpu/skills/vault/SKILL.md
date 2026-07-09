---
name: vault
description: "The agent's living memory vault (~/.hermes/vault/, markdown). ALWAYS consult it for anything about the operator, their history, projects, people, or decisions; capture durable facts here."
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [memory, vault, knowledge, obsidian, productivity]
    category: productivity
---
# Memory Vault

The operator's knowledge layer: `~/.hermes/vault/`, Obsidian-compatible markdown
(YAML frontmatter + [[wikilinks]]). Sovereign by construction: plain files on disk,
no vector database service, no cloud memory provider.
Structure: `identity.md` (PRIVATE), `preferences.md`, `people/`, `projects/`,
`topics/`, `daily/`, `README.md` (index).

## Setup (once)
```
cd ~/.hermes/skills/productivity/vault
uv venv .venv && uv pip install --python .venv/bin/python sentence-transformers numpy
.venv/bin/python scripts/index_vault.py   # builds the semantic index
```
The index is CPU-only (multilingual-e5-small, brute-force cosine): a few hundred
chunks search in milliseconds. No GPU touched — the GPU belongs to the model server.

## Recall (before answering)
Before answering anything about the operator, their work, history, people, or decisions:
search the vault SEMANTICALLY first:
`~/.hermes/skills/productivity/vault/.venv/bin/python ~/.hermes/skills/productivity/vault/scripts/search.py --q "<your query>"`
(matches by meaning, returns path :: heading :: snippet). Read the top notes it returns;
fall back to `grep -ri "<term>" ~/.hermes/vault/` only if semantic search returns nothing
useful. Ground your answer in what you find and name the note.

## Capture (ACT — write the file, don't just acknowledge)
TRIGGER: when the operator says "remember", "note that", "keep in mind", "from now on",
or states a durable preference/decision/fact — you MUST create or update the relevant
vault note **with your file tools in the same turn**. Replying "noted" WITHOUT writing
the file is a FAILURE. After writing, confirm which note you updated.

## Capture details
When a lasting fact appears — a decision and its WHY, a preference, a person, a project
update — create or update the relevant note (`people/<name>.md`, `projects/<slug>.md`,
`topics/<slug>.md`, or `preferences.md`). Add frontmatter (`type, tags, created, updated`)
and link related notes with [[wikilinks]]. Durable facts go HERE, not in the bounded
MEMORY.md. AFTER creating/updating a note, re-index:
`~/.hermes/skills/productivity/vault/.venv/bin/python ~/.hermes/skills/productivity/vault/scripts/index_vault.py`.

## Privacy (load-bearing)
The vault holds PRIVATE data: the operator's real name and personal detail. It is
local-only. NEVER surface real identity or private detail in anything destined to be
published (posts, cards, captions). The operator's public identity is their public
handle only.
