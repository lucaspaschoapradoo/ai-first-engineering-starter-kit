# Manual completo de configuração e construção
## ai-first-engineering-starter-kit

**Versão do manual:** 1.0  
**Data-base:** 07/09/2026  
**Plataforma principal deste guia:** Windows 10/11 + PowerShell + VS Code  
**Público:** Maintainers do Starter Kit, Builders, Tech Leads e administradores da esteira AI-First  

---

# 1. Objetivo deste manual

Este documento ensina, passo a passo, como sair de um computador que já possui o VS Code instalado e chegar a um ambiente funcional com o `ai-first-engineering-starter-kit` corporativo configurado, versionado no GitHub, aplicado em um projeto piloto e validado ponta a ponta.

O guia utiliza os arquivos do pacote `corporate_ai_engineering_starter_kit_v1.zip` já construído. A intenção **não é recriar manualmente os 60+ arquivos do kit**. A intenção é:

1. preparar a estação de trabalho;
2. colocar o conteúdo do ZIP no repositório corporativo `ai-first-engineering-starter-kit`;
3. instalar e validar as ferramentas-base;
4. configurar a integração com Claude Code;
5. configurar o GitHub Spec Kit;
6. instalar Superpowers;
7. conectar o Corporate Knowledge MCP;
8. mapear as ferramentas reais do MCP;
9. entender quais arquivos são corporativos e quais são específicos de cada aplicação;
10. aplicar o Starter Kit em uma aplicação piloto;
11. configurar os quality commands reais dessa aplicação;
12. validar skills, agents, hooks, MCP e gates;
13. executar uma feature de smoke test até o estado `CODE READY`;
14. versionar e promover o Starter Kit para uso do time.

## 1.1 Resultado esperado ao final

Ao concluir este manual, o fluxo esperado para um Builder será:

```text
IDEA
  -> ASSESSMENT
  -> CORPORATE CONTEXT (MCP)
  -> SPECIFICATION
  -> CLARIFICATION
  -> PLAN
  -> MULTI-AGENT PLAN REVIEW
  -> TASKS / ANALYZE
  -> CLAUDE IMPLEMENTATION
  -> BUILDER FEEDBACK LOOPS
  -> QUALITY
  -> TEST STRATEGY REVIEW
  -> ADVERSARIAL REVIEW
  -> SPEC COMPLIANCE
  -> CORPORATE COMPLIANCE
  -> PRE-REVIEW GATE
  -> PULL REQUEST
  -> CODEX INDEPENDENT REVIEW
  -> REWORK
  -> FINAL READINESS GATE
  -> CODE READY
```

---

# 2. Como ler este manual

Para reduzir erros, cada ação é marcada pelo local onde deve acontecer.

| Marcador | Onde executar | Exemplo |
|---|---|---|
| **[POWERSHELL]** | Terminal PowerShell do Windows ou terminal integrado do VS Code configurado como PowerShell | `git --version` |
| **[CLAUDE CODE]** | Campo de conversa do Claude Code, e não no terminal | `/plugin install ...` |
| **[ARQUIVO]** | Editar um arquivo no VS Code | `engineering.config.json` |
| **[GITHUB]** | Interface web do GitHub corporativo | habilitar Code Review |
| **[VALIDAÇÃO]** | Resultado que deve ser confirmado antes de avançar | `PASS`, versão exibida etc. |

> **Regra:** quando o manual disser `[CLAUDE CODE]`, não cole o comando no PowerShell. Comandos iniciados por `/` como `/plugins`, `/agents` ou `/speckit.plan` pertencem à sessão do agente.

---

# 3. Premissas e informações que você precisa obter

Antes de começar, separe as informações abaixo. Nem todas são necessárias na primeira hora, mas todas serão necessárias antes de colocar o piloto em funcionamento.

## 3.1 GitHub corporativo

Você precisa saber:

- URL/hostname do GitHub corporativo;
- organização ou grupo onde está o Starter Kit;
- URL do repositório `ai-first-engineering-starter-kit`;
- URL de um repositório de aplicação piloto;
- método de autenticação exigido: navegador/SSO, PAT, SSH ou outro mecanismo corporativo.

Usaremos placeholders neste manual:

```text
<GITHUB_HOST>       exemplo: github.com ou github.suaempresa.com
<ORG>               organização corporativa
<STARTER_REPO_URL>  URL completa do ai-first-engineering-starter-kit
<PILOT_REPO_URL>    URL completa do projeto piloto
```

## 3.2 Corporate Knowledge MCP

Obtenha com o responsável pelo MCP:

- endpoint do servidor;
- transporte utilizado: normalmente HTTP para MCP remoto;
- método de autenticação: Bearer token, OAuth ou mecanismo corporativo;
- nomes exatos das tools expostas pelo servidor;
- quais tools equivalem funcionalmente a busca de guidance, leitura de documento, Golden Path, capability e exemplos;
- se o MCP é read-only para Builders;
- se exige VPN ou rede corporativa.

As ferramentas desejadas pelo Starter Kit são funcionalmente equivalentes a:

```text
searchGuidance
getDocument
getApplicableGuidance
getCapability
getGoldenPath
getExamples
```

Os nomes **não precisam** ser exatamente esses. Eles serão mapeados no `engineering.config.json`.

## 3.3 Aplicação piloto

Escolha uma aplicação que:

- possa ser alterada sem risco de negócio;
- tenha build e testes conhecidos;
- tenha um fluxo simples, mas real;
- utilize o stack que o time pretende suportar;
- tenha pelo menos uma pequena feature funcional que permita testar Specification -> Implement -> Review.

Evite usar o primeiro teste diretamente em um sistema crítico.

---

# 4. Entenda os dois repositórios antes de executar comandos

Existem dois papéis diferentes.

## 4.1 Repositório central do Starter Kit

```text
ai-first-engineering-starter-kit
```

Ele é o **produto de engenharia interno**. Contém:

- documentação;
- `starter-overlay/`;
- `bootstrap.py`;
- agents corporativos;
- skills corporativas;
- hooks;
- templates;
- prompts;
- scripts de readiness.

Ele **não é a aplicação do Builder**.

## 4.2 Repositório da aplicação

Exemplo:

```text
supplier-portal
```

O `bootstrap.py` aplica o conteúdo de `starter-overlay/` neste repositório e inicializa o Spec Kit.

Depois do bootstrap, a aplicação passa a conter, entre outros:

```text
CLAUDE.md
AGENTS.md
engineering.config.json
.mcp.json
.claude/
.specify/
specs/
scripts/
prompts/
.github/
.ai-engineering/
```

## 4.3 Regra importante

Não execute `specify init` no repositório central apenas porque o Spec Kit foi instalado. O `specify init` é executado **no repositório da aplicação alvo** pelo `bootstrap.py`.

---

# PARTE I - PREPARAR O WINDOWS

# 5. Abrir o terminal correto no VS Code

Como o VS Code já está instalado:

1. abra o VS Code;
2. use **Terminal > New Terminal**;
3. confirme que o prompt é PowerShell, normalmente começando por `PS`;
4. se estiver em Command Prompt, clique na seta ao lado do `+` do terminal e selecione **PowerShell**.

[POWERSHELL]

```powershell
$PSVersionTable.PSVersion
```

[VALIDAÇÃO]

O comando deve mostrar a versão do PowerShell sem erro.

## Por que isso importa

Este manual usa sintaxe PowerShell (`$env:`, `Get-Command`, `Expand-Archive`). Colar esses comandos em CMD ou Git Bash pode gerar erros que parecem problemas do Starter Kit, mas são apenas diferenças de shell.

---

# 6. Criar uma pasta de trabalho padrão

Recomendação:

[POWERSHELL]

```powershell
New-Item -ItemType Directory -Force -Path C:\src\ai-first-engineering | Out-Null
Set-Location C:\src\ai-first-engineering
Get-Location
```

[VALIDAÇÃO]

O último comando deve retornar:

```text
C:\src\ai-first-engineering
```

## Por que

Evita trabalhar em `Downloads`, OneDrive sincronizado ou diretórios com nomes complexos/espaços, reduzindo problemas com Git, scripts e ferramentas de build.

---

# 7. Verificar o VS Code

[POWERSHELL]

```powershell
code --version
```

Claude Code atualmente requer VS Code 1.98 ou superior para a extensão oficial. Se o comando `code` não estiver disponível, abra **Help > About** no VS Code e confira a versão por ali.

[VALIDAÇÃO]

- VS Code >= 1.98;
- o editor abre normalmente.

---

# 8. Instalar Git for Windows

Primeiro teste:

[POWERSHELL]

```powershell
git --version
```

Se houver versão, avance.

Se `git` não existir, prefira o catálogo corporativo. Em uma estação sem restrição, o instalador oficial pode ser obtido via WinGet:

[POWERSHELL]

```powershell
winget install --id Git.Git -e --source winget
```

Feche e reabra o terminal depois da instalação.

[POWERSHELL]

```powershell
git --version
where.exe git
```

[VALIDAÇÃO]

- uma versão do Git é exibida;
- `where.exe git` retorna um caminho válido.

## Por que instalar Git mesmo usando interface gráfica

- o Starter Kit é versionado em Git;
- Spec Kit utiliza o estado do repositório;
- Claude Code funciona melhor em projetos Git;
- o code review usa Pull Request;
- Git for Windows também disponibiliza Git Bash, recomendado pelo Claude Code em Windows nativo.

---

# 9. Configurar identidade Git

Substitua pelos dados corporativos.

[POWERSHELL]

```powershell
git config --global user.name "SEU NOME"
git config --global user.email "seu.email@empresa.com"
git config --global init.defaultBranch main
```

Valide:

```powershell
git config --global --list
```

[VALIDAÇÃO]

`user.name`, `user.email` e `init.defaultBranch` devem aparecer.

---

# 10. Verificar/instalar Python

O Starter Kit exige Python 3.11 ou superior. Ele é usado por:

- `bootstrap.py`;
- `run_quality.py`;
- `validate_readiness.py`;
- `mark-stale.py`;
- scripts Python do Spec Kit quando inicializado com `--script py`.

Teste:

[POWERSHELL]

```powershell
python --version
```

Se retornar 3.11+ você pode manter a versão homologada.

Se não houver Python, a Microsoft atualmente documenta instalação via WinGet. Em ambiente sem política corporativa específica:

```powershell
winget install Python.Python.3.14
```

Feche e reabra o terminal.

Depois:

```powershell
python --version
python -c "import sys; print(sys.executable); print(sys.version)"
```

[VALIDAÇÃO]

- versão >= 3.11;
- o executável apontado é o Python esperado.

> Se sua organização homologar Python 3.13, use essa versão. O Starter Kit não exige 3.14; exige 3.11+.

---

# 11. Instalar uv

`uv` é o gerenciador recomendado pelo Spec Kit.

Teste:

[POWERSHELL]

```powershell
uv --version
```

Se não existir:

```powershell
winget install --id astral-sh.uv -e
```

Alternativa oficial por script:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Em ambiente corporativo, prefira WinGet ou o software center para evitar execução de scripts remotos quando a política assim exigir.

Feche/reabra o terminal e valide:

```powershell
uv --version
where.exe uv
```

---

# 12. Instalar Claude Code CLI

Mesmo usando a extensão no VS Code, mantenha o CLI instalado porque ele é utilizado para:

- `claude mcp list`;
- `claude mcp get`;
- debug;
- abertura de sessões pelo terminal;
- troubleshooting;
- operações avançadas.

Teste:

[POWERSHELL]

```powershell
claude --version
```

Se não existir, opção corporativamente controlável via WinGet:

```powershell
winget install Anthropic.ClaudeCode
```

Depois, feche/reabra o terminal:

```powershell
claude --version
where.exe claude
```

[VALIDAÇÃO]

Uma versão deve aparecer sem erro.

## Canal de atualização

Para times corporativos, prefira o canal `stable` e uma política de homologação, em vez de atualizar todos no mesmo dia. Isso pode ser definido por `/config` no Claude Code ou em settings administrados pela organização.

---

# 13. Instalar a extensão Claude Code no VS Code

[VS CODE]

1. pressione `Ctrl+Shift+X`;
2. pesquise **Claude Code**;
3. selecione a extensão oficial;
4. clique **Install**;
5. se a extensão não aparecer, use `Ctrl+Shift+P` -> `Developer: Reload Window`.

Abra o painel do Claude e faça login quando solicitado.

[VALIDAÇÃO]

- painel Claude Code abre;
- você consegue iniciar uma conversa;
- a extensão reconhece o workspace atual.

---

# 14. Instalar GitHub CLI

O `gh` não é obrigatório para o código existir, mas facilita autenticação, criação de PR, consulta a PR e automações.

Teste:

[POWERSHELL]

```powershell
gh --version
```

Se não existir:

```powershell
winget install --id GitHub.cli --source winget
```

**Importante:** a documentação do GitHub informa que é necessário abrir uma nova janela de terminal após instalação para atualizar o PATH.

Valide:

```powershell
gh --version
where.exe gh
```

---

# 15. Autenticar no GitHub corporativo

## Caso A - GitHub.com / Enterprise Cloud

[POWERSHELL]

```powershell
gh auth login --hostname github.com
```

## Caso B - GitHub Enterprise Server

```powershell
gh auth login --hostname <GITHUB_HOST>
```

Siga as opções de autenticação aprovadas pela organização.

Valide:

```powershell
gh auth status
```

Se for GHES:

```powershell
gh auth status --hostname <GITHUB_HOST>
```

[VALIDAÇÃO]

A conta corporativa deve aparecer autenticada.

---

# 16. Checkpoint da estação

Execute tudo:

[POWERSHELL]

```powershell
Write-Host "=== Git ==="
git --version
Write-Host "=== Python ==="
python --version
Write-Host "=== uv ==="
uv --version
Write-Host "=== Claude ==="
claude --version
Write-Host "=== GitHub CLI ==="
gh --version
Write-Host "=== VS Code ==="
code --version
```

Não avance enquanto um componente obrigatório estiver ausente.

---

# PARTE II - CONSTRUIR O REPOSITÓRIO CORPORATIVO DO STARTER KIT

# 17. Definir variáveis de trabalho no PowerShell

Ajuste os valores.

[POWERSHELL]

```powershell
$Workspace = "C:\src\ai-first-engineering"
$StarterRepoUrl = "<STARTER_REPO_URL>"
$StarterRepo = Join-Path $Workspace "ai-first-engineering-starter-kit"
$ZipPath = "$HOME\Downloads\corporate_ai_engineering_starter_kit_v1.zip"
$ExtractDir = Join-Path $env:TEMP "ai-first-engineering-starter-extract"
```

Valide:

```powershell
$Workspace
$StarterRepoUrl
$StarterRepo
$ZipPath
$ExtractDir
```

---

# 18. Clonar o repositório corporativo

[POWERSHELL]

```powershell
Set-Location $Workspace
git clone $StarterRepoUrl
Set-Location $StarterRepo
git status
```

Se o repositório já estiver clonado:

```powershell
Set-Location $StarterRepo
git pull --ff-only
```

[VALIDAÇÃO]

`git status` deve funcionar e informar a branch atual.

---

# 19. Criar uma branch de configuração inicial

Mesmo que você seja o owner, não faça toda a configuração diretamente em `main`.

[POWERSHELL]

```powershell
git switch -c setup/starter-kit-v1
```

Se a branch já existir:

```powershell
git switch setup/starter-kit-v1
```

[VALIDAÇÃO]

```powershell
git branch --show-current
```

Deve retornar `setup/starter-kit-v1`.

---

# 20. Conferir o ZIP

[POWERSHELL]

```powershell
Test-Path $ZipPath
Get-Item $ZipPath | Select-Object FullName, Length, LastWriteTime
Get-FileHash $ZipPath -Algorithm SHA256
```

[VALIDAÇÃO]

- `Test-Path` retorna `True`;
- tamanho maior que zero;
- hash SHA256 é exibido.

Registre o hash no ticket/PR se sua governança exigir rastreabilidade do pacote importado.

---

# 21. Extrair o ZIP

Limpe qualquer extração anterior:

[POWERSHELL]

```powershell
if (Test-Path $ExtractDir) {
    Remove-Item $ExtractDir -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $ExtractDir | Out-Null
Expand-Archive -LiteralPath $ZipPath -DestinationPath $ExtractDir -Force
Get-ChildItem $ExtractDir -Force
```

O pacote possui uma pasta raiz chamada:

```text
corporate_ai_engineering_starter_kit_v1
```

Defina:

```powershell
$PackageRoot = Join-Path $ExtractDir "corporate_ai_engineering_starter_kit_v1"
Test-Path $PackageRoot
```

Deve retornar `True`.

---

# 22. Copiar o pacote para o repositório corporativo

**Por que não usar somente `Copy-Item *`?** Porque queremos garantir que itens iniciados por ponto, como `.claude` e `.github`, sejam considerados.

[POWERSHELL]

```powershell
Get-ChildItem -LiteralPath $PackageRoot -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $StarterRepo -Recurse -Force
}
```

Depois:

```powershell
Set-Location $StarterRepo
git status --short
```

[VALIDAÇÃO]

Você deve ver arquivos/pastas como:

```text
README.md
docs/
scripts/
starter-overlay/
TREE.txt
```

---

# 23. Verificar a árvore completa do pacote

No PowerShell:

```powershell
tree /F /A
```

E compare com `TREE.txt`.

A árvore esperada completa está no Apêndice A deste manual.

[VALIDAÇÃO CRÍTICA]

Confirme especialmente a existência de:

```text
starter-overlay/.claude/agents/
starter-overlay/.claude/skills/
starter-overlay/.claude/hooks/
starter-overlay/prompts/
starter-overlay/scripts/
starter-overlay/templates/evidence/
scripts/bootstrap.py
```

Se `.claude` não existir, pare. O conteúdo oculto provavelmente não foi copiado.

---

# 24. Abrir o Starter Kit no VS Code

[POWERSHELL]

```powershell
Set-Location $StarterRepo
code .
```

No Explorer do VS Code, habilite a visualização e confira `starter-overlay/.claude`.

---

# 25. Entender o que NÃO deve ser configurado como projeto final no repositório central

O repositório central é um **template/bootstrap package**.

Por isso:

- `starter-overlay/engineering.config.json` começa com `"configured": false`;
- os `qualityCommands` são placeholders;
- `.mcp.starter.json` usa variáveis de ambiente;
- o bootstrap é responsável por criar `.mcp.json` no projeto alvo;
- Spec Kit será inicializado no projeto alvo.

Não altere `configured` para `true` no template apenas para fazer a validação ficar verde. Isso destruiria o comportamento fail-closed.

---

# PARTE III - INSTALAR O GITHUB SPEC KIT

# 26. Escolher uma versão homologada

Em 07/09/2026, a release upstream mais recente consultada é **Spec Kit v1.0.4**. Em ambiente corporativo, a regra recomendada é:

1. testar uma versão em piloto;
2. homologar;
3. piná-la;
4. só então promover para o time.

Neste manual usaremos `v1.0.4` como baseline inicial, sujeito à homologação interna.

---

# 27. Instalar Spec Kit de forma pinada

[POWERSHELL]

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.0.4
```

Se uma versão já existir e você quiser substituir pela homologada:

```powershell
uv tool install --force specify-cli --from git+https://github.com/github/spec-kit.git@v1.0.4
```

Valide:

```powershell
specify version
specify self check
```

[VALIDAÇÃO]

- `specify version` retorna a versão instalada;
- `self check` roda sem quebrar a instalação.

> `self check` informa se há atualização. Ele não significa que você deve atualizar automaticamente.

---

# 28. Por que o bootstrap usa `--script py`

O comando do Starter Kit é:

```text
specify init --here --force --non-interactive --integration claude --script py
```

Isso força a instalação dos scripts Python do Spec Kit, reduzindo diferenças entre Windows e Linux e mantendo o fluxo alinhado aos scripts Python do Starter Kit.

---

# 29. Extensão `assess`

O bootstrap executa:

```text
specify extension add assess
```

Essa extensão adiciona o workflow de avaliação da ideia:

```text
intake -> research -> define -> shape -> decide
```

Ela é a camada que permite começar antes de `specify`, produzindo GO / NEEDS CLARIFICATION / KILL.

Não execute esse comando manualmente no Starter Kit central. Ele será executado no projeto piloto pelo bootstrap.

---

# PARTE IV - ENTENDER E CONFIGURAR O CONTEÚDO DO STARTER KIT

# 30. Mapa dos arquivos principais

| Arquivo/pasta | Papel | Editar agora? |
|---|---|---|
| `README.md` | apresentação do produto | opcional |
| `docs/` | documentação operacional | revisar/personalizar |
| `scripts/bootstrap.py` | aplica o overlay em aplicações | não alterar sem teste |
| `starter-overlay/CLAUDE.md` | contrato operacional do Claude | revisar, manter princípios |
| `starter-overlay/AGENTS.md` | instruções para reviewer independente/Codex | revisar |
| `starter-overlay/engineering.config.json` | contrato de workflow, MCP e quality gates | **sim: mapear MCP corporativo; quality fica por projeto** |
| `starter-overlay/.mcp.starter.json` | template do MCP compartilhável | **sim: confirmar transporte/autenticação** |
| `starter-overlay/.claude/settings.starter.json` | permissions + hooks | revisar com segurança |
| `starter-overlay/.claude/agents/` | 8 reviewers/classificadores | usar baseline |
| `starter-overlay/.claude/skills/` | comandos corporativos | usar baseline |
| `starter-overlay/prompts/` | prompts de referência | usar baseline |
| `starter-overlay/scripts/` | gates executáveis | usar baseline |
| `starter-overlay/templates/evidence/` | exemplos de evidência | usar baseline |
| `starter-overlay/.github/pull_request_template.md` | PR padrão | adaptar nomenclatura corporativa se necessário |

---

# 31. Revisar `CLAUDE.md`

[ARQUIVO]

Abra:

```text
starter-overlay/CLAUDE.md
```

Ele define:

- missão do Claude;
- hierarquia de fontes;
- obrigatoriedade do MCP;
- fluxo completo;
- Plan before Code;
- Reuse before Build;
- Change Impact Router;
- Implementation Loop;
- Evidence over Claims;
- independência de review;
- bloqueio de `CODE READY` sem gate determinístico;
- proteção de secrets.

## O que você pode personalizar

- nomenclaturas internas;
- regras adicionais realmente corporativas;
- políticas de escalonamento;
- restrições adicionais.

## O que não deve remover

- MCP como autoridade;
- Evidence over Claims;
- Review independente;
- regra de readiness;
- proteção de secrets;
- Change Impact Router.

---

# 32. Revisar `AGENTS.md`

[ARQUIVO]

```text
starter-overlay/AGENTS.md
```

Esse arquivo orienta o reviewer independente. Ele determina que o review priorize:

1. correctness/regression;
2. security/authorization;
3. data integrity;
4. testes comportamentais faltantes;
5. error handling;
6. arquitetura/complexidade;
7. performance material;
8. manutenibilidade.

Ele também impede que Codex considere a evidência do Claude como prova absoluta.

---

# 33. Revisar os 8 subagents

Diretório:

```text
starter-overlay/.claude/agents/
```

| Agent | Função |
|---|---|
| `architecture-reviewer` | arquitetura, boundaries, acoplamento, padrões MCP |
| `security-reviewer` | autenticação, autorização, dados, trust boundaries |
| `test-strategy-reviewer` | gaps de testes e cobertura comportamental |
| `simplicity-reviewer` | evitar overengineering e duplicação |
| `adversarial-reviewer` | tentar quebrar a implementação |
| `spec-compliance-reviewer` | requisito vs código vs teste |
| `corporate-compliance-reviewer` | padrão corporativo vs implementação |
| `change-impact-classifier` | classificar LOCAL/BEHAVIORAL/STRUCTURAL |

Claude Code descobre subagents de projeto em `.claude/agents/`. Eles devem ser versionados para que o time use o mesmo comportamento.

---

# 34. Revisar as 11 skills

Diretório:

```text
starter-overlay/.claude/skills/
```

Skills são procedimentos reutilizáveis e podem ser chamados pelo Builder com `/nome-da-skill`.

| Skill | Objetivo |
|---|---|
| `/corporate-context` | buscar contexto obrigatório no MCP |
| `/plan-review` | disparar revisão multi-agent do plano |
| `/change-request` | classificar e aplicar ajuste com minimum safe rewind |
| `/run-quality` | executar quality commands determinísticos |
| `/test-strategy-review` | revisar estratégia de testes |
| `/adversarial-review` | tentar encontrar defeitos concretos |
| `/spec-compliance` | comprovar aderência à spec |
| `/corporate-compliance` | comprovar aderência ao MCP |
| `/pre-review-gate` | validar readiness antes do PR |
| `/post-review-rework` | processar findings do reviewer independente |
| `/code-ready` | executar o gate final |

Não copie essas instruções manualmente para cada chat. Elas existem justamente para evitar prompts ad hoc.

---

# 35. Revisar settings e hook de stale evidence

[ARQUIVO]

```text
starter-overlay/.claude/settings.starter.json
```

O arquivo possui dois objetivos.

## 35.1 Proteção de secrets

Bloqueia leitura normal de:

```text
.env
.env.*
*credential*
*private_key*
```

## 35.2 Hook após Write/Edit

Após Claude editar/escrever, é executado:

```text
python ${CLAUDE_PROJECT_DIR}/.claude/hooks/mark-stale.py
```

O objetivo é marcar evidências antigas como potencialmente obsoletas. Assim, um teste feito **antes** da última mudança não pode ser reutilizado como se provasse a versão atual.

Claude Code oferece `/hooks` para inspecionar hooks carregados.

---

# 36. Configurar o Corporate Knowledge MCP

Este é um dos pontos mais importantes do setup.

[ARQUIVO]

Abra:

```text
starter-overlay/.mcp.starter.json
```

Baseline atual:

```json
{
  "mcpServers": {
    "corporate-knowledge": {
      "type": "http",
      "url": "${CORPORATE_MCP_URL:-}",
      "headers": {
        "Authorization": "Bearer ${CORPORATE_MCP_TOKEN:-}"
      }
    }
  }
}
```

Claude Code suporta configuração MCP project-scoped em `.mcp.json` e expansão de variáveis `${VAR}` ou `${VAR:-default}` em URL e headers.

## 36.1 Se seu MCP usa HTTP + Bearer

Mantenha o modelo e use variáveis de ambiente.

## 36.2 Se usa OAuth

Não coloque Bearer token fixo. Ajuste o template conforme o servidor e autentique via `/mcp`.

## 36.3 Se o endpoint possui caminho fixo

Você pode manter a URL inteira em variável ou usar:

```json
"url": "${CORPORATE_MCP_BASE_URL}/mcp"
```

## 36.4 Não fazer

Nunca:

```json
"Authorization": "Bearer TOKEN_REAL_AQUI"
```

em arquivo versionado.

---

# 37. Mapear os nomes reais das tools MCP

[ARQUIVO]

Abra:

```text
starter-overlay/engineering.config.json
```

A seção começa com placeholders:

```json
"toolMapping": {
  "searchGuidance": "__MAP_TO_REAL_MCP_TOOL__",
  "getDocument": "__MAP_TO_REAL_MCP_TOOL__",
  "getApplicableGuidance": "__MAP_TO_REAL_MCP_TOOL__",
  "getCapability": "__MAP_TO_REAL_MCP_TOOL__",
  "getGoldenPath": "__MAP_TO_REAL_MCP_TOOL__",
  "getExamples": "__MAP_TO_REAL_MCP_TOOL__"
}
```

## Como descobrir os nomes

No projeto piloto, depois do MCP conectado:

[CLAUDE CODE]

```text
/mcp
```

Verifique o servidor e as tools. Você também pode pedir ao Claude:

```text
Liste as tools disponíveis no servidor MCP corporate-knowledge, com nome exato e descrição. Não execute ações; apenas apresente o catálogo de tools que você consegue utilizar.
```

Mapeie por função.

Exemplo hipotético:

```json
"toolMapping": {
  "searchGuidance": "search_docs",
  "getDocument": "get_document_by_id",
  "getApplicableGuidance": "find_applicable_standards",
  "getCapability": "get_capability",
  "getGoldenPath": "get_golden_path",
  "getExamples": "search_approved_examples"
}
```

Os nomes acima são **exemplos**, não use sem confirmar o MCP real.

## O que deve ser corporativo no template

Como o MCP é o mesmo para toda a organização, depois de confirmar os nomes reais, é recomendável atualizar o `starter-overlay/engineering.config.json` central com o mapeamento verdadeiro. Assim, novos projetos já nascem mapeados.

---

# 38. Quality commands: central x projeto

A seção `qualityCommands` contém placeholders e `enabled:false`.

Esses comandos normalmente dependem do repositório da aplicação.

Portanto:

- no Starter Kit central, deixe-os desabilitados se existirem stacks diferentes;
- no projeto piloto, configure comandos reais;
- só marque `"configured": true` no projeto alvo depois de configurar MCP mapping e quality commands necessários.

Se toda a empresa usa um blueprint absolutamente único, no futuro pode existir um perfil padronizado por stack. Não faça isso antes de validar.

---

# 39. Revisar prompts de referência

Diretório:

```text
starter-overlay/prompts/
```

Eles não substituem skills. São exemplos canônicos para:

- constitution;
- início da feature;
- plan review;
- implementação;
- change requests;
- Codex review;
- rework.

Os prompts completos estão no Apêndice C.

---

# 40. Revisar scripts determinísticos

Diretório:

```text
starter-overlay/scripts/
```

## `run_quality.py`

- exige `engineering.config.json` configurado;
- executa cada quality command habilitado;
- registra exit code/stdout/stderr;
- grava `quality-run.json`.

## `validate_readiness.py`

Valida:

- config;
- MCP mapping;
- spec/plan/tasks;
- evidências pré-review;
- PASS dos gates;
- MCP connection no compliance;
- stale evidence;
- independent review no final;
- Critical/High;
- tratamento de Medium.

## `validate_starter.py`

Confirma a presença dos arquivos básicos. Antes da configuração do projeto é normal retornar `ATTENTION` por `configured=false`.

---

# 41. Commit do baseline importado

Antes de personalizar, faça um commit de importação do pacote original. Isso facilita comparar suas customizações.

[POWERSHELL]

```powershell
Set-Location $StarterRepo
git add .
git status
git commit -m "chore: import AI-first engineering starter kit v1 baseline"
```

Depois:

```powershell
git log -1 --oneline
```

---

# 42. Commit das customizações corporativas

Depois de revisar MCP template, tool mapping, nomenclaturas e documentação:

[POWERSHELL]

```powershell
git add .
git diff --cached
git commit -m "feat: configure corporate AI engineering starter kit"
```

Envie branch:

```powershell
git push -u origin setup/starter-kit-v1
```

Crie PR:

```powershell
gh pr create --title "Configure AI-first engineering starter kit v1" --body "Initial corporate configuration of MCP contract, governed workflow, agents, skills, hooks and bootstrap package."
```

Se `gh pr create` não estiver adequado ao GitHub corporativo, abra o PR pela interface web.

---

# PARTE V - INSTALAR SUPERPOWERS

# 43. Abrir Claude Code

No VS Code com o Starter Kit ou projeto piloto aberto, abra o painel Claude Code.

Você também pode iniciar pelo terminal:

[POWERSHELL]

```powershell
claude
```

---

# 44. Instalar Superpowers

**Este comando é no Claude Code, não no PowerShell.**

[CLAUDE CODE]

```text
/plugin install superpowers@claude-plugins-official
```

Se necessário, consulte:

```text
/plugins
```

[VALIDAÇÃO]

Superpowers deve aparecer entre os plugins instalados.

## Por que

O Spec Kit organiza artefatos e workflow. Superpowers adiciona práticas de execução, TDD, debugging e disciplina agentic. O Starter Kit não depende de reimplementar essas práticas em prompts enormes.

---

# PARTE VI - APLICAR O KIT EM UMA APLICAÇÃO PILOTO

# 45. Clonar o projeto piloto

[POWERSHELL]

```powershell
Set-Location $Workspace
git clone <PILOT_REPO_URL>
Set-Location .\<NOME_DO_REPO_PILOTO>
git status
```

Crie branch:

```powershell
git switch -c pilot/ai-first-starter-kit
```

**Nunca rode o primeiro bootstrap diretamente em uma branch produtiva.**

---

# 46. Rodar o bootstrap

A partir do repositório central do Starter Kit:

[POWERSHELL]

```powershell
Set-Location $StarterRepo
python .\scripts\bootstrap.py --target C:\src\ai-first-engineering\<NOME_DO_REPO_PILOTO>
```

O script irá, no target:

```text
1. validar que `specify` existe;
2. executar Spec Kit init com integração Claude;
3. instalar extensão assess;
4. copiar CLAUDE.md / AGENTS.md / engineering.config.json;
5. fazer merge de .claude/settings.json;
6. fazer merge de .mcp.json;
7. copiar agents;
8. copiar skills;
9. copiar hooks;
10. copiar scripts;
11. copiar templates;
12. copiar prompts;
13. copiar PR template;
14. copiar .ai-engineering;
15. atualizar .gitignore;
16. criar .ai-engineering/local/.
```

[VALIDAÇÃO]

Ao final deve aparecer:

```text
BOOTSTRAP COMPLETE
```

seguido dos próximos passos.

---

# 47. Entender as opções do bootstrap

## `--skip-speckit`

Use somente se o Spec Kit já estiver corretamente inicializado no projeto:

```powershell
python .\scripts\bootstrap.py --target C:\src\pilot --skip-speckit
```

## `--overwrite`

Sobrescreve arquivos corporativos existentes.

```powershell
python .\scripts\bootstrap.py --target C:\src\pilot --overwrite
```

**Não use no primeiro reflexo.** O bootstrap padrão preserva vários arquivos existentes para reduzir risco.

## Tratamento especial de `CLAUDE.md`

Se já existir, o bootstrap procura o marcador:

```text
# Corporate AI Engineering Rules
```

Se o marcador não existir, ele anexa as regras corporativas ao `CLAUDE.md` existente.

---

# 48. Verificar o que mudou no piloto

[POWERSHELL]

```powershell
Set-Location C:\src\ai-first-engineering\<NOME_DO_REPO_PILOTO>
git status --short
```

Depois:

```powershell
tree /F /A
```

Confirme:

```text
.claude/agents/
.claude/skills/
.claude/hooks/
.claude/settings.json
.mcp.json
.specify/
CLAUDE.md
AGENTS.md
engineering.config.json
scripts/
prompts/
.github/pull_request_template.md
.ai-engineering/
```

---

# PARTE VII - CONFIGURAR O PILOTO

# 49. Configurar variáveis de ambiente do MCP na sessão atual

Se Bearer token:

[POWERSHELL]

```powershell
$env:CORPORATE_MCP_URL = "https://SEU-ENDPOINT-MCP/mcp"
$env:CORPORATE_MCP_TOKEN = "SEU_TOKEN_TEMPORARIO"
```

Valide sem imprimir o token:

```powershell
$env:CORPORATE_MCP_URL
if ($env:CORPORATE_MCP_TOKEN) { "TOKEN_PRESENT" } else { "TOKEN_MISSING" }
```

Nunca execute `Write-Host $env:CORPORATE_MCP_TOKEN` em gravações, screenshots ou logs compartilhados.

## Persistência por usuário - somente se aprovado

```powershell
[Environment]::SetEnvironmentVariable("CORPORATE_MCP_URL", "https://SEU-ENDPOINT-MCP/mcp", "User")
[Environment]::SetEnvironmentVariable("CORPORATE_MCP_TOKEN", "SEU_TOKEN", "User")
```

Depois abra nova janela do VS Code/terminal.

Se a organização possui secret manager/SSO/OAuth, prefira esse mecanismo em vez de persistir token em variável de usuário.

---

# 50. Validar `.mcp.json`

[ARQUIVO]

Abra o `.mcp.json` do projeto piloto.

Ele deve conter o servidor `corporate-knowledge`.

Valide sintaxe JSON:

[POWERSHELL]

```powershell
Get-Content .\.mcp.json -Raw | ConvertFrom-Json | Out-Null
"MCP_JSON_OK"
```

[VALIDAÇÃO]

Deve exibir `MCP_JSON_OK`.

---

# 51. Validar conexão MCP via CLI

[POWERSHELL]

```powershell
claude mcp list
claude mcp get corporate-knowledge
```

Na primeira utilização de `.mcp.json` project-scoped, Claude Code pode solicitar aprovação do servidor por segurança.

Abra Claude no root do projeto:

```powershell
claude
```

[CLAUDE CODE]

```text
/mcp
```

Aprove/confie no servidor project-scoped quando o fluxo corporativo permitir.

[VALIDAÇÃO]

- servidor `corporate-knowledge` conectado;
- tools disponíveis;
- sem erro de variável ausente;
- sem endpoint incorreto.

---

# 52. Mapear MCP tools no `engineering.config.json` do piloto

Se o Starter Kit central já recebeu o mapeamento real, confira apenas se está correto.

Caso contrário, edite no piloto.

[ARQUIVO]

```text
engineering.config.json
```

Troque todos os:

```text
__MAP_TO_REAL_MCP_TOOL__
```

por nomes reais.

[POWERSHELL]

Procure placeholders restantes:

```powershell
Select-String -Path .\engineering.config.json -Pattern "__MAP_"
```

[VALIDAÇÃO]

Quando mapeado, o comando não deve retornar linhas.

---

# 53. Configurar os quality commands reais

Este é um gate determinístico. Não use comandos ilustrativos sem executar manualmente antes.

Primeiro, descubra os comandos oficiais do projeto.

Exemplos possíveis:

### Maven/Java no Windows

```powershell
.\mvnw.cmd test
.\mvnw.cmd verify
```

### Gradle

```powershell
.\gradlew.bat test
.\gradlew.bat build
```

### Angular/Node

```powershell
npm ci
npm run lint
npm test -- --watch=false
npm run build
```

**Use somente os comandos que o projeto realmente possui.**

## 53.1 Testar cada comando manualmente

Exemplo:

```powershell
npm run lint
$LASTEXITCODE
```

O exit code deve ser `0` para sucesso.

## 53.2 Editar `engineering.config.json`

Exemplo ilustrativo:

```json
"qualityCommands": [
  {
    "name": "frontend-lint",
    "command": "npm run lint",
    "enabled": true
  },
  {
    "name": "frontend-tests",
    "command": "npm test -- --watch=false",
    "enabled": true
  },
  {
    "name": "frontend-build",
    "command": "npm run build",
    "enabled": true
  }
]
```

**Atenção Windows:** `run_quality.py` usa `shell=True`. Os comandos precisam ser válidos no shell do Windows. Para wrappers Maven/Gradle, prefira `.cmd`/`.bat` se necessário.

Depois de MCP mapping e quality commands:

```json
"configured": true
```

---

# 54. Validar `engineering.config.json`

[POWERSHELL]

```powershell
Get-Content .\engineering.config.json -Raw | ConvertFrom-Json | Out-Null
"ENGINEERING_CONFIG_JSON_OK"
```

Procure placeholders:

```powershell
Select-String -Path .\engineering.config.json -Pattern "__CONFIGURE|__MAP_"
```

[VALIDAÇÃO]

- JSON válido;
- nenhuma tool obrigatória ainda com placeholder;
- nenhum quality command habilitado apontando para placeholder;
- `configured=true` apenas quando real.

---

# 55. Criar a Constitution do projeto

Abra Claude no root do projeto piloto.

[CLAUDE CODE]

```text
/speckit.constitution
```

Cole o conteúdo de:

```text
prompts/00_CONSTITUTION_PROMPT.md
```

O objetivo é registrar no mecanismo do Spec Kit os princípios não negociáveis do projeto.

[VALIDAÇÃO]

Confirme que a constitution gerada contempla:

- specification before implementation;
- MCP authority;
- no invented corporate conventions;
- reuse before build;
- explicit clarification;
- plan before code;
- change impact router;
- behavior-based testing;
- Critical/High blockers;
- independent reviewer;
- evidence over claims;
- compliance revalidation;
- no CODE READY without deterministic gate;
- secrets protection.

---

# 56. Rodar validação estrutural

[POWERSHELL]

```powershell
python .\scripts\validate_starter.py
```

## Resultado possível A

```text
STARTER VALIDATION: PASS
```

Ótimo.

## Resultado possível B

```text
STARTER VALIDATION: ATTENTION
- engineering.config.json configured=false ...
```

Isso é esperado **antes** de concluir a configuração. Depois de configurado, repita até PASS.

---

# PARTE VIII - VALIDAR CLAUDE CODE, SKILLS, AGENTS E HOOKS

# 57. Reiniciar sessão depois da primeira criação de diretórios

Claude Code detecta mudanças em skills/agents, mas se `.claude/skills` ou `.claude/agents` **não existiam quando a sessão começou**, reiniciar a sessão é a forma mais segura.

Feche a conversa ou recarregue a janela do VS Code depois do bootstrap.

---

# 58. Checklist dentro do Claude Code

[CLAUDE CODE]

Execute, um por vez:

```text
/status
/mcp
/hooks
/skills
/agents
/plugins
```

## O que validar

### `/mcp`

- `corporate-knowledge` conectado;
- tools listadas;
- sem pending approval.

### `/hooks`

- hook de projeto `PostToolUse`;
- matcher `Write|Edit`;
- comando `mark-stale.py`.

### `/skills`

Deve incluir as skills corporativas e as skills Spec Kit.

Procure ao menos:

```text
corporate-context
plan-review
change-request
run-quality
test-strategy-review
adversarial-review
spec-compliance
corporate-compliance
pre-review-gate
post-review-rework
code-ready
```

E Spec Kit:

```text
speckit.specify
speckit.clarify
speckit.plan
speckit.tasks
speckit.analyze
speckit.implement
speckit.converge
speckit.constitution
```

### `/agents`

Procure os 8 agents corporativos.

### `/plugins`

Superpowers deve aparecer instalado.

---

# 59. Smoke test do MCP antes de desenvolver

[CLAUDE CODE]

```text
/corporate-context cadastro de fornecedores
```

Peça explicitamente:

```text
Use obrigatoriamente o servidor corporate-knowledge. Identifique Golden Path, standards APPROVED, capabilities reutilizáveis, restrições de arquitetura, segurança, dados, UX, integração e testes. Informe IDs/versões/status quando o MCP fornecer. Não invente convenções ausentes.
```

[VALIDAÇÃO]

O resultado deve mostrar evidência de consulta ao MCP. Se Claude responder apenas com best practices genéricas, não avance. Corrija a conexão/tool mapping/instrução.

---

# PARTE IX - EXECUTAR A PRIMEIRA FEATURE DE TREINAMENTO

# 60. Etapa 1 - Assessment

Para uma ideia relevante, use o fluxo `assess`.

[CLAUDE CODE]

```text
/speckit-assess-intake "Permitir que fornecedores autenticados atualizem seus dados de contato" slug=supplier-self-update
```

Depois:

```text
/speckit-assess-research slug=supplier-self-update
/speckit-assess-define slug=supplier-self-update
/speckit-assess-shape slug=supplier-self-update
/speckit-assess-decide slug=supplier-self-update
```

[VALIDAÇÃO]

Saída final:

```text
GO
```

ou justificativa para `NEEDS CLARIFICATION` / `KILL`.

Para pequenos ajustes previamente aprovados, a política do time pode permitir pular Assessment, mas isso deve ser uma regra explícita, não improvisada.

---

# 61. Etapa 2 - Corporate Context

[CLAUDE CODE]

```text
/corporate-context
Precisamos permitir que um fornecedor autenticado atualize telefone, e-mail e endereço. CNPJ deve permanecer imutável e todas as mudanças precisam de auditabilidade.
```

Confirme referências corporativas.

---

# 62. Etapa 3 - Specification

[CLAUDE CODE]

```text
/speckit.specify
Permitir que um fornecedor autenticado atualize telefone, e-mail e endereço. CNPJ não pode ser alterado após onboarding. Toda mudança aceita precisa ser auditável. Se a atualização falhar, nenhuma alteração parcial pode ser persistida.
```

A Specification deve responder WHAT/WHY e incorporar constraints mandatórios do contexto corporativo sem virar um plano técnico detalhado.

---

# 63. Etapa 4 - Clarification

[CLAUDE CODE]

```text
/speckit.clarify
```

Ordem esperada do Claude:

```text
spec/repo -> MCP -> Builder
```

Ele deve consultar o MCP antes de interromper o Builder sobre uma regra que já está documentada corporativamente.

Repita até não haver ambiguidade material.

---

# 64. Etapa 5 - Checklist da Specification

[CLAUDE CODE]

```text
/speckit.checklist
```

Valide se a spec cobre:

- requisitos;
- acceptance criteria;
- erros;
- edge cases relevantes;
- NFRs;
- out-of-scope;
- constraints corporativos aplicáveis.

---

# 65. Etapa 6 - Plan

Se possível, coloque Claude em Plan Mode.

[CLAUDE CODE]

```text
/speckit.plan
```

O plano deve aplicar `Reuse before Build` e referenciar MCP quando aplicável.

---

# 66. Etapa 7 - Multi-Agent Plan Review

[CLAUDE CODE]

```text
/plan-review
```

O Starter Kit dispara revisão independente com:

- architecture;
- security;
- test strategy;
- simplicity.

[VALIDAÇÃO]

Não avançar com:

```text
Critical > 0
High > 0
```

Se houver finding, atualize o plan e repita a revisão.

---

# 67. Etapa 8 - Tasks e Analyze

[CLAUDE CODE]

```text
/speckit.tasks
/speckit.analyze
```

Não implemente se `analyze` encontrar inconsistência material entre Spec, Plan e Tasks.

---

# 68. Etapa 9 - Implement

[CLAUDE CODE]

```text
/speckit.implement
```

O comportamento esperado é:

```text
Inspect
-> retrieve relevant MCP context
-> implement one coherent task
-> build/test
-> self-review
-> fix
-> prove task criteria
-> next task
```

Superpowers deve ser usado pelo Claude quando útil para TDD, debugging e execução disciplinada.

---

# 69. Testar feedback do Builder durante implementação

## 69.1 Mudança local

[CLAUDE CODE]

```text
/change-request
Não gostei do layout. Reduza o espaço vertical, agrupe os dados principais em cards e mova as ações para o canto superior direito, respeitando o Design System aprovado.
```

Esperado:

```text
LOCAL
-> alterar
-> verificar
-> preview
```

Sem reiniciar a esteira completa.

## 69.2 Mudança comportamental

```text
/change-request
A regra está errada: CNPJ deve ser imutável depois do primeiro cadastro.
```

Esperado:

- comparar com spec;
- se já existia, corrigir código/testes;
- se é nova, atualizar spec e revalidar impacto.

## 69.3 Mudança estrutural

```text
/change-request
Depois de salvar o fornecedor, publique o evento corporativo aprovado consumido pelo Sistema X.
```

Esperado:

```text
STRUCTURAL
-> MCP
-> spec se necessário
-> plan update
-> relevant reviews
-> tasks update
-> implement
```

---

# 70. Etapa 10 - Run Quality

Primeiro no PowerShell, para ter saída explícita:

[POWERSHELL]

```powershell
python .\scripts\run_quality.py
```

Ou no Claude:

[CLAUDE CODE]

```text
/run-quality
```

[VALIDAÇÃO]

- todos os comandos habilitados retornam exit code 0;
- `quality-run.json` é criado no diretório `evidence` da feature.

---

# 71. Etapa 11 - Test Strategy Review

[CLAUDE CODE]

```text
/test-strategy-review
```

O reviewer deve verificar comportamento, não só percentual de cobertura.

Se houver gaps:

```text
finding -> tests/fix -> run quality -> review novamente
```

---

# 72. Etapa 12 - Adversarial Review

[CLAUDE CODE]

```text
/adversarial-review
```

O reviewer assume que há defeitos e tenta encontrar cenário concreto de quebra.

[VALIDAÇÃO]

Pré-review não aceita Critical ou High abertos.

---

# 73. Etapa 13 - Converge

[CLAUDE CODE]

```text
/speckit.converge
```

Se o Spec Kit adicionar trabalho restante, implemente e rode `converge` novamente.

---

# 74. Etapa 14 - Spec Compliance

[CLAUDE CODE]

```text
/spec-compliance
```

Esperado: requisito x implementação x testes x evidência.

---

# 75. Etapa 15 - Corporate Compliance

[CLAUDE CODE]

```text
/corporate-compliance
```

Essa etapa deve **reconsultar o MCP**, não confiar apenas no corporate-context antigo.

A evidência precisa registrar, quando disponível:

- MCP conectado;
- standards;
- IDs;
- versões;
- status APPROVED;
- capabilities usadas;
- exceptions/conflicts;
- rationale se nenhum standard for aplicável.

---

# 76. Etapa 16 - Pre-review Gate

[POWERSHELL]

```powershell
python .\scripts\validate_readiness.py --phase pre-review
```

Ou:

[CLAUDE CODE]

```text
/pre-review-gate
```

[VALIDAÇÃO]

Deve retornar:

```text
READINESS (pre-review): PASS
READY FOR REVIEW
```

Se retornar FAIL, corrija **cada blocker**. Não crie PR para contornar o gate.

---

# PARTE X - PULL REQUEST E CODEX

# 77. Preparar commit do piloto

[POWERSHELL]

```powershell
git status
git add .
git diff --cached
git commit -m "feat: pilot AI-first supplier self-update workflow"
git push -u origin pilot/ai-first-starter-kit
```

---

# 78. Criar Pull Request

O bootstrap instala:

```text
.github/pull_request_template.md
```

Crie o PR pela interface web ou GitHub CLI.

[POWERSHELL]

```powershell
gh pr create --fill
```

Revise o PR e preencha:

- Intent;
- paths de Spec/Plan/Tasks;
- corporate guidance;
- capabilities reutilizadas;
- verification evidence;
- risks/exceptions.

---

# 79. Habilitar Codex Code Review no repositório

[GITHUB / ADMIN]

O repositório precisa ter o Code Review do Codex habilitado conforme as permissões do workspace/organização.

A OpenAI documenta que, após habilitado, o Codex pode revisar PRs automaticamente quando saem de Draft ou por menção explícita.

No PR:

```text
@codex review
```

Ou com foco adicional:

```text
@codex review for correctness, regressions, security, missing tests and maintainability. Treat the PR intent and engineering evidence as context, but review the code independently.
```

---

# 80. Registrar o resultado do review independente

O Starter Kit espera:

```text
evidence/independent-review.json
```

Use o template de exemplo existente em:

```text
templates/evidence/independent-review.example.json
```

A evidência final precisa refletir o estado **real** do review: PASS/RESOLVED e findings abertos.

---

# 81. Rework pós-review

[CLAUDE CODE]

```text
/post-review-rework
```

Para cada finding, Claude deve classificar:

```text
VALID
PARTIALLY_VALID
INVALID
```

Não aceite todo comentário cegamente.

Finding válido:

```text
investigate -> reproduce -> fix -> tests -> affected compliance -> re-review
```

Depois de mudanças, o hook marca evidências potencialmente stale. Rode novamente os gates afetados.

---

# 82. Final readiness

[POWERSHELL]

```powershell
python .\scripts\validate_readiness.py --phase final
```

Ou:

[CLAUDE CODE]

```text
/code-ready
```

[VALIDAÇÃO FINAL]

O único resultado aceito é:

```text
READINESS (final): PASS
CODE READY
```

Não use a expressão `CODE READY` se o script não passou.

---

# PARTE XI - PROMOVER O STARTER KIT

# 83. O que considerar um piloto aprovado

O piloto deve demonstrar:

- Builder operando prioritariamente por linguagem natural;
- MCP consultado como fonte de verdade;
- Spec Kit funcional;
- agents funcionalmente independentes;
- feedback local sem reiniciar tudo;
- mudança estrutural com rewind controlado;
- quality commands determinísticos;
- stale evidence funcionando;
- pre-review PASS;
- Codex independente;
- final readiness PASS.

---

# 84. Atualizar o Starter Kit com aprendizados do piloto

Faça ajustes **no repositório central**, não manualmente apenas no piloto.

Exemplos:

- tool mapping MCP confirmado;
- correção de agent prompt;
- nova policy de permission;
- melhoria do skill;
- documentação;
- script bugfix.

Depois aplique novamente em outro piloto.

---

# 85. Versionar o Starter Kit

Após aprovação:

[POWERSHELL]

```powershell
Set-Location $StarterRepo
git switch main
git pull --ff-only
```

Depois que o PR estiver mergeado, crie tag conforme política:

```powershell
git tag -a v1.0.0 -m "AI-first engineering starter kit v1.0.0"
git push origin v1.0.0
```

Se o repositório já usa outro versionamento, respeite a política existente.

---

# 86. Política de atualização

Não atualizar simultaneamente:

- Claude Code;
- Spec Kit;
- Superpowers;
- prompts/agents/hooks;
- MCP contract;

em todos os projetos.

Fluxo recomendado:

```text
release note
-> starter-kit test branch
-> pilot repo
-> smoke suite
-> homologation
-> starter-kit tag
-> progressive rollout
```

---

# PARTE XII - TROUBLESHOOTING

# 87. `git` não reconhecido

1. feche todas as janelas de terminal;
2. abra nova janela;
3. rode `where.exe git`;
4. se não existir, reinstale Git for Windows.

---

# 88. `python` abre Microsoft Store ou não é encontrado

Use:

```powershell
where.exe python
py --version
```

Confirme App Execution Aliases do Windows se necessário e mantenha apenas o Python homologado no PATH.

---

# 89. `uv` não reconhecido

Feche/reabra o terminal depois da instalação.

```powershell
where.exe uv
```

Se usou standalone installer, o binário pode estar em `.local\bin` do usuário.

---

# 90. `specify` não reconhecido

```powershell
uv tool list
specify version
```

Se necessário, reinstale a versão pinada.

---

# 91. Spec Kit skills não aparecem

No projeto piloto:

```powershell
specify integration status
```

Confirme estrutura `.claude/skills/speckit-*`.

Se necessário, em ambiente piloto:

```powershell
specify integration upgrade claude
```

Reinicie Claude/VS Code.

---

# 92. MCP Pending Approval

```powershell
claude mcp list
```

Abra sessão interativa no projeto:

```powershell
claude
```

Depois:

```text
/mcp
```

Aprove o servidor project-scoped.

---

# 93. MCP não conecta

Verifique:

```powershell
$env:CORPORATE_MCP_URL
if ($env:CORPORATE_MCP_TOKEN) { "TOKEN_PRESENT" } else { "TOKEN_MISSING" }
claude mcp get corporate-knowledge
```

Cheque:

- VPN;
- DNS/proxy;
- URL;
- transporte;
- autenticação;
- whitespace em token;
- OAuth pendente;
- certificados corporativos.

---

# 94. Agents/skills não aparecem

Confirme:

```text
.claude/agents/
.claude/skills/
```

Se esses diretórios foram criados depois da sessão começar, reinicie Claude Code.

Use:

```text
/agents
/skills
```

---

# 95. Hooks não aparecem

[CLAUDE CODE]

```text
/hooks
```

No terminal:

```powershell
claude --debug
```

ou:

```powershell
claude --debug-file claude-debug.log
```

Confirme sintaxe de `.claude/settings.json`.

---

# 96. `validate_starter.py` retorna ATTENTION

Leia cada linha. Se o único motivo for:

```text
engineering.config.json configured=false
```

configure o projeto e repita.

Não altere para `true` apenas para remover o alerta.

---

# 97. `run_quality.py` bloqueia

Causas comuns:

- `configured=false`;
- nenhum command habilitado;
- placeholder ainda presente;
- comando não funciona no shell Windows;
- dependência do projeto não instalada.

Execute o comando manualmente antes de culpar o script.

---

# 98. Readiness falha por stale evidence

Isso significa que houve alteração relevante depois de uma evidência.

Solução correta:

1. reexecute quality;
2. repita reviews afetados;
3. repita compliance;
4. regenere evidências;
5. rode readiness novamente.

Não edite timestamp para burlar o mecanismo.

---

# 99. Codex review não dispara

Verifique:

- Code Review habilitado para o repo;
- permissões do workspace;
- integração GitHub instalada/permitida;
- PR não está em estado incompatível;
- menção `@codex review` registrada.

---

# PARTE XIII - MATRIZ DE RESPONSABILIDADES

# 100. Quem configura o quê

| Item | Starter Kit Maintainer | Projeto/Tech Lead | Builder |
|---|---:|---:|---:|
| Spec Kit version | A/R | C | I |
| Claude minimum/channel | A/R | C | I |
| MCP contract/tool mapping | A/R | C | I |
| MCP credentials | Governança | R | R uso seguro |
| CLAUDE.md corporate | A/R | C | I |
| Agents/skills/hooks | A/R | C | I |
| Quality commands | template | A/R | I |
| Feature spec | I | C | A/R |
| Plan approval | C | A/R | R |
| Builder feedback | I | C | A/R |
| Corporate compliance | framework | C | R execução |
| Independent review | framework | C | R solicitação |
| CODE READY gate | framework | C | R execução |

A = Accountable, R = Responsible, C = Consulted, I = Informed.

---

# 101. O que deve ser commitado e o que não deve

## Commitar

```text
CLAUDE.md
AGENTS.md
engineering.config.json
.mcp.json SEM segredo
.claude/agents/
.claude/skills/
.claude/hooks/
.claude/settings.json
.specify/
specs/
prompts/
scripts/
.github/
evidence corporativa conforme política
```

## Não commitar

```text
.env
.env.*
tokens
passwords
private keys
local secret files
.claude/settings.local.json
.ai-engineering/local/
```

---

# 102. Checklist final de instalação

Marque somente depois de validar.

```text
[ ] VS Code >= 1.98
[ ] Git instalado e identidade configurada
[ ] Python >= 3.11
[ ] uv instalado
[ ] Claude Code CLI instalado
[ ] Claude Code VS Code extension instalada
[ ] GitHub CLI instalado e autenticado
[ ] Starter Kit corporativo clonado
[ ] ZIP importado integralmente incluindo dotfiles
[ ] Spec Kit versão homologada instalada
[ ] Superpowers instalado
[ ] MCP endpoint/auth definido
[ ] MCP project-scoped conecta no piloto
[ ] MCP tools mapeadas
[ ] quality commands reais configurados
[ ] configured=true apenas após configuração real
[ ] Constitution criada
[ ] validate_starter.py PASS
[ ] /mcp validado
[ ] /hooks validado
[ ] /skills validado
[ ] /agents validado
[ ] /plugins mostra Superpowers
[ ] corporate-context consulta o MCP
[ ] smoke feature passa pelo Spec Kit
[ ] plan-review sem Critical/High
[ ] run_quality PASS
[ ] adversarial review sem Critical/High
[ ] spec compliance PASS
[ ] corporate compliance PASS
[ ] pre-review readiness PASS
[ ] Codex review executado
[ ] rework resolvido
[ ] final readiness PASS / CODE READY
[ ] piloto aprovado
[ ] Starter Kit versionado/tagueado
```

---

# APÊNDICE A - ÁRVORE COMPLETA DO ZIP

```text
corporate_ai_engineering_starter_kit_v1/
├── README.md
├── docs/
│   ├── 01_INSTALLATION_AND_BOOTSTRAP.md
│   ├── 02_ADMIN_CONFIGURATION.md
│   ├── 03_BUILDER_USER_MANUAL.md
│   ├── 04_WORKFLOW_DETAILED.md
│   ├── 05_MCP_SOURCE_OF_TRUTH.md
│   ├── 06_CHANGE_IMPACT_ROUTER.md
│   ├── 07_GOVERNANCE_AND_GATES.md
│   ├── 08_TROUBLESHOOTING.md
│   ├── 09_UPGRADE_AND_VERSION_POLICY.md
│   ├── 10_TRAINING_PLAN.md
│   └── 11_SOURCES.md
├── scripts/
│   ├── CONFIGURE_CHECKLIST.md
│   └── bootstrap.py
└── starter-overlay/
    ├── .ai-engineering/
    │   └── README.md
    ├── .claude/
    │   ├── agents/
    │   │   ├── adversarial-reviewer.md
    │   │   ├── architecture-reviewer.md
    │   │   ├── change-impact-classifier.md
    │   │   ├── corporate-compliance-reviewer.md
    │   │   ├── security-reviewer.md
    │   │   ├── simplicity-reviewer.md
    │   │   ├── spec-compliance-reviewer.md
    │   │   └── test-strategy-reviewer.md
    │   ├── hooks/
    │   │   └── mark-stale.py
    │   ├── settings.starter.json
    │   └── skills/
    │       ├── adversarial-review/
    │       │   └── SKILL.md
    │       ├── change-request/
    │       │   └── SKILL.md
    │       ├── code-ready/
    │       │   └── SKILL.md
    │       ├── corporate-compliance/
    │       │   └── SKILL.md
    │       ├── corporate-context/
    │       │   └── SKILL.md
    │       ├── plan-review/
    │       │   └── SKILL.md
    │       ├── post-review-rework/
    │       │   └── SKILL.md
    │       ├── pre-review-gate/
    │       │   └── SKILL.md
    │       ├── run-quality/
    │       │   └── SKILL.md
    │       ├── spec-compliance/
    │       │   └── SKILL.md
    │       └── test-strategy-review/
    │           └── SKILL.md
    ├── .github/
    │   └── pull_request_template.md
    ├── .gitignore.append
    ├── .mcp.starter.json
    ├── AGENTS.md
    ├── CLAUDE.md
    ├── engineering.config.json
    ├── prompts/
    │   ├── 00_CONSTITUTION_PROMPT.md
    │   ├── 01_START_FEATURE.md
    │   ├── 02_PLAN_REVIEW.md
    │   ├── 03_IMPLEMENTATION.md
    │   ├── 04_CHANGE_REQUEST_EXAMPLES.md
    │   ├── 05_CODEX_REVIEW.md
    │   └── 06_REWORK.md
    ├── scripts/
    │   ├── _feature.py
    │   ├── clear_stale_after_gates.py
    │   ├── run_quality.py
    │   ├── validate_readiness.py
    │   └── validate_starter.py
    └── templates/
        └── evidence/
            ├── adversarial-review.example.json
            ├── corporate-compliance.example.json
            ├── evidence-report.example.md
            ├── independent-review.example.json
            ├── spec-compliance.example.json
            └── test-strategy-review.example.json
```

# APÊNDICE B - ARQUIVOS CORE QUE O BOOTSTRAP DISTRIBUI

Os arquivos abaixo já estão prontos no ZIP. Este apêndice existe para facilitar revisão de governança e mostrar exatamente quais contratos são inseridos nos projetos.

## B.1 `CLAUDE.md`

```markdown
# Corporate AI Engineering Rules

## Mission

Operate as the implementation agent inside a governed, specification-driven engineering workflow. The Builder interacts primarily in natural language. Your job is to turn approved intent into robust code while preserving traceability, corporate compliance and executable evidence.

## Source-of-truth hierarchy

Use this order whenever sources conflict:

1. **Corporate Knowledge MCP** for organizational engineering standards, Golden Path, architecture, security, data, UX, integrations, testing and reusable capabilities.
2. **Current feature specification** for functional intent and acceptance criteria.
3. **Repository state** for existing implementation and local constraints.
4. **Project Constitution and this CLAUDE.md** for workflow rules.
5. General model knowledge only where no corporate standard applies.

If corporate guidance conflicts with generic best practice, corporate guidance wins unless it is explicitly deprecated/invalid.

## Corporate Knowledge MCP is mandatory

The MCP server `corporate-knowledge` is an authoritative read-only knowledge source.

Before architecture-sensitive decisions:

1. query the MCP;
2. identify applicable APPROVED standards/guides;
3. identify existing reusable capabilities before proposing new implementations;
4. record IDs/versions/sources when available;
5. do not invent corporate conventions.

If MCP guidance is unavailable or conflicting, explicitly report it. Do not claim corporate compliance without evidence.

Use **Just-in-Time Retrieval** during implementation: refresh relevant MCP guidance when entering tasks involving architecture, security, identity, data, UX, integrations, APIs or testing.

## Workflow

Substantial features follow:

```text
Assessment → Corporate Context → Spec → Clarify → Plan → Plan Review
→ Checklist → Tasks → Analyze → Implement → Verify → Test Strategy Review
→ Adversarial Review → Converge → Spec Compliance → Corporate Compliance
→ Pre-review Gate → PR → Independent Codex Review → Rework → Code Ready
```

Do not skip a gate because the implementation appears simple. The Change Impact Router may select a shorter path for incremental feedback.

## Plan before code

Do not begin substantial implementation without a current spec, plan and tasks. For plan changes, update the relevant artifacts before coding.

## Reuse before build

Before creating a new library, integration, component or technical mechanism, search Corporate Knowledge MCP for:

- existing capability;
- approved pattern;
- Golden Path;
- reference implementation.

Prefer reuse unless the spec/plan explicitly justifies deviation.

## Builder feedback during implementation

The Builder may request adjustments in natural language at any time.

Classify change impact:

- `LOCAL`: cosmetic/local behavior with no material contract/risk impact. Apply directly and verify.
- `BEHAVIORAL`: rule/flow changes. Compare against spec; update spec when it is a new requirement; rerun affected tests/compliance.
- `STRUCTURAL`: architecture, integration, data model, identity, security, NFR, sensitive data, dependencies. Update Plan and run relevant reviewers before implementation.

Choose the **minimum safe rewind**, not a full restart by default.

## Implementation loop

For each task:

```text
Inspect → retrieve relevant corporate context → implement → build/test
→ self-review → fix → repeat until task criteria are proven.
```

Use Superpowers skills when relevant for TDD, systematic debugging and execution discipline.

## Testing

Tests validate behavior, not coverage numbers alone.

For defects:

1. reproduce when practical;
2. create a failing test when practical;
3. fix root cause;
4. demonstrate passing tests;
5. check regressions.

## Evidence over claims

Never declare success because something "looks correct".

Use executable evidence: commands, exit codes, tests and traceability artifacts.

## Reviews

Internal subagents are critics, not implementers. Critical/High findings block progression.

The final code review is independent and performed by Codex on the PR. Do not treat your own review as a substitute.

## Post-review rework

For each independent finding classify:

- VALID;
- PARTIALLY_VALID;
- INVALID.

Validate against code/spec/tests. Correct valid findings, add tests where appropriate, rerun affected gates and request re-review.

## Completion

Do not use the phrase `CODE READY` unless `python scripts/validate_readiness.py --phase final` returns success.

Do not use `READY FOR REVIEW` unless `python scripts/validate_readiness.py --phase pre-review` returns success.

## Safety and secrets

Never read or expose `.env`, `.env.*`, credentials, private keys or secret stores unless an approved workflow explicitly requires it and permissions allow it.

Never put tokens or credentials in committed files.
```

## B.2 `AGENTS.md`

```markdown
# Independent Reviewer Instructions

This repository uses Claude Code as the primary implementation agent and Codex as an independent reviewer.

## Review role

Review independently. Do not assume implementation correctness because Claude or internal agents approved it.

Use, when available:

- feature spec;
- plan;
- tasks;
- PR intent;
- quality evidence;
- spec compliance report;
- corporate compliance manifest;
- test strategy review;
- adversarial review.

Treat those artifacts as context/evidence, not proof by assertion.

## Focus

Prioritize:

1. correctness and regressions;
2. security and authorization;
3. data integrity;
4. missing behavioral tests;
5. error handling / edge conditions;
6. architectural consistency and unnecessary complexity;
7. performance issues with material impact;
8. maintainability.

## Severity

Use:

- CRITICAL — must block.
- HIGH — must block.
- MEDIUM — fix or explicitly accept with rationale.
- LOW — recommendation.
- NIT — optional.

For each finding include concrete file/location, scenario and consequence. Avoid style-only noise unless it creates real maintenance risk.

Do not claim that corporate MCP compliance is verified unless you have direct access to the same authoritative source. You may verify that the evidence is internally consistent and that the code does not contradict the referenced guidance visible in the repository/PR.
```

## B.3 `engineering.config.json`

```json
{
  "schemaVersion": 1,
  "configured": false,
  "workflow": {
    "mcpRequired": true,
    "mcpServerName": "corporate-knowledge",
    "blockCritical": true,
    "blockHigh": true,
    "mediumRequiresResolutionOrAcceptance": true,
    "builderDefaultInteraction": "natural-language",
    "codeReadyValidator": "python scripts/validate_readiness.py --phase final"
  },
  "mcp": {
    "expectedDomains": [
      "architecture",
      "security",
      "data",
      "ux",
      "integration",
      "testing"
    ],
    "approvedDocumentStatuses": [
      "APPROVED"
    ],
    "toolMapping": {
      "searchGuidance": "__MAP_TO_REAL_MCP_TOOL__",
      "getDocument": "__MAP_TO_REAL_MCP_TOOL__",
      "getApplicableGuidance": "__MAP_TO_REAL_MCP_TOOL__",
      "getCapability": "__MAP_TO_REAL_MCP_TOOL__",
      "getGoldenPath": "__MAP_TO_REAL_MCP_TOOL__",
      "getExamples": "__MAP_TO_REAL_MCP_TOOL__"
    }
  },
  "qualityCommands": [
    {
      "name": "format-check",
      "command": "__CONFIGURE_PROJECT_COMMAND__",
      "enabled": false
    },
    {
      "name": "lint",
      "command": "__CONFIGURE_PROJECT_COMMAND__",
      "enabled": false
    },
    {
      "name": "build",
      "command": "__CONFIGURE_PROJECT_COMMAND__",
      "enabled": false
    },
    {
      "name": "unit-tests",
      "command": "__CONFIGURE_PROJECT_COMMAND__",
      "enabled": false
    },
    {
      "name": "static-analysis",
      "command": "__CONFIGURE_PROJECT_COMMAND__",
      "enabled": false
    }
  ],
  "evidence": {
    "directoryName": "evidence",
    "requiredPreReview": [
      "quality-run.json",
      "test-strategy-review.json",
      "adversarial-review.json",
      "spec-compliance.json",
      "corporate-compliance.json",
      "evidence-report.md"
    ],
    "requiredFinal": [
      "independent-review.json"
    ]
  }
}
```

## B.4 `.mcp.starter.json`

```json
{
  "mcpServers": {
    "corporate-knowledge": {
      "type": "http",
      "url": "${CORPORATE_MCP_URL:-}",
      "headers": {
        "Authorization": "Bearer ${CORPORATE_MCP_TOKEN:-}"
      }
    }
  }
}
```

## B.5 `.claude/settings.starter.json`

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/.env)",
      "Read(./**/.env.*)",
      "Read(./**/*credential*)",
      "Read(./**/*private_key*)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python",
            "args": [
              "${CLAUDE_PROJECT_DIR}/.claude/hooks/mark-stale.py"
            ]
          }
        ]
      }
    ]
  }
}
```

## B.6 `.github/pull_request_template.md`

```markdown
## Intent

<!-- What problem/change does this PR implement? -->

## Spec / Plan

- Spec: `specs/.../spec.md`
- Plan: `specs/.../plan.md`
- Tasks: `specs/.../tasks.md`

## Corporate guidance applied

<!-- IDs/versions or link to evidence/corporate-context.md -->

## Reusable capabilities used

<!-- List approved capabilities reused instead of reimplemented -->

## Verification evidence

- [ ] `quality-run.json` PASS
- [ ] `test-strategy-review.json` PASS
- [ ] `adversarial-review.json` has 0 Critical / 0 High
- [ ] `spec-compliance.json` PASS
- [ ] `corporate-compliance.json` PASS
- [ ] `/speckit.converge` completed
- [ ] Pre-review gate PASS

## Risks / exceptions

<!-- Any accepted medium finding or standard exception must have rationale + owner -->

## Independent review

After PR is ready, request Codex review:

```text
@codex review for correctness, regressions, security, missing tests and maintainability. Treat the PR intent and engineering evidence as context, but review the code independently.
```
```

# APÊNDICE C - PROMPTS CANÔNICOS DO ZIP

## C.1 `00_CONSTITUTION_PROMPT.md`

Use with `/speckit.constitution`:

```text
Create/update this project's engineering constitution with these non-negotiable principles:

1. Specification precedes substantial implementation.
2. Corporate Knowledge MCP is the authoritative source for organizational standards, Golden Path, approved capabilities and engineering conventions.
3. Never invent a corporate convention when MCP evidence is missing.
4. Reuse approved corporate capabilities before building new mechanisms.
5. Resolve ambiguity explicitly; consult repo/MCP before interrupting the Builder.
6. Plan before code for material changes.
7. Builder feedback may use the minimum safe workflow rewind based on Local/Behavioral/Structural impact.
8. Tests prove behavior, not merely coverage.
9. Critical and High review findings block progression.
10. Implementation agent and final PR reviewer must be independent.
11. Evidence over agent claims: successful builds/tests/reviews must be executable and recorded.
12. Corporate compliance must be revalidated before PR.
13. No CODE READY state without final deterministic readiness gate.
14. Do not expose secrets; project agents must not read .env/credential/private-key files in normal workflow.
```

## C.2 `01_START_FEATURE.md`

Example Builder input after assessment GO:

```text
/corporate-context
We need to allow authenticated suppliers to update contact and address data. CNPJ must remain immutable and all changes need auditability.
```

Then:

```text
/speckit.specify
Allow an authenticated supplier to update phone, email and address. CNPJ cannot be changed after onboarding. Every accepted change must be auditable. If an update fails, the system must not persist partial changes.
```

## C.3 `02_PLAN_REVIEW.md`

Preferred command:

```text
/plan-review
```

Equivalent natural-language request:

```text
Run independent architecture, security, test-strategy and simplicity reviews of the current plan. Each reviewer must consult applicable Corporate Knowledge MCP guidance. Do not implement. Consolidate findings by severity and do not approve while Critical/High remain.
```

## C.4 `03_IMPLEMENTATION.md`

Use `/speckit.implement`. If you need to reinforce behavior:

```text
Implement task-by-task. Before architecture/security/data/UX/integration/testing decisions, refresh relevant Corporate Knowledge MCP guidance. Use existing approved capabilities before creating new mechanisms. For each task: inspect → implement → build/test → self-review → fix → prove task criteria. Do not silently alter the spec or plan.
```

## C.5 `04_CHANGE_REQUEST_EXAMPLES.md`

# Change request examples

## Local

```text
/change-request I don't like the layout. Reduce vertical whitespace, group the main fields into cards, and move the actions to the upper-right using the approved Design System.
```

## Behavioral

```text
/change-request The rule is wrong: CNPJ must be immutable after initial registration. Correct the behavior and tests, and update the spec if this was not already explicit.
```

## Structural

```text
/change-request After saving the supplier, publish the approved corporate domain event consumed by System X.
```

## C.6 `05_CODEX_REVIEW.md`

Use on GitHub PR:

```text
@codex review for correctness, regressions, security, data integrity, missing behavioral tests and maintainability. Treat the PR intent and attached engineering evidence as context, but review the implementation independently. Prioritize high-signal findings and include concrete file/location, scenario and consequence.
```

## C.7 `06_REWORK.md`

Preferred command:

```text
/post-review-rework
```

Equivalent natural-language request:

```text
Process every Codex finding independently. Classify VALID, PARTIALLY_VALID or INVALID using code/spec/test evidence. Fix valid issues at root cause, add regression tests when practical, rerun affected quality/compliance gates, document invalid findings with evidence, and request re-review. Do not mark review resolved while Critical/High remain.
```

# APÊNDICE D - COMANDOS DE REFERÊNCIA RÁPIDA

## D.1 Preparação

```powershell
git --version
python --version
uv --version
claude --version
gh --version
code --version
```

## D.2 Spec Kit

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.0.4
specify version
specify self check
```

## D.3 Bootstrap

```powershell
python .\scripts\bootstrap.py --target C:\src\ai-first-engineering\SEU-PROJETO
```

## D.4 Claude Code - instalação do Superpowers

```text
/plugin install superpowers@claude-plugins-official
```

## D.5 Validações Claude

```text
/status
/mcp
/hooks
/skills
/agents
/plugins
```

## D.6 Workflow do Builder

```text
/speckit-assess-intake
/speckit-assess-research
/speckit-assess-define
/speckit-assess-shape
/speckit-assess-decide
/corporate-context
/speckit.specify
/speckit.clarify
/speckit.checklist
/speckit.plan
/plan-review
/speckit.tasks
/speckit.analyze
/speckit.implement
/run-quality
/test-strategy-review
/adversarial-review
/speckit.converge
/spec-compliance
/corporate-compliance
/pre-review-gate
/post-review-rework
/code-ready
```

## D.7 Gates

```powershell
python .\scripts\run_quality.py
python .\scripts\validate_readiness.py --phase pre-review
python .\scripts\validate_readiness.py --phase final
```

---

# APÊNDICE E - REFERÊNCIAS OFICIAIS CONSULTADAS

Data de consulta: 07/09/2026.

1. Claude Code - instalação e Windows: https://code.claude.com/docs/en/installation
2. Claude Code - VS Code: https://code.claude.com/docs/pt/vs-code
3. Claude Code - MCP: https://code.claude.com/docs/en/mcp
4. Claude Code - Hooks: https://code.claude.com/docs/en/hooks
5. Claude Code - Skills: https://code.claude.com/docs/en/skills
6. Claude Code - Subagents: https://code.claude.com/docs/en/sub-agents
7. GitHub Spec Kit - Installation: https://github.com/github/spec-kit/blob/main/docs/installation.md
8. GitHub Spec Kit - Releases: https://github.com/github/spec-kit/releases
9. GitHub Spec Kit - Assess: https://github.com/github/spec-kit/blob/main/extensions/assess/README.md
10. Superpowers: https://github.com/obra/superpowers
11. uv - Installation: https://docs.astral.sh/uv/getting-started/installation/
12. Git for Windows: https://git-scm.com/install/windows
13. GitHub CLI: https://cli.github.com/manual/
14. OpenAI Codex Code Review: https://openai.com/index/introducing-upgrades-to-codex/

---

# 103. Critério de encerramento

A instalação técnica não termina quando as ferramentas estão instaladas. Ela termina quando **um segundo Builder**, sem ajuda artesanal do criador do Starter Kit, consegue:

```text
abrir o projeto
-> conectar MCP
-> iniciar uma ideia
-> especificar
-> planejar
-> implementar em linguagem natural
-> iterar
-> gerar evidência
-> passar pelo review independente
-> atingir CODE READY
```

Se somente o maintainer consegue executar o processo, o Starter Kit ainda não está pronto para escala.
