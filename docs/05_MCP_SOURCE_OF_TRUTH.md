# 05 — Corporate Knowledge MCP como Source of Truth

## Princípio

> Claude conhece engenharia de software. A organização determina como engenharia deve ser feita aqui.

O MCP é a **Knowledge Authority** para:

- Golden Path;
- arquitetura;
- coding standards;
- segurança;
- dados;
- UX / Design System;
- integração;
- testes;
- componentes/capabilities reutilizáveis;
- exemplos aprovados;
- convenções;
- compliance.

## Hierarquia de fontes

1. Corporate Knowledge MCP — padrão corporativo.
2. Feature Spec — requisito funcional.
3. Repositório — estado técnico atual.
4. CLAUDE.md / Constitution — regras operacionais.
5. Conhecimento geral do modelo — somente quando não existir padrão corporativo aplicável.

## Fail closed

Se o MCP estiver indisponível:

- não declarar compliance;
- não inventar standard;
- não tomar decisão arquitetura-sensitive como se fosse corporativa;
- registrar `MCP_UNAVAILABLE`.

## Retrieval obrigatório

### Antes da Specification

Descobrir constraints e capabilities.

### Durante Clarification

Consultar MCP antes de perguntar ao Builder questões normativas.

### Durante Plan

Aplicar `Reuse before Build`.

### Durante Implementation

Just-in-Time Retrieval por task/domínio.

### Durante Corporate Compliance

Reconsultar/revalidar standards críticos.

## Evidence contract

`corporate-context.json` e `corporate-compliance.json` precisam registrar:

- conexão MCP confirmada;
- queries/domínios pesquisados;
- documentos usados;
- `id`, `version`, `status` e `domain` quando disponíveis;
- capabilities reutilizadas;
- conflicts;
- exceptions;
- no-applicable-standards rationale quando aplicável.

## Modelo recomendado de documento no MCP

```json
{
  "id": "ARCH-012",
  "title": "Backend Layering Standard",
  "domain": "architecture",
  "version": "4.2",
  "status": "APPROVED",
  "effective_date": "2026-08-01",
  "owner": "Enterprise Architecture",
  "tags": ["java", "backend"],
  "applicability": ["corporate", "core"],
  "supersedes": "ARCH-009"
}
```

## Tool contract ideal

O Starter Kit não assume nomes de ferramentas porque o MCP já existe. O contrato funcional desejável é:

- pesquisar guidance;
- obter documento por ID;
- descobrir guidance aplicável ao contexto;
- descobrir capabilities;
- obter Golden Path;
- obter exemplos aprovados;
- descobrir relacionados/sucessores.

Documente os nomes reais em `engineering.config.json`.

## Proteção

O MCP de conhecimento utilizado pelo Builder deve, preferencialmente, ser read-only.

Processo de alteração de standard:

```text
Proposal → Review → Approval → Publish
```

O agente consumidor não deve editar a fonte de verdade.
