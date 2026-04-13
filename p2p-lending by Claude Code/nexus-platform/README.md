# NEXUS — P2P Credit Platform

> Plataforma de crédito direto (SCD/CMN 5050/2022) com MACRO HASH SHA-256, IA Agentic e Cartão Visa Pré-Pago.

## 🚀 Como começar no VSCode

1. Abra o arquivo `nexus-platform.code-workspace` no VSCode
2. Instale as extensões recomendadas (VSCode vai sugerir automaticamente)
3. Abra `platform/index.html` com **Live Server** para ver o hub de navegação

## 📁 Estrutura

| Pasta | Conteúdo |
|-------|---------|
| `website/` | Site institucional (4 páginas HTML prontas) |
| `platform/` | Plataforma demo — telas em construção |
| `platform/shared/` | Design tokens CSS + mock data JS |
| `platform/screens/` | Telas individuais (Camada 3) |
| `docs/` | DEF v1.0 (.docx) + OpenAPI (.yaml) |

## 🧠 Contexto completo do projeto

Cole o arquivo `NEXUS_CONTEXT.md` em qualquer IA (Cursor, Copilot, Claude) para ela entender **todo o projeto instantaneamente** — design system, regras de negócio, fluxos, fórmulas, 141 verticais, MACRO HASH, score model, tudo.

## 🎨 Design System

- **Cores**: `--navy #0B2447` · `--primary #1640D6` · `--gold #D97706`
- **Fontes**: Playfair Display (títulos) + Poppins (corpo)
- **Componentes**: `.card`, `.badge`, `.btn`, `.sidebar`, `.stat-card`, etc.
- Tudo no arquivo `platform/shared/design-tokens.css`

## 📊 Mock Data

Todos os dados de demonstração estão em `platform/shared/mock-data.js`:
- `NEXUS.applicant` — perfil do Aplicante logado
- `NEXUS.user` — perfil do Usuário logado
- `NEXUS.portfolios` — 5 portfólios A/B/C
- `NEXUS.investments` — aportes do Aplicante
- `NEXUS.credits` — solicitações de crédito
- `NEXUS.transactions` — extrato do cartão
- `NEXUS.ledger` — blocos MACRO HASH L1→L5
- `NEXUS.score_detail` — componentes e histórico do score
- `NEXUS.fmt.*` — helpers de formatação (BRL, %, datas)

## 🏗️ Roadmap (7 Camadas)

- **Camada 0** — Fundação Documental ✅
- **Camada 1** — Captação (Pitch + Financeiro) 🔄
- **Camada 2** — Spec Técnica (DB + ADR) 📋
- **Camada 3** — Protótipo Navegável 🔨 ← **AQUI AGORA**
- **Camada 4** — Backend (FastAPI + Celery) 📋
- **Camada 5** — Frontend (React + Mobile) 📋
- **Camada 6** — QA, Compliance, Deploy 📋

## 📌 Governanca tecnica (novo)

- `docs/ARCHITECTURE_CURRENT_VS_TARGET.md` — estado atual vs arquitetura alvo
- `docs/TECH_BACKLOG.md` — backlog tecnico priorizado (P0/P1/P2)
- `docs/EXECUTION_PLAN_30_60_90.md` — plano de execucao por fases
