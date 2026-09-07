# 04 — Workflow detalhado e regras de transição

## Fase 0 — Idea Assessment

**Entrada:** oportunidade, problema ou ideia.

**Saída:** decisão GO / NEEDS CLARIFICATION / KILL.

**Regra:** assessment não altera código.

## Fase 1 — Corporate Context Discovery

**Objetivo:** descobrir constraints corporativos antes de especificar solução.

**Obrigatório:** consulta ao Corporate Knowledge MCP.

**Saídas mínimas:** standards, capabilities, Golden Path, exemplos e gaps.

## Fase 2 — Specification

**Objetivo:** definir WHAT/WHY.

Não colocar decisão técnica que pertence ao Plan, exceto constraints corporativos mandatórios encontrados no MCP.

## Fase 3 — Clarification

Ordem de resolução:

```text
Spec/repo → MCP → Builder
```

Nunca inventar resposta corporativa.

## Fase 4 — Solution Plan

**Objetivo:** definir HOW.

O plano deve referenciar standards/capabilities do MCP.

## Fase 5 — Multi-Agent Plan Review

Reviewers independentes:

- architecture-reviewer;
- security-reviewer;
- test-strategy-reviewer;
- simplicity-reviewer.

Blocking condition:

```text
Critical > 0 OR High > 0
```

## Fase 6 — Task Decomposition / Analyze

Tasks devem ser pequenas, verificáveis e rastreáveis à spec.

## Fase 7 — Implementation

Claude implementa task-by-task.

Para cada task relevante, usar **Just-in-Time MCP Retrieval** antes de decisões de arquitetura, segurança, dados, UX, integração ou testes.

## Fase 8 — Builder Feedback Loop

O Builder pode iterar durante implementação sem voltar ao início.

O `change-impact-classifier` determina o menor rewind necessário.

## Fase 9 — Verification

Quality commands são determinísticos e configurados por projeto.

## Fase 10 — Test Strategy Review

Revisar cobertura comportamental, não apenas percentual de cobertura.

## Fase 11 — Adversarial Review

Assume presença de defeito e tenta quebrar a solução.

## Fase 12 — Convergence + Compliance

Três perguntas diferentes:

1. **Convergence:** tudo que Spec/Plan/Tasks exigem foi implementado?
2. **Spec Compliance:** comportamento entregue atende requisitos/ACs?
3. **Corporate Compliance:** decisões seguem standards/Golden Path do MCP?

## Fase 13 — Independent Review

Codex revisa PR independentemente do agente implementador.

## Fase 14 — Rework

Rework não é obediência cega ao reviewer. Findings são avaliados com evidência.

## Fase 15 — Code Ready

É um estado verificável, não uma declaração do modelo.
