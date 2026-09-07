---
name: run-quality
description: Run the project's deterministic configured quality commands and save machine-readable evidence for readiness gates.
disable-model-invocation: true
allowed-tools: Bash(python scripts/run_quality.py *)
---

Run:

`python scripts/run_quality.py`

Do not reinterpret a failed command as success. If a quality command fails, diagnose and fix through the normal implementation loop, then rerun this skill.
