---
name: corporate-compliance
description: Revalidate the current implementation against authoritative Corporate Knowledge MCP guidance before PR, recording standards and capabilities used.
disable-model-invocation: true
---

Delegate to `corporate-compliance-reviewer`.

This is a fresh compliance check, not a restatement of the initial corporate context.

Write `<feature>/evidence/corporate-compliance.json` from the repository template.

Requirements for PASS:
- MCP reachable;
- applicable guidance retrieved;
- only approved/current guidance treated as authoritative;
- no blocking violation;
- conflicts/exceptions explicitly recorded;
- if no standard applies, `noApplicableStandards=true` with a concrete rationale.
