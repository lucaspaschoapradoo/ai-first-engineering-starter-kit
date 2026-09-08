# 01 — Instalação e Bootstrap

## 1. Pré-requisitos

Padronize as estações antes do treinamento.

### Obrigatórios

- Git.
- VS Code homologado pela organização.
- Claude Code + extensão oficial para VS Code.
- Python 3.11+ acessível pelo comando `python`.
- `uv`.
- GitHub CLI (`gh`) se o time criar/consultar PRs pelo terminal.
- Acesso ao repositório Git da aplicação.
- Acesso ao Corporate Knowledge MCP.
- Acesso ao Codex Code Review no GitHub.

### Verificações

```bash
git --version
python --version
uv --version
claude --version
gh --version
```

## 2. Instalar Claude Code

### Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

Alternativa:

```powershell
winget install Anthropic.ClaudeCode
```

### macOS / Linux

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Valide:

```bash
claude --version
```

Abra o repositório no VS Code e instale a extensão oficial **Claude Code**.

## 3. Instalar Spec Kit

Recomendação corporativa: **pin de versão homologada**.

### PyPI

```bash
uv tool install specify-cli
```

### Release pinado

```bash
uv tool install specify-cli==<VERSAO_HOMOLOGADA>
```

Valide:

```bash
specify version
specify self check
```

## 4. Instalar Superpowers

A instalação é feita dentro de uma sessão Claude Code:

```text
/plugin install superpowers@claude-plugins-official
```

Se o marketplace oficial não estiver registrado:

```text
/plugin marketplace add anthropics/claude-plugins-official
/plugin install superpowers@claude-plugins-official
```

Depois, se solicitado:

```text
/reload-plugins
```

Valide no Claude Code usando `/plugins` e `/skills`.

## 5. Aplicar o Starter Kit ao projeto

No diretório deste Starter Kit:

```bash
python scripts/bootstrap.py --target /caminho/para/repo
```

Windows, exemplo:

```powershell
python .\scripts\bootstrap.py --target C:\src\supplier-portal
```

O script executará no target:

```text
specify init --here --force --non-interactive --integration claude --script py
specify extension add assess
```

Depois instalará o overlay corporativo.

### Se o Spec Kit já está instalado no projeto

```bash
python scripts/bootstrap.py --target /caminho/para/repo --skip-speckit
```

## 6. Configurar o MCP

O bootstrap cria `.mcp.json` com um servidor chamado `corporate-knowledge` usando variáveis de ambiente.

Defina:

```text
CORPORATE_MCP_URL
CORPORATE_MCP_TOKEN   # apenas se a autenticação for Bearer token
```

### Windows — sessão atual

```powershell
$env:CORPORATE_MCP_URL="https://mcp.suaempresa.com/mcp"
$env:CORPORATE_MCP_TOKEN="<TOKEN>"
```

### Windows — persistente por usuário

```powershell
[Environment]::SetEnvironmentVariable("CORPORATE_MCP_URL", "https://mcp.suaempresa.com/mcp", "User")
[Environment]::SetEnvironmentVariable("CORPORATE_MCP_TOKEN", "<TOKEN>", "User")
```

Não salve token no Git.

Se o MCP usa OAuth, remova o header Authorization de `.mcp.json` e siga o fluxo de autenticação do servidor.

Valide:

```bash
claude mcp list
claude mcp get corporate-knowledge
```

Em um repositório recém-clonado, o servidor project-scoped pode ficar `Pending approval`. Execute `claude`, confie no workspace e aprove o servidor.

Dentro da sessão:

```text
/mcp
```

O servidor precisa aparecer como conectado antes do uso do workflow.

## 7. Configurar Quality Commands

Abra:

```text
engineering.config.json
```

Troque `configured` para `true` **somente depois** de preencher os comandos reais.

Exemplo Maven + Angular (ajuste ao seu projeto):

```json
{
  "qualityCommands": [
    {"name": "backend-tests", "command": "./mvnw test", "enabled": true},
    {"name": "frontend-lint", "command": "npm run lint", "enabled": true},
    {"name": "frontend-tests", "command": "npm test -- --runInBand", "enabled": true}
  ]
}
```

Nunca copie comandos ilustrativos sem validar no projeto real.

## 8. Criar/atualizar Constitution

Inicie Claude Code no root do projeto e execute:

```text
/speckit.constitution
```

Use o prompt em:

```text
prompts/00_CONSTITUTION_PROMPT.md
```

## 9. Verificações de instalação

Execute:

```bash
python scripts/validate_starter.py
```

Depois no Claude Code:

```text
/status
/mcp
/hooks
/skills
/agents
```

Valide:

- settings do projeto carregados;
- MCP conectado;
- Spec Kit skills visíveis;
- skills corporativas visíveis;
- subagents visíveis;
- Superpowers instalado;
- hooks do projeto carregados.

## 10. Primeiro teste de fumaça

Dentro do Claude:

```text
/corporate-context cadastro de fornecedores
```

O resultado precisa:

1. Consultar o MCP.
2. Registrar fontes corporativas.
3. Não inventar convenções.
4. Criar `corporate-context.md/json` na feature quando ela existir, ou retornar contexto para uso no próximo passo.

Depois faça uma pequena feature de treinamento seguindo o manual do Builder.
