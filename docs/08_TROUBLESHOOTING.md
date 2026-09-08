# 08 — Troubleshooting

## Spec Kit não aparece em `/skills`

1. Execute `specify integration status`.
2. Confirme `.claude/skills/speckit-*`.
3. Reinicie Claude Code / VS Code.
4. Se necessário: `specify integration upgrade claude`.

## Agents novos não aparecem

Se `.claude/agents/` não existia quando a sessão iniciou, reinicie a sessão. Depois alterações dentro de um diretório já observado normalmente são detectadas.

Use `/agents` ou menção explícita ao agent.

## Skill nova não aparece

Confira `.claude/skills/<skill>/SKILL.md` e reinicie se o diretório de skills foi criado após o início da sessão.

## MCP Pending approval

```bash
claude mcp list
```

Abra `claude` interativamente, confie no workspace e aprove o servidor.

## MCP não conecta

```bash
claude mcp get corporate-knowledge
```

Verifique:

- `CORPORATE_MCP_URL`;
- autenticação;
- whitespace em token/env;
- transport correto (`http` recomendado para remote MCP);
- VPN/rede corporativa.

## Hooks não executam

Dentro do Claude:

```text
/hooks
```

Debug:

```bash
claude --debug
```

ou:

```bash
claude --debug-file claude-debug.log
```

## Readiness sempre falha como stale

Execute os reviews/gates novamente **depois da última mudança de código/spec/plan/tasks**. O hook registra a última mudança relevante e o readiness gate compara timestamps: evidências anteriores à mudança são consideradas stale automaticamente. Um gate bem-sucedido limpa o estado stale.

## run_quality falha dizendo que projeto não foi configurado

Abra `engineering.config.json`, configure comandos reais e defina:

```json
"configured": true
```

## Codex review não dispara

A integração Code Review precisa estar habilitada para o repositório GitHub. Depois solicite no PR:

```text
@codex review
```
