---
name: code-ready
description: Execute the final deterministic readiness gate after independent review/rework; this is the only approved way to declare CODE READY.
disable-model-invocation: true
allowed-tools: Bash(python scripts/validate_readiness.py *)
---

Run:

`python scripts/validate_readiness.py --phase final`

Only if exit code is 0 may you state `CODE READY`. Otherwise report blockers exactly and continue the necessary loop.
