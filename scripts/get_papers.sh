#!/usr/bin/env bash
# Rebuild your own copy of the paper corpus from scripts/refs.json.
#
# The PDFs are NOT in this repo (copyright). This fetches whatever is openly
# available — expect roughly 93 of 172. The rest are paywalled and need your
# institutional access; scripts/still_missing.json lists them with DOIs.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "1/3  downloading open-access papers into the central corpus…"
python3 scripts/run_download.py || true
echo "2/3  Europe PMC recovery pass…"
python3 scripts/recover_pmc.py || true
echo "3/3  hard-linking into resources/papers/ and writing INDEX.md…"
python3 scripts/link_into_topic.py
