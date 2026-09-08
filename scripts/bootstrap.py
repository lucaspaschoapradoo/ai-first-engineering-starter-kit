#!/usr/bin/env python3
import argparse, json, shutil, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
OVERLAY=HERE/"starter-overlay"

def run(cmd,cwd):
    print("$ "+" ".join(cmd))
    cp=subprocess.run(cmd,cwd=cwd)
    if cp.returncode!=0:
        raise SystemExit(cp.returncode)

def merge_dict(a,b):
    out=dict(a)
    for k,v in b.items():
        if k in out and isinstance(out[k],dict) and isinstance(v,dict): out[k]=merge_dict(out[k],v)
        elif k in out and isinstance(out[k],list) and isinstance(v,list):
            existing=out[k]
            for item in v:
                if item not in existing: existing.append(item)
            out[k]=existing
        else: out[k]=v
    return out

def merge_json(src,dst):
    incoming=json.loads(src.read_text(encoding="utf-8"))
    current={}
    if dst.exists():
        try: current=json.loads(dst.read_text(encoding="utf-8"))
        except Exception as e: raise SystemExit(f"Cannot merge invalid JSON {dst}: {e}")
    merged=merge_dict(current,incoming)
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(merged,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def copy_tree(src,dst,overwrite=False):
    for p in src.rglob("*"):
        if p.is_dir() or "__pycache__" in p.parts or p.suffix == ".pyc": continue
        rel=p.relative_to(src); target=dst/rel
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and not overwrite:
            print(f"KEEP existing: {target}")
        else:
            shutil.copy2(p,target); print(f"COPY: {target}")

parser=argparse.ArgumentParser(description="Apply Corporate AI Engineering Starter Kit to an application repository")
parser.add_argument("--target",required=True)
parser.add_argument("--skip-speckit",action="store_true")
parser.add_argument("--overwrite",action="store_true",help="Overwrite existing corporate overlay files (use carefully)")
args=parser.parse_args()
target=Path(args.target).expanduser().resolve()
target.mkdir(parents=True,exist_ok=True)
if not (target/".git").exists():
    print("WARNING: target is not currently a Git repository. Initialize Git before team use.")
if not args.skip_speckit:
    try:
        subprocess.run(["specify","version"],check=True,capture_output=True,text=True)
    except Exception:
        raise SystemExit("Spec Kit CLI not found. Install with: uv tool install specify-cli")
    run(["specify","init","--here","--force","--non-interactive","--integration","claude","--script","py"],target)
    run(["specify","extension","add","assess"],target)
# files copied directly
for name in ["CLAUDE.md","AGENTS.md","engineering.config.json"]:
    src=OVERLAY/name; dst=target/name
    if dst.exists() and not args.overwrite:
        if name=="CLAUDE.md":
            text=dst.read_text(encoding="utf-8")
            marker="# Corporate AI Engineering Rules"
            if marker not in text:
                dst.write_text(text.rstrip()+"\n\n---\n\n"+src.read_text(encoding="utf-8"),encoding="utf-8")
                print("APPEND corporate rules to existing CLAUDE.md")
            else: print("KEEP existing CLAUDE.md (corporate marker found)")
        else: print(f"KEEP existing {name}; compare with starter manually")
    else:
        shutil.copy2(src,dst); print(f"COPY: {dst}")
# JSON merges
merge_json(OVERLAY/".claude/settings.starter.json", target/".claude/settings.json")
merge_json(OVERLAY/".mcp.starter.json", target/".mcp.json")
# copy directories
for d in [".claude/agents",".claude/skills",".claude/hooks","scripts","templates","prompts",".github",".ai-engineering"]:
    copy_tree(OVERLAY/d,target/d,overwrite=args.overwrite)
# append gitignore
lines=(OVERLAY/".gitignore.append").read_text(encoding="utf-8").splitlines()
gitignore=target/".gitignore"
existing=gitignore.read_text(encoding="utf-8").splitlines() if gitignore.exists() else []
changed=False
for line in lines:
    if line not in existing:
        existing.append(line); changed=True
if changed: gitignore.write_text("\n".join(existing)+"\n",encoding="utf-8")
# evidence dirs
(target/".ai-engineering"/"local").mkdir(parents=True,exist_ok=True)
print("\nBOOTSTRAP COMPLETE")
print("Next steps:")
print("1) Configure CORPORATE_MCP_URL/auth and run: claude mcp list")
print("2) Map real MCP tools and quality commands in engineering.config.json; set configured=true")
print("3) In Claude Code install Superpowers: /plugin install superpowers@claude-plugins-official")
print("4) Run /speckit.constitution using prompts/00_CONSTITUTION_PROMPT.md")
print("5) Run: python scripts/validate_starter.py")
