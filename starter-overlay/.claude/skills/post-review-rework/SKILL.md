---
name: post-review-rework
description: Process independent Codex PR review findings, validate each finding, implement justified fixes and prepare final review evidence.
disable-model-invocation: true
---

Process the latest independent PR review.

For each finding:
1. classify VALID / PARTIALLY_VALID / INVALID;
2. cite code/spec/test evidence for the classification;
3. for valid portions, reproduce when practical, add/adjust tests, fix root cause and rerun affected quality checks;
4. for invalid findings, document concise evidence rather than changing correct code;
5. update `<feature>/evidence/independent-review.json` using the template;
6. after any implementation change, rerun stale spec/corporate/adversarial evidence as required.

Final review status cannot be RESOLVED while Critical/High findings remain open.
