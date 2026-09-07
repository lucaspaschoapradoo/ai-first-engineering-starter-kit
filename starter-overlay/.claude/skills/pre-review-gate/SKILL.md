---
name: pre-review-gate
description: Execute the deterministic pre-PR readiness validator; use only after quality, adversarial, spec and corporate compliance evidence are current.
disable-model-invocation: true
allowed-tools: Bash(python scripts/validate_readiness.py *)
---

Run:

`python scripts/validate_readiness.py --phase pre-review`

If it exits non-zero, do not create/declare READY FOR REVIEW. Resolve each reported blocker and rerun.
