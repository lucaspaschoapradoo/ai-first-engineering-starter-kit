# ai-first-engineering-starter-kit

<img width="1536" height="1024" alt="ChatGPT Image 7_09_2026, 18_28_34" src="https://github.com/user-attachments/assets/5559f023-9b2b-4a90-8969-95593abac79d" />

Starter Kit corporativo para desenvolvimento **AI-First**, estruturado para operar com **VS Code + Claude Code + GitHub Spec Kit + Superpowers + agentes especializados + MCP corporativo + Code Review independente**.

O objetivo deste repositório é transformar o desenvolvimento assistido por IA em um processo de engenharia **estruturado, rastreável, reproduzível e governado**.

Em vez de operar no modelo:

```text
Prompt → Código
```

o Starter Kit estabelece:

```text
Ideia
↓
Assessment
↓
Corporate Context Discovery
↓
Specification
↓
Clarification
↓
Planning
↓
Multi-Agent Review
↓
Task Decomposition
↓
Implementation
↓
Continuous Verification
↓
Test Strategy Review
↓
Adversarial Review
↓
Spec Compliance
↓
Corporate Compliance
↓
Independent Code Review
↓
Rework
↓
CODE READY
```

---

# 1. Objetivo

Este Starter Kit fornece a base comum para que aplicações desenvolvidas com IA sigam um mesmo modelo de engenharia.

Ele padroniza:

- como uma ideia vira especificação;
- como ambiguidades são eliminadas;
- como soluções são planejadas antes da implementação;
- como Claude Code deve trabalhar;
- como padrões corporativos são consultados;
- como o Golden Path é aplicado;
- como testes e evidências são gerados;
- como agentes independentes revisam a implementação;
- como findings são tratados;
- quando uma implementação pode ser considerada `CODE READY`.

O objetivo não é limitar o uso da IA.

O objetivo é permitir **mais autonomia com mais controle**.

---

# 2. Princípios

## 2.1 Specification before implementation

Nenhuma feature relevante deve começar diretamente pelo código.

A implementação deve ser precedida por:

```text
Intent
→ Specification
→ Clarification
→ Plan
→ Tasks
```

---

## 2.2 Evidence over claims

O agente não pode considerar uma atividade concluída apenas porque acredita que o código está correto.

Conclusões precisam ser sustentadas por evidências executáveis:

- build;
- testes;
- análise estática;
- compliance;
- review;
- rastreabilidade.

---

## 2.3 Corporate Knowledge over generic knowledge

O conhecimento geral do modelo não substitui padrões corporativos.

A hierarquia de fontes é:

```text
1. Corporate Knowledge MCP
2. Feature Specification
3. Repository
4. CLAUDE.md / Engineering Constitution
5. General model knowledge
```

Se existir uma recomendação corporativa aplicável, ela tem precedência.

---

## 2.4 Reuse before build

Antes de criar uma nova capability, integração, componente ou padrão, o agente deve consultar o MCP corporativo.

A ordem esperada é:

```text
Necessidade
↓
Existe capability corporativa?
├── Sim → Reutilizar
└── Não
    ↓
Existe pattern / guideline?
├── Sim → Aplicar
└── Não → Projetar
```

---

## 2.5 Plan before code

Claude Code não deve iniciar uma implementação estrutural sem um plano previamente validado.

---

## 2.6 Independent review

O agente responsável pela implementação não deve ser o único responsável pela validação final.

A solução utiliza:

- Claude Code para planejamento e implementação;
- subagents especializados para revisão;
- Codex para Code Review independente.

---

## 2.7 Fail closed

Se um gate obrigatório não puder ser validado, o processo deve bloquear.

Exemplos:

- MCP indisponível;
- spec ausente;
- testes não executados;
- Critical/High findings abertos;
- compliance não validado.

O sistema não deve assumir conformidade.

---

# 3. Experiência do Builder

O Builder trabalha prioritariamente em **linguagem natural**.

Não é necessário utilizar o código como principal interface de trabalho.

Exemplo:

```text
"Precisamos permitir que fornecedores atualizem
telefone, e-mail e endereço.

CNPJ não poderá ser alterado.

As mudanças devem possuir histórico."
```

A partir disso, a esteira conduz:

```text
Specification
↓
Clarification
↓
Planning
↓
Implementation
↓
Validation
↓
Review
```

O Builder continua responsável por:

- intenção;
- regra de negócio;
- decisões;
- aceite;
- priorização.

A IA executa grande parte do trabalho operacional de engenharia.

---

# 4. Iterações durante o desenvolvimento

O processo não é uma esteira rígida e totalmente linear.

O Builder pode solicitar alterações em linguagem natural durante a implementação.

Exemplo:

```text
"Não gostei desse layout.
Quero os campos principais em cards
e as ações no canto superior direito."
```

A solicitação é classificada por impacto.

| Tipo | Exemplo | Comportamento |
|---|---|---|
| Local | layout, cor, espaçamento, texto | altera diretamente e revalida |
| Behavioral | nova regra ou ajuste funcional | atualiza spec quando necessário |
| Structural | integração, arquitetura, segurança, novo domínio | retorna ao planning/review |

Princípio:

> O Builder pode evitar etapas desnecessárias, mas os controles aplicáveis à mudança não podem ser ignorados.

---

# 5. Componentes principais

O Starter Kit utiliza:

### VS Code

Ambiente principal do Builder.

### Claude Code

Agente principal para:

- análise;
- planejamento;
- implementação;
- testes;
- correções;
- geração de evidências.

### GitHub Spec Kit

Backbone do processo Spec-Driven:

```text
Specify
Clarify
Checklist
Plan
Tasks
Analyze
Implement
Converge
```

### Superpowers

Disciplina adicional para:

- planejamento;
- execução incremental;
- TDD;
- debugging;
- verification;
- subagent-driven development.

### Corporate Knowledge MCP

Fonte de verdade corporativa para:

- Golden Path;
- arquitetura;
- padrões;
- convenções;
- segurança;
- APIs;
- design;
- componentes;
- integrações;
- exemplos;
- documentação.

### Codex

Revisor independente do Pull Request.

---

# 6. Arquitetura do workflow

```text
                        CORPORATE KNOWLEDGE MCP
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ↓                      ↓                      ↓
    SPECIFICATION              PLAN              IMPLEMENTATION
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 ↓
                           VERIFICATION
                                 ↓
                        SPEC COMPLIANCE
                                 +
                     CORPORATE COMPLIANCE
                                 ↓
                        INDEPENDENT REVIEW
                                 ↓
                              REWORK
                                 ↓
                           CODE READY
```

O MCP é transversal à esteira.

Ele não é apenas consultado no início.

Ele pode ser utilizado durante:

- specification;
- clarification;
- planning;
- implementation;
- testing;
- architecture review;
- security review;
- compliance.

---

# 7. Estrutura do repositório

Estrutura de referência:

```text
ai-first-engineering-starter-kit/
│
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── engineering.config.json
├── .mcp.json
│
├── .claude/
│   │
│   ├── agents/
│   │   ├── architecture-reviewer.md
│   │   ├── security-reviewer.md
│   │   ├── test-strategy-reviewer.md
│   │   ├── simplicity-reviewer.md
│   │   ├── adversarial-reviewer.md
│   │   ├── spec-compliance-reviewer.md
│   │   ├── corporate-compliance-reviewer.md
│   │   └── change-impact-classifier.md
│   │
│   ├── skills/
│   │   ├── corporate-context/
│   │   ├── plan-review/
│   │   ├── change-request/
│   │   ├── run-quality/
│   │   ├── test-strategy-review/
│   │   ├── adversarial-review/
│   │   ├── spec-compliance/
│   │   ├── corporate-compliance/
│   │   ├── pre-review-gate/
│   │   ├── post-review-rework/
│   │   └── code-ready/
│   │
│   ├── hooks/
│   │   └── mark-stale.py
│   │
│   └── settings.json
│
├── specs/
│
├── evidence/
│   ├── quality-run.json
│   ├── test-strategy-review.json
│   ├── adversarial-review.json
│   ├── spec-compliance.json
│   ├── corporate-compliance.json
│   ├── independent-review.json
│   └── evidence-report.md
│
├── scripts/
│   ├── bootstrap.py
│   ├── run_quality.py
│   └── validate_readiness.py
│
├── docs/
│   ├── installation.md
│   ├── builder-guide.md
│   ├── mcp-guide.md
│   └── governance.md
│
└── .github/
    └── pull_request_template.md
```

A estrutura poderá evoluir sem alterar os princípios centrais da esteira.

---

# 8. Pré-requisitos

Antes de utilizar o Starter Kit, a estação precisa possuir:

- VS Code;
- Git;
- Python 3.11+;
- `uv`;
- Claude Code;
- acesso ao GitHub corporativo;
- acesso ao Corporate Knowledge MCP;
- acesso ao Codex para revisão independente;
- toolchain da aplicação.

Validar:

```bash
git --version
python --version
uv --version
claude --version
```

---

# 9. Instalação do Claude Code

## Windows

PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

ou via `winget`, conforme padrão corporativo.

Depois:

```bash
claude --version
```

Abrir o repositório no VS Code e instalar a extensão oficial do Claude Code.

---

# 10. GitHub Spec Kit

Instalar:

```bash
uv tool install specify-cli
```

Validar:

```bash
specify version
```

Para ambientes corporativos, utilizar uma versão homologada e pinada.

---

# 11. Inicialização do Spec Kit

No repositório da aplicação:

```bash
specify init --here --force --non-interactive --integration claude --script py
```

Adicionar avaliação de ideias:

```bash
specify extension add assess
```

---

# 12. Superpowers

Dentro do Claude Code:

```text
/plugin install superpowers@claude-plugins-official
```

Validar usando:

```text
/plugins
```

---

# 13. Configuração do MCP

O Corporate Knowledge MCP deve ser configurado em:

```text
.mcp.json
```

Exemplo conceitual:

```json
{
  "mcpServers": {
    "corporate-knowledge": {
      "transport": "http",
      "url": "${CORPORATE_MCP_URL}",
      "headers": {
        "Authorization": "Bearer ${CORPORATE_MCP_TOKEN}"
      }
    }
  }
}
```

Credenciais nunca devem ser commitadas.

Utilizar variáveis de ambiente ou mecanismo corporativo de secrets.

---

# 14. Corporate Knowledge MCP

O MCP deve ser tratado como **read-only** durante o desenvolvimento.

O agente pode:

- buscar guidelines;
- consultar padrões;
- ler exemplos;
- localizar Golden Paths;
- identificar capabilities;
- consultar documentação.

O agente não deve alterar unilateralmente a fonte normativa.

Mudanças em guidelines devem possuir governança própria.

---

# 15. Fluxo padrão

## Etapa 1 — Idea Assessment

```text
/speckit-assess-intake
/speckit-assess-research
/speckit-assess-define
/speckit-assess-shape
/speckit-assess-decide
```

Resultado:

```text
GO
NEEDS CLARIFICATION
KILL
```

Somente `GO` segue para desenvolvimento.

---

# 16. Corporate Context Discovery

Antes da especificação ou durante sua criação:

```text
/corporate-context
```

Objetivo:

identificar:

- Golden Path aplicável;
- padrões arquiteturais;
- security guidelines;
- padrões de UI;
- capabilities existentes;
- integrações disponíveis;
- padrões de testes;
- restrições.

O resultado deve ser utilizado na especificação e no planejamento.

---

# 17. Specification

Executar:

```text
/speckit.specify
```

A specification deve conter:

- requisitos funcionais;
- regras de negócio;
- user flows;
- acceptance criteria;
- NFRs;
- out of scope;
- corporate constraints.

---

# 18. Clarification

Executar:

```text
/speckit.clarify
```

O agente deve identificar:

- ambiguidades;
- assumptions;
- contradições;
- dados faltantes;
- riscos.

Antes de perguntar ao Builder, deve consultar o MCP quando a questão estiver relacionada a padrões corporativos.

---

# 19. Specification Checklist

Executar:

```text
/speckit.checklist
```

O objetivo é validar a qualidade da própria especificação.

---

# 20. Solution Plan

Executar:

```text
/speckit.plan
```

O plano deve incluir:

- arquitetura;
- componentes;
- arquivos impactados;
- dados;
- APIs;
- integrações;
- estratégia de testes;
- riscos;
- capabilities corporativas reutilizadas;
- guidance do MCP aplicado.

---

# 21. Multi-Agent Plan Review

Executar:

```text
/plan-review
```

Subagents utilizados:

```text
architecture-reviewer
security-reviewer
test-strategy-reviewer
simplicity-reviewer
```

Critérios:

```text
0 Critical
0 High
```

antes de avançar.

---

# 22. Task Decomposition

Executar:

```text
/speckit.tasks
```

Cada tarefa deve possuir:

- objetivo;
- dependências;
- arquivos impactados;
- testes esperados;
- critério de pronto.

---

# 23. Consistency Analysis

Executar:

```text
/speckit.analyze
```

Essa etapa valida consistência entre:

```text
SPEC
PLAN
TASKS
```

---

# 24. Implementation

Executar:

```text
/speckit.implement
```

Modelo esperado:

```text
Task
↓
Inspect
↓
Retrieve MCP Context
↓
Implement
↓
Compile
↓
Test
↓
Self Review
↓
Fix
↺
```

Claude deve implementar uma unidade coerente por vez.

---

# 25. Ajustes solicitados pelo Builder

Durante a implementação, utilizar:

```text
/change-request
```

Exemplo:

```text
/change-request

Não gostei do layout.
Quero diminuir a densidade da tela
e colocar as ações principais no topo.
```

A mudança será classificada como:

```text
LOCAL
BEHAVIORAL
STRUCTURAL
```

E o fluxo retornará apenas ao ponto necessário.

---

# 26. Continuous Verification

Executar:

```text
/run-quality
```

O projeto deve possuir comandos configurados para:

- formatter;
- lint;
- build;
- unit tests;
- static analysis;
- architecture checks.

O processo deve corrigir e repetir enquanto houver falha.

---

# 27. Test Strategy Review

Executar:

```text
/test-strategy-review
```

O reviewer deve verificar:

- acceptance criteria;
- happy path;
- negative path;
- edge cases;
- authorization;
- error handling;
- regression;
- integration;
- gaps.

---

# 28. Adversarial Review

Executar:

```text
/adversarial-review
```

Princípio:

> Assume that the implementation contains defects and find evidence.

O reviewer tenta encontrar:

- regressões;
- inconsistências;
- bypass;
- erro de autorização;
- edge cases;
- problemas de concorrência;
- problemas de dados;
- regras quebradas.

---

# 29. Convergence

Executar:

```text
/speckit.converge
```

A implementação deve convergir com:

```text
SPEC
PLAN
TASKS
```

---

# 30. Spec Compliance

Executar:

```text
/spec-compliance
```

Valida:

```text
Requirements
×
Code
×
Tests
×
Evidence
```

---

# 31. Corporate Compliance

Executar:

```text
/corporate-compliance
```

Valida a implementação contra o Corporate Knowledge MCP.

Resultado deve registrar:

- guidelines consultados;
- versões;
- capabilities reutilizadas;
- conflitos;
- exceções;
- status.

Exemplo:

```json
{
  "status": "PASS",
  "mcpConnected": true,
  "standards": [
    {
      "id": "ARCH-012",
      "version": "4.2"
    },
    {
      "id": "SEC-004",
      "version": "3.1"
    }
  ],
  "conflicts": [],
  "exceptions": []
}
```

---

# 32. Pre-Review Gate

Executar:

```text
/pre-review-gate
```

ou diretamente:

```bash
python scripts/validate_readiness.py --phase pre-review
```

O Pull Request só deve ser criado se o gate estiver aprovado.

---

# 33. Independent Code Review

Criar Pull Request.

Solicitar:

```text
@codex review
```

ou:

```text
@codex review for correctness, regressions, security,
spec compliance and missing tests.
```

O Code Review final deve ser independente do Claude.

---

# 34. Findings

Se existirem findings:

```text
/post-review-rework
```

Para cada finding:

```text
VALID
INVALID
PARTIALLY VALID
```

Findings válidos devem gerar:

```text
Investigate
↓
Reproduce
↓
Fix
↓
Tests
↓
Compliance
↓
Re-review
```

---

# 35. Code Ready

Executar:

```text
/code-ready
```

O comando deve validar:

```bash
python scripts/validate_readiness.py --phase final
```

A expressão:

```text
CODE READY
```

somente pode ser utilizada se o gate final retornar sucesso.

---

# 36. Critérios de bloqueio

Bloqueiam conclusão:

- build falhando;
- testes falhando;
- MCP obrigatório indisponível;
- spec compliance diferente de `PASS`;
- corporate compliance diferente de `PASS`;
- Critical finding aberto;
- High finding aberto;
- review independente não realizado;
- evidência obsoleta;
- mudança posterior não revalidada.

---

# 37. Severidade

| Severidade | Tratamento |
|---|---|
| Critical | bloqueia |
| High | bloqueia |
| Medium | corrigir ou justificar |
| Low | recomendação |
| Nit | opcional |

---

# 38. Evidence

Os artefatos de qualidade devem ser gravados em:

```text
evidence/
```

Exemplos:

```text
quality-run.json
test-strategy-review.json
adversarial-review.json
spec-compliance.json
corporate-compliance.json
independent-review.json
evidence-report.md
```

Esses arquivos criam rastreabilidade entre intenção e implementação.

---

# 39. Evidências obsoletas

Quando código, spec, plan ou tasks forem alterados após validação, evidências relacionadas podem ser marcadas como stale.

Isso evita:

```text
Review passou
↓
Código mudou
↓
Review antigo continua sendo considerado válido
```

O processo exige revalidação.

---

# 40. Definition of Ready

Uma feature pode iniciar implementação quando possuir:

```text
GO
Spec criada
Clarification concluído
Checklist concluído
Plan criada
Plan Review aprovado
Tasks criadas
Analyze aprovado
Corporate Context identificado
```

---

# 41. Definition of Done — Camada 1

Uma feature somente é `CODE READY` quando possuir:

```text
All Tasks Complete

Build PASS

Tests PASS

Test Strategy Review PASS

Adversarial Review concluído

Spec Converged

Spec Compliance PASS

Corporate Compliance PASS

MCP Evidence registrada

0 Critical

0 High

Independent Code Review concluído

Review Findings resolvidos

Final Readiness Gate PASS
```

---

# 42. Bootstrap

Para aplicar o Starter Kit em outro repositório:

```bash
python scripts/bootstrap.py --target /path/do/projeto
```

O bootstrap pode preparar:

- integração Spec Kit;
- agentes;
- skills;
- hooks;
- configuração MCP;
- templates;
- scripts;
- evidências;
- PR template;
- CLAUDE.md.

---

# 43. Arquivos que devem ser customizados por aplicação

Cada aplicação precisa informar seus comandos reais em:

```text
engineering.config.json
```

Exemplo:

```json
{
  "quality": {
    "format": "./mvnw spotless:check",
    "lint": "npm run lint",
    "build": "./mvnw clean verify",
    "unitTests": "./mvnw test",
    "staticAnalysis": "./mvnw sonar:sonar"
  }
}
```

Não deixar comandos fictícios marcados como válidos.

---

# 44. Segurança

Nunca commit:

- tokens;
- passwords;
- API keys;
- secrets;
- credenciais MCP;
- credenciais GitHub;
- credenciais de banco.

Utilizar mecanismos corporativos de secrets.

---

# 45. Governança do Starter Kit

Alterações neste Starter Kit devem ser tratadas como alterações em uma plataforma interna.

Mudanças relevantes devem considerar:

- compatibilidade;
- impacto em Builders;
- impacto nos agentes;
- alteração de comportamento;
- novas versões do Claude Code;
- novas versões do Spec Kit;
- novos padrões corporativos.

Recomenda-se manter releases versionadas:

```text
v1.0.0
v1.1.0
v2.0.0
```

---

# 46. O que não fazer

## Não iniciar pelo código

```text
"Claude, construa isso."
```

sem spec e planejamento.

## Não inventar padrões corporativos

Consultar MCP.

## Não duplicar capability existente

Aplicar `Reuse before Build`.

## Não aceitar self-approval

Claude não é o reviewer final.

## Não confiar em coverage isoladamente

Validar comportamento.

## Não ignorar mudança de escopo

Usar Change Impact Router.

## Não declarar CODE READY manualmente

Executar o gate.

---

# 47. Modelo mental

A arquitetura pode ser resumida em:

```text
Claude Intelligence
        +
Corporate Knowledge MCP
        +
Spec-Driven Workflow
        +
Specialized Review Agents
        +
Deterministic Gates
        +
Independent Code Review
        ↓
Robust Corporate Software
```

---

# 48. Resultado esperado

Este Starter Kit deve permitir que um Builder trabalhe de forma próxima a:

```text
"Tenho uma ideia."
↓
IA estrutura
↓
IA consulta os padrões corporativos
↓
IA elimina ambiguidades
↓
IA propõe solução
↓
agentes criticam
↓
Claude implementa
↓
Builder acompanha e ajusta em linguagem natural
↓
testes e gates validam
↓
agentes tentam quebrar
↓
compliance é comprovado
↓
Codex revisa
↓
Claude corrige
↓
CODE READY
```

A meta é combinar:

**velocidade de Vibe Coding**

com

**disciplina de engenharia corporativa**.

---

# 49. Visão

O `ai-first-engineering-starter-kit` não é apenas uma coleção de prompts.

Ele representa um **modelo operacional de engenharia AI-First**.

A IA deixa de atuar como um gerador isolado de código e passa a operar dentro de um sistema que possui:

- especificações;
- contexto institucional;
- constraints;
- padrões;
- revisão independente;
- testes;
- evidências;
- compliance;
- gates.

> **AI-First não significa remover engenharia.  
> Significa utilizar IA para executar engenharia com mais velocidade, consistência e inteligência.**
