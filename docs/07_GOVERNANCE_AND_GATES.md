# 07 — Governance e Gates

## Definition of Ready para implementar

- Spec existente.
- Clarification concluído.
- Corporate context consultado.
- Plan existente.
- Plan Review sem Critical/High.
- Tasks existentes.
- Analyze sem inconsistência material.

## Pre-review Gate

Antes do PR:

- quality-run PASS;
- test strategy PASS;
- adversarial review sem Critical/High;
- Spec Kit converge sem trabalho restante material;
- spec compliance PASS;
- corporate compliance PASS;
- MCP evidence atual;
- evidence report criado.

## Final Code Ready Gate

Tudo do Pre-review +:

- Codex independent review concluído;
- findings Critical = 0;
- findings High = 0;
- Mediums corrigidos ou formalmente aceitos com rationale/owner;
- rework revalidado;
- evidence não stale após última mudança.

## Severidade

- CRITICAL — bloqueia.
- HIGH — bloqueia.
- MEDIUM — corrigir ou aceitar formalmente.
- LOW — recomendação.
- NIT — opcional.

## Evidence over claims

Nunca aceitar como gate:

```text
"Claude disse que passou."
```

Aceitar:

```text
comando executado + exit code + resultado registrado + rastreabilidade.
```
