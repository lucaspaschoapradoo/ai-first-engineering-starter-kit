---
name: change-request
description: Route a Builder's implementation adjustment through the minimum safe workflow path instead of forcing a full restart.
argument-hint: "<requested adjustment>"
---

Process Builder change request: $ARGUMENTS

Use `change-impact-classifier`.

LOCAL:
- implement directly;
- run affected verification;
- refresh preview/evidence.

BEHAVIORAL:
- compare with spec;
- update spec if this is a new requirement;
- update tests;
- implement;
- rerun affected spec/test/compliance gates.

STRUCTURAL:
- update spec if needed;
- update plan;
- query Corporate MCP;
- run relevant plan reviewers;
- update tasks;
- only then implement.

Explain the classification and selected rewind briefly before acting.
