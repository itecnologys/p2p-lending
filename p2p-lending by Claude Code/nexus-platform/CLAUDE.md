# P2P Lending Platform — Contexto do Projeto

## O que estamos construindo

Plataforma de empréstimos peer-to-peer (P2P) conectando investidores e tomadores diretamente,
sem intermediação bancária tradicional. Inspirado nas plataformas Prosper, LendingClub (EUA)
e regulamentado no Brasil pela Resolução CMN 4.656/2018 (SEP — Sociedade de Empréstimo entre Pessoas).

---

## Base Acadêmica: Achados Críticos para o Produto

### 1. Seleção Adversa e Sinalização de Qualidade
**Fonte:** Iyer et al. (2009), Herzenstein et al. (2008)

- Tomadores de alto risco tendem a se autoselecionar para plataformas P2P (adverse selection)
- Lenders individuais conseguem inferir risco além do score tradicional quando têm **sinais sociais e narrativos**
- **Implicação de produto:** O perfil do tomador deve incluir campos de narrativa/descrição do propósito do empréstimo. Não é frescura — reduz default.

### 2. Score de Crédito Tradicional Ainda Importa (Muito)
**Fonte:** Emekter et al. (2015)

- Variáveis tradicionais (FICO/Serasa score, DTI — debt-to-income ratio, histórico de inadimplência) são os melhores preditores de default em P2P
- Fatores "soft" (aparência, narrativa) têm efeito mas são secundários
- **Implicação de produto:** O motor de scoring deve ter como base dados bureaus (Serasa/SPC/Quod) + dados comportamentais internos.

### 3. Redes Sociais Reduzem Default
**Fonte:** Lin, Prabhala & Viswanathan (2012), Everett (2010)

- Tomadores com conexões sociais verificáveis (amigos que já pagaram empréstimos na plataforma) têm taxa de default significativamente menor
- Grupos com responsabilidade mútua (group lending) reduzem inadimplência
- **Implicação de produto:** Implementar sistema de "vouching" — usuários podem endossar tomadores. Endossos têm peso no scoring.

### 4. Efeito Manada (Herding) entre Investidores
**Fonte:** Lee & Lee (2012), Chen (2012), Shen et al. (2010)

- Investidores tendem a seguir outros investidores: empréstimos com mais funding atraem mais funding
- Isso pode inflar percepção de qualidade de empréstimos ruins
- **Implicação de produto:** Não exibir % de funding de forma que induza herding cego. Exibir métricas de risco ao lado da popularidade.

### 5. Discriminação e Bias em Decisões
**Fonte:** Pope & Sydnor (2011), Ravina (2007)

- Plataformas com fotos/características pessoais visíveis apresentam discriminação racial e por aparência
- Atratividade física influencia aprovação mesmo controlando por risco
- **Implicação de produto:** Minimizar dados pessoais visíveis antes da decisão de crédito. Anonymizar perfis para lenders na fase de análise.

### 6. Confiança e Reputação São Ativos
**Fonte:** Collier & Hampshire (2010), Chen et al. (2012)

- Reputação do tomador (histórico na plataforma) é um dos mais fortes preditores de sucesso
- Sinais mistos de reputação (bom histórico + comportamento errático) prejudicam mais que reputação ruim consistente
- **Implicação de produto:** Sistema de reputação incremental — cada pagamento em dia melhora score interno. Primeira linha de crédito deve ser pequena.

### 7. Papel dos Intermediários Eletrônicos
**Fonte:** Berger & Gleisner (2009), Frerichs & Schumann (2008)

- Plataformas P2P evoluem naturalmente de marketplaces puros para intermediários com papel ativo na precificação de risco
- A plataforma que só "apresenta" tomadores e lenders tende a ter mais default que a que faz curadoria ativa
- **Implicação de produto:** A plataforma deve ter papel ativo no scoring e na precificação da taxa, não apenas matching.

---

## Regras de Negócio Fundamentais

### Tomador (Borrower)
- KYC obrigatório: CPF, renda comprovada, score bureau
- Limite inicial conservador (ex: R$ 1.000 – R$ 5.000) — aumenta com histórico
- Taxa de juros definida pelo score: quanto melhor o perfil, menor a taxa
- Prazo: 3 a 36 meses
- Finalidade do empréstimo deve ser declarada

### Investidor (Lender)
- KYC obrigatório
- Diversificação obrigatória: máx. X% do portfólio em um único empréstimo
- Retorno esperado precificado pelo risco da carteira
- Recebe amortização + juros mensais

### Plataforma
- Taxa de originação cobrada do tomador (ex: 2–5% do valor)
- Taxa de administração cobrada do investidor (ex: 1% a.a. sobre saldo)
- Reserva de liquidez para atrasos

---

## Arquitetura de Dados Críticos

### Scoring Model (inputs)
```
- score_bureau: int          # Serasa/SPC/Quod
- renda_mensal: decimal
- divida_renda_ratio: decimal  # DTI
- historico_pagamentos_plataforma: int  # 0 se novo
- vouches_recebidos: int
- tempo_conta_ativo: int (dias)
- finalidade_emprestimo: enum
- valor_solicitado: decimal
```

### Loan Status Flow
```
DRAFT → PENDING_ANALYSIS → APPROVED → FUNDING → ACTIVE → 
  PAID_OFF | DEFAULTED | LATE_30 | LATE_60 | LATE_90+
```

---

## Stack Definida
> (a definir com o usuário)

---

## Referências Bibliográficas Completas
Ver `/docs/research/bibliography.md`
