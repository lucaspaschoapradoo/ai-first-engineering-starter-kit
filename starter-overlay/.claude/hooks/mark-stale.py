#!/usr/bin/env python3
"""Mark engineering evidence stale after source/spec/plan/task edits.
Reads Claude Code PostToolUse JSON from stdin. Evidence/review file writes are ignored.
"""
import json, sys
from pathlib import Path
from datetime import datetime, timezone

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cwd = Path(data.get("cwd") or ".").resolve()
tool_input = data.get("tool_input") or {}
file_path = tool_input.get("file_path") or tool_input.get("path") or ""
if not file_path:
    sys.exit(0)

p = Path(file_path)
if not p.is_absolute():
    p = (cwd / p).resolve()

s = p.as_posix().lower()
# Evidence and review updates should not invalidate themselves.
if "/evidence/" in s or "/reviews/" in s or "/.ai-engineering/" in s:
    sys.exit(0)

state_dir = cwd / ".ai-engineering"
state_dir.mkdir(parents=True, exist_ok=True)
state_file = state_dir / "workflow-state.json"
state = {}
if state_file.exists():
    try:
        state = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception:
        state = {}
state.update({
    "evidenceStale": True,
    "lastRelevantChangeAt": datetime.now(timezone.utc).isoformat(),
    "lastRelevantFile": str(p)
})
state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
sys.exit(0)
