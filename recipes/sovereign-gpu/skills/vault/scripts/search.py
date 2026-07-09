#!/usr/bin/env python3
"""Semantic search over the vault index. Usage: search.py --q "..." [--k 6]"""
import os, json, argparse
import numpy as np
from sentence_transformers import SentenceTransformer

IDX = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index"))
MODEL = "intfloat/multilingual-e5-small"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", required=True)
    ap.add_argument("--k", type=int, default=6)
    a = ap.parse_args()
    epath = os.path.join(IDX, "embeddings.npy")
    if not os.path.exists(epath):
        print("no index yet - run index_vault.py first"); return
    emb = np.load(epath)
    recs = [json.loads(l) for l in open(os.path.join(IDX, "chunks.jsonl"), encoding="utf-8")]
    model = SentenceTransformer(MODEL, device="cpu")
    q = model.encode(["query: " + a.q], normalize_embeddings=True)[0]
    sims = emb @ q
    for i in np.argsort(-sims)[:a.k]:
        r = recs[i]
        snip = " ".join(r["text"].split())[:160]
        print(f"[{sims[i]:.3f}] {r['path']} :: {r['heading'] or '(top)'} :: {snip}")

if __name__ == "__main__":
    main()
