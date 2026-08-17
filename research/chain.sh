#!/bin/bash
# Wait for the main download to finish, then run recovery + hard-linking.
PY=/Users/faye_valentine/miniconda3/envs/compalgoclaw/bin/python
cd "$(dirname "$0")/.."
while pgrep -f "run_download.py" > /dev/null; do sleep 60; done
echo "=== main download done $(date) ===" 
echo "=== Europe PMC recovery pass ==="
$PY research/recover_pmc.py
echo "=== hard-linking into topic ==="
$PY research/link_into_topic.py
echo "=== chain complete $(date) ==="
