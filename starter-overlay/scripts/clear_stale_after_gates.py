#!/usr/bin/env python3
"""Use only after rerunning all affected evidence gates following the latest relevant edit."""
import json
from pathlib import Path
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
p=root/".ai-engineering"/"workflow-state.json"
p.parent.mkdir(parents=True,exist_ok=True)
state={}
if p.exists():
    try: state=json.loads(p.read_text(encoding="utf-8"))
    except Exception: state={}
state["evidenceStale"]=False
state["evidenceRefreshedAt"]=datetime.now(timezone.utc).isoformat()
p.write_text(json.dumps(state,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("Evidence stale flag cleared. This script does not prove gate results; use only after rerunning required reviews/gates.")
