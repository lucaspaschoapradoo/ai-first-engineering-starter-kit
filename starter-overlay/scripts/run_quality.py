#!/usr/bin/env python3
import argparse, json, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
from _feature import find_feature

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--feature-dir")
args = parser.parse_args()
config_path = root / "engineering.config.json"
if not config_path.exists():
    print("BLOCK: engineering.config.json not found")
    sys.exit(2)
config = json.loads(config_path.read_text(encoding="utf-8"))
if not config.get("configured"):
    print("BLOCK: engineering.config.json configured=false. Configure real project quality commands first.")
    sys.exit(2)
commands = [x for x in config.get("qualityCommands", []) if x.get("enabled")]
if not commands:
    print("BLOCK: no enabled qualityCommands")
    sys.exit(2)
try:
    feature = find_feature(root, args.feature_dir)
except Exception as e:
    print(f"BLOCK: {e}")
    sys.exit(2)
ev = feature / config.get("evidence", {}).get("directoryName", "evidence")
ev.mkdir(parents=True, exist_ok=True)
results=[]
all_ok=True
for item in commands:
    cmd=item.get("command","")
    if not cmd or "__CONFIGURE" in cmd:
        results.append({"name":item.get("name"),"command":cmd,"passed":False,"returnCode":None,"error":"not configured"})
        all_ok=False
        continue
    print(f"\n==> {item.get('name')}: {cmd}")
    cp=subprocess.run(cmd, cwd=root, shell=True, text=True, capture_output=True)
    print(cp.stdout)
    if cp.stderr:
        print(cp.stderr, file=sys.stderr)
    ok=cp.returncode==0
    all_ok &= ok
    results.append({
        "name": item.get("name"), "command": cmd, "passed": ok,
        "returnCode": cp.returncode,
        "stdoutTail": cp.stdout[-4000:], "stderrTail": cp.stderr[-4000:]
    })
out={"passed":all_ok,"runAt":datetime.now(timezone.utc).isoformat(),"feature":str(feature.relative_to(root)),"results":results}
(ev/"quality-run.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"\nEvidence: {ev/'quality-run.json'}")
sys.exit(0 if all_ok else 1)
