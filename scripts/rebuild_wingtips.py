#!/usr/bin/env python3
"""Rebuild the public Wingtips index and llms.txt from per-tip files.

Source of truth is docs/wingtips/NN-*.md (as-shipped X text). The two public
URLs never change:

  https://notwitcheer.github.io/hermes-recipes/wingtips/
  https://notwitcheer.github.io/hermes-recipes/llms.txt

Run from the hermes-recipes repo root after writing a new NN-slug.md:

    python3 scripts/rebuild_wingtips.py

Wingtip post-closeout calls this in the same turn as the ledger flip.
Do not rebuild from X: free gateways flake, and the as-shipped body on
closeout is already the source.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIPS_DIR = ROOT / "docs" / "wingtips"
INDEX = TIPS_DIR / "index.md"
LLMS = ROOT / "docs" / "llms.txt"

HEADING_RE = re.compile(r"^#\s+Hermes Wingtips #(\d+)(?::\s*(.*))?$")
POSTED_RE = re.compile(
    r"^posted\s+(\d{4}-\d{2}-\d{2})\.\s+original:\s+\[([^\]]+)\]"
)
FNAME_RE = re.compile(r"^(\d{2,})-")


def parse_tip(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        raise ValueError(f"{path.name}: empty file")
    m = HEADING_RE.match(lines[0].strip())
    if not m:
        raise ValueError(f"{path.name}: first line is not a Wingtips heading")
    number = int(m.group(1))
    title = (m.group(2) or "").strip()
    posted = None
    url = None
    body_start = None
    for i, line in enumerate(lines[1:], start=1):
        pm = POSTED_RE.match(line.strip())
        if pm:
            posted = pm.group(1)
            url = pm.group(2)
            body_start = i + 1
            break
    if not posted or not url:
        raise ValueError(f"{path.name}: missing 'posted YYYY-MM-DD. original:' line")
    body_lines = lines[body_start:]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()
    body = "\n".join(body_lines)
    if not title:
        # older tips put the gotcha on a later line
        title = lines[0].replace("# ", "", 1).strip()
        title = re.sub(r"^Hermes Wingtips #\d+:\s*", "", title)
    return {
        "number": number,
        "title": title,
        "posted": posted,
        "url": url,
        "body": body,
        "filename": path.name,
    }


def load_tips() -> list[dict]:
    tips = []
    for path in sorted(TIPS_DIR.glob("*.md")):
        if path.name == "index.md":
            continue
        if not FNAME_RE.match(path.name):
            raise ValueError(f"unexpected file in wingtips/: {path.name}")
        tips.append(parse_tip(path))
    tips.sort(key=lambda t: t["number"], reverse=True)
    numbers = [t["number"] for t in tips]
    if len(numbers) != len(set(numbers)):
        dup = sorted({n for n in numbers if numbers.count(n) > 1})
        raise ValueError(f"duplicate tip numbers: {dup}")
    expected = list(range(max(numbers), 0, -1)) if numbers else []
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        extra = sorted(set(numbers) - set(expected))
        raise ValueError(f"tip numbers not a contiguous 1..N (missing={missing} extra={extra})")
    return tips


def write_index(tips: list[dict]) -> None:
    n = tips[0]["number"] if tips else 0
    rows = [
        f"- [#{t['number']}: {t['title']}]({t['filename']}) · {t['posted']} · [on X]({t['url']})"
        for t in tips
    ]
    text = "\n".join(
        [
            "# Hermes Wingtips",
            "",
            "one tested Hermes Agent tip at a time, collected so you can read the series in one place and point an agent at it.",
            "",
            f"{n} tips, #1 to #{n}. newest first. each page is the as-shipped X text. cards stay on the original posts.",
            "",
            "for agents: [llms.txt](../llms.txt) is the same series as one file.",
            "",
            'the running X search (latest-first, needs X): [from:witcheer "Hermes Wingtips"](https://x.com/search?q=from%3Awitcheer%20%22Hermes%20Wingtips%22&f=live)',
            "",
            "## the series",
            "",
            *rows,
            "",
        ]
    )
    INDEX.write_text(text, encoding="utf-8")


def write_llms(tips: list[dict]) -> None:
    chunks = [
        "# Hermes Wingtips",
        "",
        "collected as-shipped posts from @witcheer. one tested Hermes Agent tip per entry.",
        "source: https://notwitcheer.github.io/hermes-recipes/wingtips/",
        "original posts keep the cards. this file is rebuilt from docs/wingtips/ on each new tip.",
        "",
    ]
    for t in tips:
        heading = f"Hermes Wingtips #{t['number']}"
        if t["title"]:
            heading = f"{heading}: {t['title']}"
        chunks.extend(
            [
                "---",
                "",
                f"## {heading}",
                "",
                f"posted: {t['posted']}",
                f"url: {t['url']}",
                "",
                t["body"],
                "",
            ]
        )
    LLMS.write_text("\n".join(chunks), encoding="utf-8")


def main() -> int:
    if not TIPS_DIR.is_dir():
        print(f"missing {TIPS_DIR}", file=sys.stderr)
        return 1
    tips = load_tips()
    write_index(tips)
    write_llms(tips)
    n = tips[0]["number"] if tips else 0
    print(f"rebuilt {n} tips -> {INDEX.relative_to(ROOT)} and {LLMS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
