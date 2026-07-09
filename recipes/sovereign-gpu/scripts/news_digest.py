#!/usr/bin/env python3
"""Dated news candidates for the morning brief digest.

Every item carries a machine-verified date from its source API — no web-search
snippets, so nothing stale can masquerade as fresh. The brief model WRITES
from this list; it never adds items of its own.

Edit the config block for your interests. Sources:
- reddit via Arctic Shift (keyless; reddit.com 403s server IPs). Posts younger
  than ~12h haven't accumulated votes, so the matured 12-48h window is ranked
  by real score.
- newest GitHub release per watched repo (unauthenticated API, 60 req/h is
  plenty for a daily run).
- HuggingFace daily papers, keyword-filtered.
"""

import time
from datetime import datetime, timedelta, timezone

import httpx

# ---- config: edit these ------------------------------------------------------
SUBREDDIT = "LocalLLaMA"
MIN_SCORE = 50
RELEASE_REPOS = ["ggml-org/llama.cpp", "vllm-project/vllm",
                 "sgl-project/sglang", "unslothai/unsloth"]
PAPER_KEYWORDS = ["llm", "language model", "quantization", "inference",
                  "attention", "moe", "speculative", "kv cache", "efficient",
                  "on-device", "decoding", "distill"]
# ------------------------------------------------------------------------------

UA = {"User-Agent": "morning-digest/1.0 (read-only)"}


def fetch_reddit_top(client, top_n=5):
    # posts younger than ~12h have not accumulated votes yet, so rank the
    # matured 12-48h window by real score (Arctic Shift re-crawls update it)
    now = int(time.time())
    r = client.get(
        "https://arctic-shift.photon-reddit.com/api/posts/search",
        params={"subreddit": SUBREDDIT, "after": now - 48 * 3600,
                "before": now - 12 * 3600, "limit": 100, "sort": "desc"},
    )
    r.raise_for_status()
    posts = [p for p in r.json()["data"]
             if not p.get("over_18") and (p.get("score") or 0) >= MIN_SCORE]
    posts.sort(key=lambda p: p.get("score") or 0, reverse=True)
    out = []
    for p in posts[:top_n]:
        day = datetime.fromtimestamp(p["created_utc"], tz=timezone.utc)
        link = p.get("permalink")
        url = ("https://www.reddit.com" + link) if link else ""
        out.append(f"- [reddit, {day:%Y-%m-%d}, {p.get('score', 0)} pts, "
                   f"{p.get('num_comments', 0)} comments] "
                   f"{p.get('title', '')[:130]} — {url}")
    return out


def fetch_releases(client, hours=48):
    floor = datetime.now(timezone.utc) - timedelta(hours=hours)
    out = []
    for repo in RELEASE_REPOS:
        r = client.get(f"https://api.github.com/repos/{repo}/releases",
                       params={"per_page": 3},
                       headers={"Accept": "application/vnd.github+json"})
        if r.status_code != 200:
            continue
        newest = None
        for rel in r.json():
            pub = rel.get("published_at")
            if not pub:
                continue
            when = datetime.fromisoformat(pub.replace("Z", "+00:00"))
            if when < floor:
                continue
            # repos like llama.cpp cut several tagged builds a day; the
            # digest only needs the newest one per repo
            if newest is None or when > newest[0]:
                newest = (when, rel)
        if newest:
            when, rel = newest
            out.append(f"- [release, {when:%Y-%m-%d}] {repo.split('/')[1]} "
                       f"{rel.get('tag_name', '')}: {rel.get('name', '')[:90]} — "
                       f"{rel.get('html_url', '')}")
        time.sleep(1)
    return out


def fetch_hf_papers(client, top_n=3):
    r = client.get("https://huggingface.co/api/daily_papers",
                   params={"limit": 25})
    r.raise_for_status()
    out = []
    today = datetime.now(timezone.utc)
    relevant = [item for item in r.json()
                if any(k in (item.get("paper", {}).get("title") or "").lower()
                       for k in PAPER_KEYWORDS)]
    for item in relevant[:top_n]:
        paper = item.get("paper", {})
        pid = paper.get("id", "")
        title = (paper.get("title") or "").replace("\n", " ")[:120]
        out.append(f"- [hf-paper, {today:%Y-%m-%d}] {title} — "
                   f"https://huggingface.co/papers/{pid}")
    return out


def main():
    lines, errors = [], []
    with httpx.Client(timeout=20, headers=UA, follow_redirects=True) as client:
        for name, fn in [("reddit", fetch_reddit_top),
                         ("releases", fetch_releases),
                         ("hf-papers", fetch_hf_papers)]:
            try:
                lines += fn(client)
            except Exception as e:
                errors.append(f"{name}: {type(e).__name__}")

    if not lines:
        note = f" (sources down: {', '.join(errors)})" if errors else ""
        print(f"news digest: no dated candidates this morning{note}")
        return

    print("NEWS CANDIDATES — every date is machine-verified from the source API.")
    print("Write digest lines ONLY from items below; always keep the [date].")
    for ln in lines:
        print(ln)
    if errors:
        print(f"(sources down this morning: {', '.join(errors)})")


if __name__ == "__main__":
    main()
