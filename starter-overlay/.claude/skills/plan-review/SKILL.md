---
name: plan-review
description: Run independent multi-agent review of the current solution plan for architecture, security, test strategy and simplicity before task decomposition.
disable-model-invocation: true
---

Review the current feature plan. Do not implement.

Delegate independent reviews to:
- architecture-reviewer
- security-reviewer
- test-strategy-reviewer
- simplicity-reviewer

Require each reviewer to use relevant Corporate Knowledge MCP guidance.

Consolidate findings by severity without hiding disagreements. Update the plan only after presenting findings and only when the Builder has not asked for review-only mode.

A plan is approved only with 0 CRITICAL and 0 HIGH. Write a summary under `<feature>/reviews/plan-review.md`.
