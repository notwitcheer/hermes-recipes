#!/usr/bin/env python3
"""Index the memory vault for semantic search (local, CPU). Re-runnable; overwrites the index."""
import os, re, glob, json
import numpy as np
from sentence_transformers import SentenceTransformer

VAULT = os.path.expanduser(os.environ.get("VAULT_DIR", "~/.hermes/vault"))
IDX = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index"))
MODEL = "intfloat/multilingual-e5-small"

def strip_frontmatter(t):
    if t.startswith("---"):
        end = t.find("\n---", 3)
        if end != -1:
            return t[end + 4:]
    return t

def chunk(text, max_chars=1600):
    parts = re.split(r"(?m)^(#{1,6}\s.*)$", text)
    out = []
    pre = parts[0] if parts else ""
    if pre.strip():
        out.append(("", pre.strip()))
    for i in range(1, len(parts), 2):
        head = parts[i].strip("# ").strip()
        body = (parts[i + 1] if i + 1 < len(parts) else "").strip()
        if not body:
            continue
        if len(body) <= max_chars:
            out.append((head, body))
        else:
            for j in range(0, len(body), max_chars):
                out.append((head, body[j:j + max_chars]))
    return out

def main():
    os.makedirs(IDX, exist_ok=True)
    model = SentenceTransformer(MODEL, device="cpu")
    recs, texts = [], []
    for path in sorted(glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(path, VAULT)
        body = strip_frontmatter(open(path, encoding="utf-8").read())
        for head, ch in chunk(body):
            if not ch.strip():
                continue
            recs.append({"path": rel, "heading": head, "text": ch})
            texts.append("passage: " + ch)
    if not texts:
        print("no vault content to index"); return
    emb = model.encode(texts, normalize_embeddings=True, batch_size=16, show_progress_bar=False)
    np.save(os.path.join(IDX, "embeddings.npy"), np.asarray(emb, dtype=np.float32))
    with open(os.path.join(IDX, "chunks.jsonl"), "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"indexed {len(recs)} chunks from {VAULT} -> {IDX}")

if __name__ == "__main__":
    main()
