# Local workflow state

This directory stores project-level workflow state used by deterministic gates.

- `workflow-state.json` is created/updated by hooks and scripts.
- `local/` is gitignored and can hold machine-local diagnostics.

Feature evidence itself belongs under the active Spec Kit feature directory:

```text
specs/<feature>/evidence/
```
