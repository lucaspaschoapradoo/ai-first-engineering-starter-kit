---
name: adversarial-review
description: Run a read-only adversarial review that attempts to find concrete defects before independent PR review.
disable-model-invocation: true
---

Delegate to `adversarial-reviewer` against the current feature implementation.

Write `<feature>/evidence/adversarial-review.json` using the repository template.

0 CRITICAL and 0 HIGH are required to pass. Valid findings return to implementation/testing and must be re-reviewed after correction.
