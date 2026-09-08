#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
from _feature import find_feature

root = Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument("--phase", choices=["pre-review","final"], required=True)
parser.add_argument("--feature-dir")
args=parser.parse_args()
blockers=[]

def loadj(path, label):
    if not path.exists():
        blockers.append(f"missing {label}: {path.relative_to(root)}")
        return None
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        blockers.append(f"invalid JSON {label}: {e}")
        return None

cfgp=root/"engineering.config.json"
cfg=loadj(cfgp,"engineering config")
if not cfg:
    print("READINESS: FAIL"); [print("- "+b) for b in blockers]; sys.exit(1)
if not cfg.get("configured"):
    blockers.append("engineering.config.json configured=false")
for k,v in (cfg.get("mcp",{}).get("toolMapping",{}) or {}).items():
    if isinstance(v,str) and v.startswith("__MAP_"):
        blockers.append(f"MCP tool mapping not configured: {k}")
try:
    feature=find_feature(root,args.feature_dir)
except Exception as e:
    blockers.append(str(e)); feature=None
if feature:
    for fn in ["spec.md","plan.md","tasks.md"]:
        if not (feature/fn).exists(): blockers.append(f"missing {fn}")
    ev=feature/cfg.get("evidence",{}).get("directoryName","evidence")
    for fn in cfg.get("evidence",{}).get("requiredPreReview",[]):
        if not (ev/fn).exists(): blockers.append(f"missing evidence/{fn}")
    q=loadj(ev/"quality-run.json","quality evidence")
    if q and not q.get("passed"): blockers.append("quality-run did not pass")
    t=loadj(ev/"test-strategy-review.json","test strategy review")
    if t and str(t.get("status","")).upper() not in {"PASS","SUFFICIENT"}: blockers.append("test strategy review not PASS/SUFFICIENT")
    a=loadj(ev/"adversarial-review.json","adversarial review")
    if a:
        if str(a.get("status","")).upper() != "PASS": blockers.append("adversarial review not PASS")
        sev=a.get("openFindings",{}) or {}
        if int(sev.get("critical",0))>0 or int(sev.get("high",0))>0: blockers.append("adversarial review has Critical/High findings")
    s=loadj(ev/"spec-compliance.json","spec compliance")
    if s and str(s.get("status","")).upper() != "PASS": blockers.append("spec compliance not PASS")
    c=loadj(ev/"corporate-compliance.json","corporate compliance")
    if c:
        if not c.get("mcpConnected"): blockers.append("corporate compliance did not confirm MCP connection")
        if str(c.get("status","")).upper() != "PASS": blockers.append("corporate compliance not PASS")
        standards=c.get("standards",[]) or []
        if not standards and not c.get("noApplicableStandards"):
            blockers.append("corporate compliance has no standards and no noApplicableStandards rationale")
        if c.get("noApplicableStandards") and not c.get("noApplicableStandardsRationale"):
            blockers.append("noApplicableStandards requires rationale")
    statep=root/".ai-engineering"/"workflow-state.json"
    state=None
    if statep.exists():
        try:
            state=json.loads(statep.read_text(encoding="utf-8"))
            if state.get("evidenceStale") and state.get("lastRelevantChangeAt"):
                from datetime import datetime
                changed=datetime.fromisoformat(state["lastRelevantChangeAt"].replace("Z","+00:00")).timestamp()
                current_required=list(cfg.get("evidence",{}).get("requiredPreReview",[]))
                if args.phase=="final": current_required += list(cfg.get("evidence",{}).get("requiredFinal",[]))
                stale_files=[]
                for fn in current_required:
                    fp=ev/fn
                    if fp.exists() and fp.stat().st_mtime < changed:
                        stale_files.append(fn)
                if stale_files:
                    blockers.append("evidence older than the latest relevant edit: "+", ".join(stale_files))
        except Exception as e: blockers.append("workflow-state.json invalid: "+str(e))
    if args.phase=="final":
        ir=loadj(ev/"independent-review.json","independent review")
        if ir:
            if str(ir.get("status","")).upper() not in {"RESOLVED","PASS"}: blockers.append("independent review not RESOLVED/PASS")
            sev=ir.get("openFindings",{}) or {}
            if int(sev.get("critical",0))>0 or int(sev.get("high",0))>0: blockers.append("independent review has Critical/High findings")
            med=int(sev.get("medium",0))
            accepted=ir.get("acceptedMediumFindings",[]) or []
            if med>0 and len(accepted)<med: blockers.append("open Medium findings require documented acceptance or resolution")
if blockers:
    print(f"READINESS ({args.phase}): FAIL")
    for b in blockers: print("- "+b)
    sys.exit(1)
# Successful validation proves required evidence is current relative to the latest relevant edit.
statep=root/".ai-engineering"/"workflow-state.json"
if statep.exists():
    try:
        st=json.loads(statep.read_text(encoding="utf-8"))
        st["evidenceStale"]=False
        statep.write_text(json.dumps(st,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    except Exception:
        pass
print(f"READINESS ({args.phase}): PASS")
print(f"Feature: {feature.relative_to(root) if feature else 'n/a'}")
print("READY FOR REVIEW" if args.phase=="pre-review" else "CODE READY")
sys.exit(0)
