#!/bin/bash
# Polysigma Terminal Launcher
# Usage: ./start.sh [port]
# Default port: 8765

PORT=${1:-8765}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=============================================="
echo " Polysigma Terminal"
echo "=============================================="
echo " URL: http://localhost:$PORT/"
echo " API:  https://terminal.polysigma.io"
echo "=============================================="
echo ""

cd "$SCRIPT_DIR"
python3 local_terminal_server.py $PORT