# NEXUS — Contexto Completo do Projeto
> Cole este arquivo em qualquer IA (Cursor, Copilot, Claude, ChatGPT) para ela entender todo o projeto instantaneamente.

---

## O QUE É O NEXUS

Plataforma P2P de crédito direto (SCD) regulada pelo BACEN (CMN 5050/2022) que conecta:
- **Aplicantes** (investidores): aportam capital, recebem 3–5% a.m. via PIX D+1
- **Usuários** (tomadores): recebem crédito pré-aprovado em blocos de R$40 num cartão Visa pré-pago

Três pilares únicos:
1. **MACRO HASH**: cadeia SHA-256 de 5 camadas (L1→L5) — append-only, auditável publicamente
2. **IA Agentic**: workers Celery/Redis com fila FIFO para distribuição justa de crédito
3. **NEXUS Score**: score proprietário 0–1000, independente de bureaus externos

---

## DESIGN SYSTEM

```css
/* Cores */
--navy:    #0B2447   /* Principal escuro */
--primary: #1640D6   /* Azul primário */
--gold:    #D97706   /* Âmbar/dourado */
--success: #059669   /* Verde */
--light:   #FAFCFF   /* Fundo da plataforma */

/* Fontes */
Playfair Display → títulos/hero (font-display)
Poppins          → corpo/UI    (font-body)
Courier New      → hashes/mono (font-mono)
```

---

## ESTRUTURA DO PROJETO

```
nexus-platform/
├── website/               ← Site institucional (4 páginas HTML prontas)
│   ├── index.html         ← Landing page completa
│   ├── portfolios.html    ← Marketplace de portfólios
│   ├── como-funciona.html ← Explicação do produto
│   └── sobre.html         ← Sobre a empresa/tecnologia
├── platform/              ← Plataforma demo (EM CONSTRUÇÃO)
│   ├── index.html         ← Hub de navegação das telas
│   ├── shared/
│   │   ├── design-tokens.css  ← Todo o design system CSS
│   │   └── mock-data.js       ← Todos os dados de demonstração
│   └── screens/           ← Telas individuais (criar aqui)
│       ├── onboarding/    ← register.html, kyc.html
│       ├── dashboard-aplicante/  ← index.html, retornos.html
│       ├── dashboard-usuario/    ← index.html
│       ├── portfolios/    ← index.html, invest.html
│       ├── credito/       ← solicitar.html, parcelas.html
│       ├── cartao/        ← index.html
│       ├── score/         ← nexus-score.html
│       └── macro-hash/    ← index.html
└── docs/
    ├── NEXUS_DEF_v1.0.docx      ← Documento funcional completo
    └── nexus-openapi.yaml       ← API spec completa (OpenAPI 3.1)
```

---

## COMO MONTAR CADA TELA

Toda tela da plataforma usa esta estrutura base:

```html
<\!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="../../shared/design-tokens.css"/>
  <script src="../../shared/mock-data.js"></script>
</head>
<body>
  <div class="app-layout">
    <\!-- SIDEBAR -->
    <nav class="sidebar">
      <div class="sidebar-logo">
        <div class="nav-logo">
          <div class="logo-mark">NX</div>
          <span style="color:#fff;font-weight:700">NEXUS</span>
        </div>
      </div>
      <\!-- itens do menu -->
    </nav>
    <\!-- CONTEÚDO PRINCIPAL -->
    <main class="app-main">
      <div class="page-header">
        <div class="page-title">Título da Página</div>
        <div class="page-sub">Subtítulo descritivo</div>
      </div>
      <div class="page-content">
        <\!-- cards, tabelas, etc -->
      </div>
    </main>
  </div>
</body>
</html>
```

---

## NEXUS SCORE — MODELO PROPRIETÁRIO

Score 0–1000. Fórmula:
```
Score = (PagamentosNDia × 0.35) + (ComportamentoCartão × 0.25) +
        (DadosAlternativos × 0.20) + (Relacionamento × 0.12) + (BureauExterno × 0.08)
```

Faixas:
| Faixa     | Risco      | Status     | Limite/Solicitação |
|-----------|------------|------------|-------------------|
| 0–399     | Muito Alto | Bloqueado  | R$ 0              |
| 400–549   | Alto       | Restrito   | R$ 40 (1 bloco)   |
| 550–699   | Médio      | Monitorado | R$ 120 (3 blocos) |
| 700–849   | Baixo      | Aprovado   | R$ 280 (7 blocos) |
| 850–1000  | Muito Baixo| Premium    | R$ 400 (10 blocos)|

---

## MÓDULO DE CRÉDITO — FLUXO FIFO

1. Usuário solicita N blocos (1–10) × R$40 + vertical + parcelas
2. Inserido na fila Redis com timestamp (FIFO)
3. Worker Celery consome: revalida score, faz matching de portfólio
4. MACRO HASH L4 (Contract Block) gerado
5. Crédito carregado no cartão Visa via API Dock
6. MACRO HASH L5 (Block State) gerado por bloco
7. Notificação: push + email + SMS

Fórmula de parcela (Sistema Price):
```
PMT = PV × [i × (1+i)^n] / [(1+i)^n - 1]
PV = valor total (blocos × 40)
i  = taxa mensal do portfólio
n  = número de parcelas
```

---

## MACRO HASH — CADEIA L1→L5

| Nível | Nome            | Composição do Hash                              |
|-------|-----------------|------------------------------------------------|
| L1    | Platform State  | H(platform_id ∥ timestamp ∥ config_hash)       |
| L2    | Investor Block  | H(investor_id ∥ portfolio_id ∥ amount ∥ L1)    |
| L3    | Portfolio Block | H(portfolio_params ∥ allocation ∥ L2)           |
| L4    | Contract Block  | H(contract_id ∥ user_id ∥ terms ∥ L3)          |
| L5    | Block State     | H(block_id ∥ amount_40 ∥ card_token ∥ L4)      |

---

## PORTFÓLIOS

| Classe | Taxa Mensal   | Risco | Score Usuário |
|--------|---------------|-------|---------------|
| A      | 3,0% – 3,8%   | Baixo | ≥ 850         |
| B      | 3,9% – 4,5%   | Médio | ≥ 700         |
| C      | 4,6% – 5,0%   | Alto  | ≥ 550         |

Retorno (juros compostos):
```
Retorno_Bruto  = Principal × (1 + taxa)^n − Principal
IR_Retido      = Retorno_Bruto × alíquota_IR(n)
Retorno_Líquido = Retorno_Bruto − IR_Retido
```
IR regressivo: ≤180d=22,5% | 181–360d=20% | 361–720d=17,5% | >720d=15%

---

## 141 VERTICAIS DE CONSUMO (resumo)

V001–V018: Alimentação · V019–V032: Moradia · V033–V044: Transporte
V045–V058: Saúde · V059–V068: Educação · V069–V076: Vestuário
V077–V085: Beleza · V086–V097: Lazer · V098–V105: Tecnologia
V106–V111: Pet · V112–V117: Esporte · V118–V125: Serviços Lar
V126–V132: Financeiros · V133–V137: Social · V138–V141: Sustentabilidade

---

## INTEGRAÇÕES PRINCIPAIS

| Parceiro        | Para quê                                    |
|-----------------|---------------------------------------------|
| Dock / BS2      | BIN Sponsor Visa/MC, emissão e crédito cartão|
| PIX / BACEN     | Aportes, retornos D+1, amortizações         |
| Serasa Experian | Enriquecimento opcional do score (Bloco E)  |
| Open Finance    | Dados bancários para score (futuro)         |
| Twilio/SendGrid | SMS e emails transacionais                  |

---

## API ENDPOINTS PRINCIPAIS (OpenAPI 3.1)

```
POST /auth/register         → Cadastrar usuário (role: applicant | user)
POST /auth/login            → Login → JWT
POST /auth/kyc/documents    → Upload docs KYC

POST /score/check           → Consultar score (max 1×/semana)
POST /credit/request        → Solicitar crédito (entra na fila FIFO)
GET  /credit/requests       → Listar solicitações

GET  /portfolios            → Listar portfólios (público)
POST /portfolios/:id/simulate → Simular retorno
POST /investments           → Realizar aporte

GET  /ledger/verify/:hash   → Verificar integridade (público)
GET  /ledger/root           → Hash raiz do dia (público)

GET  /cards/me              → Dados do cartão Visa
GET  /cards/me/transactions → Extrato por vertical
```

---

## REGRAS DE NEGÓCIO CHAVE

- Bloco unitário: R$40 (indivisível)
- Máx. 10 blocos por solicitação (R$400)
- 1 solicitação ativa por usuário
- Aporte mínimo Aplicante: R$500
- Prazo investimento: 3/6/9/12 meses
- Retorno via PIX D+1 no 1º dia útil do mês
- Resgate antecipado: permitido após 60 dias (taxa saída 1%)
- Atraso ≥ 30 dias: cartão suspenso
- Hash raiz L1 publicado diariamente em /ledger/root

---

## ROADMAP — 7 CAMADAS

| Camada | Status | Entregável |
|--------|--------|-----------|
| 0 — Fundação Documental  | ✅ Pronto  | DEF, OpenAPI, Context |
| 1 — Captação             | 🔄 Próximo | Pitch deck, modelo financeiro |
| 2 — Spec Técnica         | 📋 Planejado | Schema DB, ADR |
| 3 — Protótipo Navegável  | 🔨 Em construção | Demo screens |
| 4 — Backend              | 📋 Planejado | FastAPI + Celery |
| 5 — Frontend             | 📋 Planejado | React + app mobile |
| 6 — QA/Deploy            | 📋 Planejado | Testes, BACEN, K8s |

---

## PRÓXIMAS TELAS A CRIAR (Camada 3)

1. `screens/onboarding/register.html` — formulário de cadastro com seletor de role
2. `screens/onboarding/kyc.html` — upload de docs, status de aprovação
3. `screens/dashboard-aplicante/index.html` — hub do investidor
4. `screens/portfolios/index.html` — marketplace com filtros
5. `screens/portfolios/invest.html` — fluxo de aporte com simulador e PIX
6. `screens/dashboard-usuario/index.html` — hub do tomador
7. `screens/credito/solicitar.html` — seleção de blocos + vertical + parcelas
8. `screens/cartao/index.html` — cartão Visa virtual + extrato
9. `screens/score/nexus-score.html` — score detalhado com gráfico
10. `screens/macro-hash/index.html` — explorador do ledger

Para criar cada tela: use o design-tokens.css, o mock-data.js, e o layout sidebar+main.
