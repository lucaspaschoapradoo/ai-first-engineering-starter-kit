# 02 — Guia do Administrador / Maintainer

## Objetivo

O maintainer é responsável por manter o Starter Kit como produto de engenharia: versões, policies, MCP contract, agents, skills, hooks e configuração dos quality gates.

## 1. Repositório central

Mantenha uma fonte única, por exemplo:

```text
corporate-ai-engineering-starter/
```

Aplicações recebem versões homologadas do overlay. Não copie arquivos ad hoc entre projetos.

## 2. Versionamento

Use tags semânticas:

```text
v1.0.0
v1.1.0
v2.0.0
```

Registre no CHANGELOG:

- Spec Kit version homologada;
- Claude Code minimum tested version;
- Superpowers version/marketplace state;
- mudanças de agent prompts;
- mudanças em gates;
- mudanças no MCP contract.

## 3. Spec Kit

Inicialização recomendada:

```bash
specify init --here --force --non-interactive --integration claude --script py
specify extension add assess
```

Depois do bootstrap não execute `init` rotineiramente. Para atualização:

```bash
specify integration status
specify integration upgrade claude
specify extension update
```

Faça isso primeiro em um repositório piloto.

## 4. MCP como Knowledge Authority

O MCP precisa ser read-only para o fluxo normal de Builder. O agente de desenvolvimento consome; não governa os standards.

Recomendação de metadata por documento:

```text
id
title
domain
version
status: DRAFT | APPROVED | DEPRECATED | RETIRED
effective_date
owner
tags
applicability
supersedes
```

Claude deve usar automaticamente apenas `APPROVED`.

## 5. Contract mínimo do MCP

Idealmente o servidor oferece equivalentes funcionais de:

```text
search_guidance(query)
get_document(id)
get_related_standards(id)
get_applicable_guidance(context)
get_capability(name)
get_golden_path(domain)
get_examples(pattern)
```

Se o MCP existente possui nomes diferentes, documente o mapeamento em `engineering.config.json` e em `docs/MCP_TOOL_MAPPING.md` do projeto.

## 6. Governança de agents

Mudanças em reviewers exigem PR e pelo menos:

- um teste em feature conhecida;
- um caso com finding real;
- um caso sem finding;
- avaliação de falso positivo;
- confirmação de que o reviewer é read-only.

## 7. Governança de hooks

Hooks são código executado automaticamente. Toda mudança exige Code Review humano.

O Starter Kit usa apenas hooks determinísticos e locais. Evite prompt hooks/agent hooks como bloqueadores de produção enquanto forem experimentais.

## 8. Quality commands

Cada projeto precisa definir comandos reais em `engineering.config.json`.

Regras:

- comando precisa ser reproduzível localmente;
- retorno `0` significa sucesso;
- retorno diferente de `0` significa falha;
- não deve exigir input interativo;
- deve ser executável em CI futuramente.

## 9. Proteção de secrets

Não colocar:

- token MCP em `.mcp.json`;
- `.env` em contexto do Claude;
- credenciais em CLAUDE.md;
- secrets em prompts.

`.claude/settings.json` bloqueia leitura de arquivos `.env*` por padrão no Starter Kit.

## 10. Promote para plugin corporativo

Quando o fluxo estabilizar, considere empacotar agents/skills/hooks em um Claude Code plugin corporativo. Mantenha MCP project-scoped ou managed se for obrigatório em toda a organização.
