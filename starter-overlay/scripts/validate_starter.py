#!/usr/bin/env python3
import json, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=[
 "CLAUDE.md","AGENTS.md","engineering.config.json",".mcp.json",".claude/settings.json",
 ".claude/agents/architecture-reviewer.md",".claude/agents/security-reviewer.md",
 ".claude/skills/corporate-context/SKILL.md","scripts/run_quality.py","scripts/validate_readiness.py"
]
issues=[]
for r in required:
    if not (root/r).exists(): issues.append("missing "+r)
try:
    cfg=json.loads((root/"engineering.config.json").read_text(encoding="utf-8"))
    if not cfg.get("configured"): issues.append("engineering.config.json configured=false (expected until project commands/MCP mapping are configured)")
except Exception as e: issues.append("engineering.config.json invalid: "+str(e))
if issues:
    print("STARTER VALIDATION: ATTENTION")
    for x in issues: print("- "+x)
    sys.exit(1)
print("STARTER VALIDATION: PASS")
