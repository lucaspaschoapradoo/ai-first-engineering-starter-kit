---
name: test-strategy-review
description: Independently evaluate test completeness against specification, code and corporate test guidance after implementation.
disable-model-invocation: true
---

Delegate to `test-strategy-reviewer`.

Write `<feature>/evidence/test-strategy-review.json` using the template in `templates/evidence/test-strategy-review.example.json`.

If gaps exist, status is FAIL until missing tests are implemented and the reviewer is rerun.
