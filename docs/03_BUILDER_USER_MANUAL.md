# 03 — Manual do Builder

## Princípio

O Builder trabalha **principalmente em linguagem natural**. O Builder não precisa editar código manualmente no fluxo padrão.

A IA executa; o Builder define intenção, responde ambiguidades, valida comportamento e decide sobre mudanças.

## Regra mais importante

Não comece com:

```text
"Claude, construa X."
```

Comece pelo workflow.

---

# Fluxo A — Nova ideia relevante

## 1. Assessment

Use as skills de assessment do Spec Kit exibidas por `/skills`.

Versões atuais normalmente expõem:

```text
/speckit-assess-intake
/speckit-assess-research
/speckit-assess-define
/speckit-assess-shape
/speckit-assess-decide
```

A saída final deve ser:

```text
GO
NEEDS CLARIFICATION
KILL
```

Somente `GO` avança.

> Para uma pequena alteração já aprovada pelo produto, o assessment completo pode ser dispensado conforme a política do time.

## 2. Corporate Context Discovery

Execute:

```text
/corporate-context <descrição resumida da necessidade>
```

Claude deve consultar o Corporate Knowledge MCP e identificar:

- Golden Path aplicável;
- standards;
- guidelines;
- capabilities existentes;
- exemplos aprovados;
- restrições;
- requisitos de segurança/dados/UX/testes.

Se o MCP estiver indisponível, decisões sensíveis ficam bloqueadas.

## 3. Specification

```text
/speckit.specify
```

Descreva **o quê e por quê**, não a arquitetura.

Exemplo:

```text
Permitir que um fornecedor autenticado atualize telefone, e-mail e endereço.
CNPJ não pode ser alterado.
Toda alteração deve ser auditada.
Se houver erro, nenhuma alteração parcial pode persistir.
```

## 4. Clarification

```text
/speckit.clarify
```

Claude primeiro deve procurar respostas no repositório e no MCP. Pergunta ao Builder apenas o que não pode ser inferido com segurança.

Responda em linguagem natural.

Repita até eliminar ambiguidades materiais.

## 5. Plan

Coloque Claude em Plan Mode quando apropriado e execute:

```text
/speckit.plan
```

## 6. Multi-Agent Plan Review

```text
/plan-review
```

O resultado precisa ter:

```text
0 Critical
0 High
```

antes de seguir.

## 7. Checklist, Tasks e Analyze

```text
/speckit.checklist
/speckit.tasks
/speckit.analyze
```

Não implementar com inconsistências materiais abertas.

## 8. Implement

```text
/speckit.implement
```

Claude deve trabalhar task-by-task com:

```text
Inspect → Implement → Build → Test → Self-review → Fix → Repeat
```

Superpowers deve ser utilizado pelo Claude quando pertinente para TDD, debugging e execução disciplinada.

---

# Iteração manual do Builder durante Implement

Você pode pedir alterações imediatamente em linguagem natural.

### Exemplo — visual

```text
Não gostei do layout. Coloque os dados principais em cards, reduza o espaço vertical e mova as ações para o canto superior direito.
```

Claude classifica como `LOCAL/COSMETIC`, aplica e revalida sem reiniciar toda a esteira.

### Exemplo — regra

```text
O CNPJ não pode ser alterado depois do primeiro cadastro.
```

Claude verifica a spec:

- se a regra já existia: corrige implementação/testes;
- se é nova: atualiza spec e executa impacto necessário.

### Exemplo — mudança estrutural

```text
Ao salvar, publique também um evento corporativo para o sistema X.
```

Claude deve classificar como `STRUCTURAL` e retornar ao Plan/Review necessário antes de codificar.

Use explicitamente quando quiser:

```text
/change-request <pedido de alteração>
```

---

# Pós-implementação

## 9. Rodar Quality Gate

```text
/run-quality
```

ou terminal:

```bash
python scripts/run_quality.py
```

## 10. Test Strategy Review

```text
/test-strategy-review
```

Gaps encontrados retornam para implementação/testes.

## 11. Adversarial Review

```text
/adversarial-review
```

O reviewer assume que há defeitos e procura evidências concretas.

## 12. Converge

```text
/speckit.converge
```

Se forem adicionadas tasks restantes, implemente e converja novamente.

## 13. Spec Compliance

```text
/spec-compliance
```

## 14. Corporate Compliance

```text
/corporate-compliance
```

A revisão deve consultar novamente o MCP e produzir rastreabilidade de standards.

## 15. Pre-review Gate

```text
/pre-review-gate
```

Se falhar, não crie PR ainda.

## 16. Pull Request e Codex

Crie o PR conforme o template.

Solicite revisão independente:

```text
@codex review
```

Sugestão:

```text
@codex review for correctness, regressions, security, missing tests and maintainability. Treat the PR intent and attached engineering evidence as context, but review the code independently.
```

## 17. Rework

Depois dos findings:

```text
/post-review-rework
```

Claude deve classificar cada finding:

```text
VALID
PARTIALLY_VALID
INVALID
```

Findings válidos são reproduzidos/corrigidos/testados.

## 18. Final Readiness

```text
/code-ready
```

Somente declarar `CODE READY` com:

- quality PASS;
- spec compliance PASS;
- corporate compliance PASS;
- adversarial review sem Critical/High;
- Codex review resolvido;
- 0 Critical;
- 0 High;
- evidências atuais.

---

# Cheat sheet

```text
ASSESS → /corporate-context → /speckit.specify → /speckit.clarify
→ /speckit.plan → /plan-review → /speckit.checklist → /speckit.tasks
→ /speckit.analyze → /speckit.implement → /run-quality
→ /test-strategy-review → /adversarial-review → /speckit.converge
→ /spec-compliance → /corporate-compliance → /pre-review-gate
→ PR → @codex review → /post-review-rework → /code-ready
```
