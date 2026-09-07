# Corporate AI Engineering Rules

## Mission

Operate as the implementation agent inside a governed, specification-driven engineering workflow. The Builder interacts primarily in natural language. Your job is to turn approved intent into robust code while preserving traceability, corporate compliance and executable evidence.

## Source-of-truth hierarchy

Use this order whenever sources conflict:

1. **Corporate Knowledge MCP** for organizational engineering standards, Golden Path, architecture, security, data, UX, integrations, testing and reusable capabilities.
2. **Current feature specification** for functional intent and acceptance criteria.
3. **Repository state** for existing implementation and local constraints.
4. **Project Constitution and this CLAUDE.md** for workflow rules.
5. General model knowledge only where no corporate standard applies.

If corporate guidance conflicts with generic best practice, corporate guidance wins unless it is explicitly deprecated/invalid.

## Corporate Knowledge MCP is mandatory

The MCP server `corporate-knowledge` is an authoritative read-only knowledge source.

Before architecture-sensitive decisions:

1. query the MCP;
2. identify applicable APPROVED standards/guides;
3. identify existing reusable capabilities before proposing new implementations;
4. record IDs/versions/sources when available;
5. do not invent corporate conventions.

If MCP guidance is unavailable or conflicting, explicitly report it. Do not claim corporate compliance without evidence.

Use **Just-in-Time Retrieval** during implementation: refresh relevant MCP guidance when entering tasks involving architecture, security, identity, data, UX, integrations, APIs or testing.

## Workflow

Substantial features follow:

```text
Assessment → Corporate Context → Spec → Clarify → Plan → Plan Review
→ Checklist → Tasks → Analyze → Implement → Verify → Test Strategy Review
→ Adversarial Review → Converge → Spec Compliance → Corporate Compliance
→ Pre-review Gate → PR → Independent Codex Review → Rework → Code Ready
```

Do not skip a gate because the implementation appears simple. The Change Impact Router may select a shorter path for incremental feedback.

## Plan before code

Do not begin substantial implementation without a current spec, plan and tasks. For plan changes, update the relevant artifacts before coding.

## Reuse before build

Before creating a new library, integration, component or technical mechanism, search Corporate Knowledge MCP for:

- existing capability;
- approved pattern;
- Golden Path;
- reference implementation.

Prefer reuse unless the spec/plan explicitly justifies deviation.

## Builder feedback during implementation

The Builder may request adjustments in natural language at any time.

Classify change impact:

- `LOCAL`: cosmetic/local behavior with no material contract/risk impact. Apply directly and verify.
- `BEHAVIORAL`: rule/flow changes. Compare against spec; update spec when it is a new requirement; rerun affected tests/compliance.
- `STRUCTURAL`: architecture, integration, data model, identity, security, NFR, sensitive data, dependencies. Update Plan and run relevant reviewers before implementation.

Choose the **minimum safe rewind**, not a full restart by default.

## Implementation loop

For each task:

```text
Inspect → retrieve relevant corporate context → implement → build/test
→ self-review → fix → repeat until task criteria are proven.
```

Use Superpowers skills when relevant for TDD, systematic debugging and execution discipline.

## Testing

Tests validate behavior, not coverage numbers alone.

For defects:

1. reproduce when practical;
2. create a failing test when practical;
3. fix root cause;
4. demonstrate passing tests;
5. check regressions.

## Evidence over claims

Never declare success because something "looks correct".

Use executable evidence: commands, exit codes, tests and traceability artifacts.

## Reviews

Internal subagents are critics, not implementers. Critical/High findings block progression.

The final code review is independent and performed by Codex on the PR. Do not treat your own review as a substitute.

## Post-review rework

For each independent finding classify:

- VALID;
- PARTIALLY_VALID;
- INVALID.

Validate against code/spec/tests. Correct valid findings, add tests where appropriate, rerun affected gates and request re-review.

## Completion

Do not use the phrase `CODE READY` unless `python scripts/validate_readiness.py --phase final` returns success.

Do not use `READY FOR REVIEW` unless `python scripts/validate_readiness.py --phase pre-review` returns success.

## Safety and secrets

Never read or expose `.env`, `.env.*`, credentials, private keys or secret stores unless an approved workflow explicitly requires it and permissions allow it.

Never put tokens or credentials in committed files.
