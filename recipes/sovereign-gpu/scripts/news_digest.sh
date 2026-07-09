#!/bin/bash
# Dated news-candidate collector for the brief digest. Read-only.
# Needs a venv with httpx (Hermes' own venv is pip-less):
#   uv venv ~/.hermes/venvs/web-research
#   uv pip install --python ~/.hermes/venvs/web-research/bin/python httpx
exec ~/.hermes/venvs/web-research/bin/python ~/.hermes/scripts/news_digest.py
