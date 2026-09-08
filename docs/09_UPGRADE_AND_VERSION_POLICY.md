# 09 — Política de atualização e versões

## Princípio

Nunca atualizar ferramentas-base simultaneamente em todos os repositórios.

## Ciclo

1. Checar release notes.
2. Atualizar repositório piloto.
3. Rodar scenario suite do Starter Kit.
4. Validar MCP, agents, skills, hooks e Spec Kit.
5. Homologar.
6. Publicar tag do Starter Kit.
7. Rollout progressivo.

## Spec Kit

Checagem:

```bash
specify self check
specify integration status
```

Upgrade de projeto:

```bash
specify integration upgrade claude
specify extension update
```

## Claude Code

Antes de elevar minimum supported version, validar:

- `.mcp.json`;
- project skills;
- subagents;
- hooks;
- VS Code extension;
- Superpowers;
- startup/trust behavior.

## Rollback

Starter Kit e configuração devem ser versionados no Git. Reverter por tag/commit, nunca editar manualmente dezenas de projetos sem rastreabilidade.
