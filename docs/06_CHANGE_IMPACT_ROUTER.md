# 06 — Change Impact Router

## Objetivo

Permitir iteração rápida em linguagem natural sem obrigar o Builder a reiniciar a esteira a cada ajuste.

## Classificação

### LOCAL / COSMETIC

Exemplos:

- spacing;
- alinhamento;
- labels/copy sem impacto de regra;
- layout;
- ordem visual;
- estilo usando Design System existente.

Fluxo:

```text
Change → Implement → Verify → Preview
```

Não precisa retornar à Spec/Plan, salvo se o pedido contradizer requisitos.

### BEHAVIORAL

Exemplos:

- validação;
- regra de negócio;
- fluxo funcional;
- tratamento de erro;
- permissão já dentro do modelo previsto.

Fluxo:

```text
Change → Compare with Spec
          ├─ already specified → Fix + Tests
          └─ new requirement   → Update Spec → Impact → Fix + Tests
```

### STRUCTURAL

Exemplos:

- nova integração;
- novo evento;
- mudança de modelo de dados relevante;
- nova tecnologia/dependência;
- alteração de autenticação/autorização;
- alteração de arquitetura;
- dado sensível novo;
- mudança de NFR/criticidade.

Fluxo mínimo:

```text
Change → Update Spec if needed → Update Plan → Relevant Plan Review
→ Update Tasks → Implement → Full affected gates
```

## Regra

O Builder pode pular etapas operacionais; o sistema não pode pular gates exigidos pelo impacto.
