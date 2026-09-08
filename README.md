# Corporate AI Engineering Starter Kit — Camada 1

Starter Kit para materializar a esteira **AI Engineering Workflow** no **VS Code + Claude Code**, cobrindo o ciclo da ideia ao pós-Code Review.

## Objetivo

Padronizar um fluxo em linguagem natural que preserve velocidade para o Builder sem abrir mão de engenharia disciplinada, rastreabilidade, revisão independente e compliance corporativo.

Fluxo-alvo:

```text
IDEIA
  ↓
ASSESSMENT
  ↓
CORPORATE CONTEXT DISCOVERY (MCP)
  ↓
SPECIFICATION
  ↓
CLARIFICATION LOOP
  ↓
SOLUTION PLAN
  ↓
MULTI-AGENT PLAN REVIEW
  ↓
CHECKLIST / TASKS / ANALYZE
  ↓
IMPLEMENTATION WITH CLAUDE CODE
  ↕ Builder feedback em linguagem natural
  ↓
CONTINUOUS VERIFICATION
  ↓
TEST STRATEGY REVIEW
  ↓
ADVERSARIAL REVIEW
  ↓
SPEC COMPLIANCE
  ↓
CORPORATE MCP COMPLIANCE
  ↓
PRE-REVIEW GATE
  ↓
PULL REQUEST
  ↓
CODEX INDEPENDENT REVIEW
  ↓
REWORK LOOP
  ↓
FINAL READINESS GATE
  ↓
CODE READY
```

## Componentes

- **GitHub Spec Kit** — Spec-Driven Development e rastreabilidade.
- **Superpowers** — práticas de engenharia, TDD, debugging e execução disciplinada.
- **Claude Code** — agente principal de planejamento/implementação.
- **Corporate Knowledge MCP** — fonte de verdade de Golden Path, arquitetura, convenções e guidelines.
- **Subagents Claude** — Architecture, Security, Testing, Simplicity, Adversarial, Compliance e Change Impact.
- **Codex** — Code Review independente no Pull Request.
- **Gates executáveis** — validação local de qualidade, evidências e readiness.

## Como usar este pacote

Este repositório é um **bootstrap package**, não a aplicação final. A forma recomendada é aplicá-lo sobre um repositório de aplicação existente ou recém-criado:

```bash
python scripts/bootstrap.py --target /caminho/para/minha-aplicacao
```

O bootstrap:

1. Inicializa o Spec Kit com integração Claude.
2. Instala a extensão `assess` do Spec Kit.
3. Copia as regras, agents, skills, hooks, templates e scripts corporativos.
4. Faz merge seguro de `.claude/settings.json` e `.mcp.json`.
5. Cria a estrutura de evidências.

Depois siga `docs/01_INSTALLATION_AND_BOOTSTRAP.md`.

## Dois dados que não podem ser inventados pelo Starter Kit

O kit é funcional, mas existem dois conjuntos de valores que **precisam ser configurados pela organização/projeto**:

1. **Corporate Knowledge MCP**: URL/transporte/autenticação e nomes reais das ferramentas disponíveis.
2. **Quality commands do projeto**: comandos reais para format/lint/build/test/static analysis do stack utilizado.

O Starter Kit falha de forma segura (`fail closed`) enquanto esses itens não forem configurados.

## Arquivos principais

- `starter-overlay/CLAUDE.md` — contrato operacional do Claude.
- `starter-overlay/AGENTS.md` — instruções para Codex e outros agentes.
- `starter-overlay/.claude/agents/` — reviewers especializados.
- `starter-overlay/.claude/skills/` — comandos de workflow corporativo.
- `starter-overlay/.mcp.starter.json` — configuração MCP compartilhável.
- `starter-overlay/engineering.config.json` — configuração do workflow e quality gates.
- `starter-overlay/scripts/validate_readiness.py` — gate determinístico pré-review/final.
- `starter-overlay/scripts/run_quality.py` — execução e registro de quality commands.
- `docs/03_BUILDER_USER_MANUAL.md` — manual diário do Builder.
- `docs/05_MCP_SOURCE_OF_TRUTH.md` — desenho de Knowledge Authority.
- `TREE.txt` — árvore completa.
