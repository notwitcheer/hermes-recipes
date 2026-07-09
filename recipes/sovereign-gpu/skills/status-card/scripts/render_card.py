#!/usr/bin/env python3
"""Branded card renderer (local, Pillow, no browser). Auto-fits height to content.

Palette and font are the config block below — swap in your brand once and
every card the agent renders matches it.
"""
import argparse, json, os
from PIL import Image, ImageDraw, ImageFont

# ---- brand config: edit these ----------------------------------------------
BG = (18, 18, 20)          # background
ACCENT = (120, 170, 255)   # headline accent, top bar, footer
TEXT = (235, 235, 235)     # body text
HIGHLIGHT = (255, 140, 100)  # top bar / emphasis
FONT_DIR = os.path.expanduser("~/.local/share/fonts/Inter")
FONT_REGULAR = "Inter-Regular.ttf"
FONT_BOLD = "Inter-Bold.ttf"
FOOTER_DEFAULT = "your-handle"
# -----------------------------------------------------------------------------

W = 1200
PAD = 90
H_MAX = 4000  # scratch height; cropped to content at the end


def font(size, bold=False):
    name = FONT_BOLD if bold else FONT_REGULAR
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except Exception:
        return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--type", required=True, choices=["finding", "leaderboard", "quote"])
    p.add_argument("--title", required=True)
    p.add_argument("--subtitle", default="")
    p.add_argument("--body", default="")
    p.add_argument("--rows", default="[]")
    p.add_argument("--footer", default=FOOTER_DEFAULT)
    p.add_argument("--out", required=True)
    a = p.parse_args()

    img = Image.new("RGB", (W, H_MAX), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([PAD, PAD, PAD + 120, PAD + 12], fill=HIGHLIGHT)
    y = PAD + 50

    for line in wrap(d, a.title, font(64, True), W - 2 * PAD):
        d.text((PAD, y), line, font=font(64, True), fill=TEXT); y += 78
    if a.subtitle:
        y += 6
        for line in wrap(d, a.subtitle, font(34), W - 2 * PAD):
            d.text((PAD, y), line, font=font(34), fill=ACCENT); y += 46
    y += 30

    if a.type in ("finding", "quote") and a.body:
        for line in wrap(d, a.body, font(40), W - 2 * PAD):
            d.text((PAD, y), line, font=font(40), fill=TEXT); y += 56
    if a.type == "leaderboard":
        for i, (label, val) in enumerate(json.loads(a.rows)):
            d.text((PAD, y), f"{i+1}. {label}", font=font(42, i == 0),
                   fill=ACCENT if i == 0 else TEXT)
            vfnt = font(42, i == 0)
            d.text((W - PAD - d.textlength(val, font=vfnt), y), val, font=vfnt,
                   fill=ACCENT if i == 0 else TEXT)
            y += 64

    y += 44
    d.line([PAD, y, W - PAD, y], fill=ACCENT, width=2)
    y += 22
    d.text((PAD, y), a.footer, font=font(30, True), fill=ACCENT)
    y += 44

    final_h = y + PAD
    img = img.crop((0, 0, W, final_h))
    img.save(a.out)
    print(f"{a.out} ({W}x{final_h})")


if __name__ == "__main__":
    main()
