---
name: corporate-context
description: Discover authoritative Corporate Knowledge MCP guidance, Golden Path, approved capabilities and constraints for a feature before specification/planning or when new technical context is needed.
argument-hint: "<feature or change description>"
---

Perform Corporate Context Discovery for: $ARGUMENTS

Mandatory:
1. Confirm the `corporate-knowledge` MCP is available.
2. Search broadly enough to cover relevant architecture, security, data, UX, integration and testing domains.
3. Identify approved Golden Path/patterns and reusable capabilities.
4. Prefer documents with status APPROVED. Flag DEPRECATED/RETIRED and find successor when possible.
5. Record concrete source IDs/versions/titles/domains when available.
6. Identify conflicts or missing guidance.
7. Do not implement code.

If a current feature directory exists, write/update:
- `<feature>/corporate-context.md`
- `<feature>/corporate-context.json`

JSON must include: `mcpConnected`, `retrievedAt`, `queries`, `standards`, `capabilities`, `conflicts`, `missingGuidance`.
