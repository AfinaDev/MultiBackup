#!/bin/bash

set -e

VENV_DIR=".venv"
PID_FILE="backup.pid"

if [ ! -d "$VENV_DIR" ]; then
    echo "[~] Creating virtual environment"
    python3 -m venv "$VENV_DIR"
fi

echo "[~] Activating virtual environment"
source "$VENV_DIR/bin/activate"

echo "[~] Installing dependencies"
pip install --upgrade pip
pip install -r requirements.txt

if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
        echo "[!] Existing backup script found with PID: $OLD_PID. Killing it..."
        kill "$OLD_PID"
        sleep 1
    fi
fi

echo "[~] Starting backup script in background"
nohup python3 main.py > backup.log 2>&1 &

NEW_PID=$!
echo $NEW_PID > "$PID_FILE"

echo "[+] Backup script started with PID: $NEW_PID"
echo "[+] Logs: backup.log"
