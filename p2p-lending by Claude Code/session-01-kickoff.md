# Session 01 — Project Kickoff
**Data:** 2026-04-11

---

## O que foi decidido

- Projeto: plataforma fintech de empréstimos P2P
- Localização: `C:/LAPTOP/p2p-lending/`
- Base acadêmica: 26 papers clássicos de P2P lending incorporados ao CLAUDE.md

## Estrutura criada

```
C:/LAPTOP/p2p-lending/
├── CLAUDE.md                        ← regras de negócio + achados acadêmicos
├── docs/
│   ├── research/
│   │   └── bibliography.md          ← 26 referências bibliográficas
│   └── session-01-kickoff.md        ← este arquivo
└── src/
    ├── credit/
    ├── matching/
    ├── loans/
    ├── users/
    └── payments/
```

## Base acadêmica — 7 achados críticos para o produto

| # | Fonte | Achado | Decisão de produto |
|---|---|---|---|
| 1 | Iyer et al. (2009), Herzenstein et al. (2008) | Sinais narrativos ajudam lenders a inferir risco | Campo de narrativa obrigatório no pedido de empréstimo |
| 2 | Emekter et al. (2015) | Score de bureau é o melhor preditor de default | Motor de scoring via Serasa/SPC/Quod como base |
| 3 | Lin et al. (2012), Everett (2010) | Redes sociais verificáveis reduzem default | Sistema de "vouching" — endosso de outros usuários |
| 4 | Lee & Lee (2012), Chen (2012) | Efeito manada entre investidores distorce qualidade | Exibir métricas de risco ao lado de popularidade |
| 5 | Pope & Sydnor (2011), Ravina (2007) | Aparência/raça influencia decisão de crédito | Anonimizar perfis para lenders na fase de análise |
| 6 | Collier & Hampshire (2010) | Reputação incremental é o maior ativo do tomador | Score interno cresce com cada pagamento em dia |
| 7 | Berger & Gleisner (2009) | Plataformas ativas têm menos default que marketplaces puros | Curadoria ativa de scoring e precificação pela plataforma |

## Loan Status Flow definido

```
DRAFT → PENDING_ANALYSIS → APPROVED → FUNDING → ACTIVE →
  PAID_OFF | DEFAULTED | LATE_30 | LATE_60 | LATE_90+
```

## Inputs do modelo de scoring

- `score_bureau` — Serasa/SPC/Quod
- `renda_mensal`
- `divida_renda_ratio` (DTI)
- `historico_pagamentos_plataforma`
- `vouches_recebidos`
- `tempo_conta_ativo` (dias)
- `finalidade_emprestimo`
- `valor_solicitado`

## Pendente

- [ ] Definir stack (linguagem, framework, banco de dados)
- [ ] Definir se começa pelo backend/API ou pelo modelo de scoring
- [ ] Decidir sobre regulamentação brasileira (CMN 4.656/2018 — SEP)

---

## Contexto de memória

O Claude tem memória deste projeto salva em:
`C:/Users/mini/.claude/projects/C--Users-mini/memory/project_p2p_lending.md`

O `CLAUDE.md` em `C:/LAPTOP/p2p-lending/CLAUDE.md` é lido automaticamente em cada sessão nesta pasta.
