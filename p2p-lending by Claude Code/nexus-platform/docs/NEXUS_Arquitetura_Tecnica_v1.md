---
title: "NEXUS — NEXUS_Arquitetura_Tecnica_v1"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>NEXUS</strong></p>
<p>Arquitetura Técnica do Sistema v1.0</p>
<p>FastAPI · PostgreSQL · Redis · Celery · Docker · Python 3.12</p>
<p>Confidencial — Uso Interno</p></td>
</tr>
</tbody>
</table>

> **1. Visão Geral da Arquitetura**

O NEXUS é uma plataforma P2P lending brasileira que conecta Aplicantes (investidores) a Usuários (tomadores de crédito via cartão pré-pago). A arquitetura foi projetada para alta disponibilidade, segurança financeira e rastreabilidade total de cada centavo via o sistema MACRO HASH.

**1.1 Decisão de Framework: FastAPI**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Critério</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FastAPI</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Django+DRF</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Flask</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Performance async</p>
</blockquote></td>
<td><blockquote>
<p>Nativo ASGI</p>
</blockquote></td>
<td><blockquote>
<p>WSGI (sync default)</p>
</blockquote></td>
<td><blockquote>
<p>WSGI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Validação de dados</p>
</blockquote></td>
<td><blockquote>
<p>Pydantic v2 nativo</p>
</blockquote></td>
<td><blockquote>
<p>Serializers DRF</p>
</blockquote></td>
<td><blockquote>
<p>Manual / Marshmallow</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OpenAPI auto</p>
</blockquote></td>
<td><blockquote>
<p>Swagger + ReDoc auto</p>
</blockquote></td>
<td><blockquote>
<p>drf-spectacular (extra)</p>
</blockquote></td>
<td><blockquote>
<p>Flask-RESTX (extra)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Segurança injeção</p>
</blockquote></td>
<td><blockquote>
<p>Pydantic bloqueia na entrada</p>
</blockquote></td>
<td><blockquote>
<p>Boa, manual</p>
</blockquote></td>
<td><blockquote>
<p>Manual</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Curva aprendizado</p>
</blockquote></td>
<td><blockquote>
<p>Média</p>
</blockquote></td>
<td><blockquote>
<p>Alta</p>
</blockquote></td>
<td><blockquote>
<p>Baixa</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSocket nativo</p>
</blockquote></td>
<td><blockquote>
<p>Sim (Starlette)</p>
</blockquote></td>
<td><blockquote>
<p>django-channels (extra)</p>
</blockquote></td>
<td><blockquote>
<p>flask-socketio (extra)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Adoção fintech BR</p>
</blockquote></td>
<td><blockquote>
<p>Alta — Nubank, iFood</p>
</blockquote></td>
<td><blockquote>
<p>Alta — projetos legados</p>
</blockquote></td>
<td><blockquote>
<p>Média</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recomendação NEXUS</p>
</blockquote></td>
<td><blockquote>
<p>ESCOLHIDO</p>
</blockquote></td>
<td><blockquote>
<p>Não</p>
</blockquote></td>
<td><blockquote>
<p>Não</p>
</blockquote></td>
</tr>
</tbody>
</table>

**1.2 Stack Tecnológica Completa**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Camada</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tecnologia</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Versão</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Função</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>API Framework</p>
</blockquote></td>
<td><blockquote>
<p>FastAPI</p>
</blockquote></td>
<td><blockquote>
<p>0.115+</p>
</blockquote></td>
<td><blockquote>
<p>Rotas HTTP/WebSocket, validação, OAuth2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Validação</p>
</blockquote></td>
<td><blockquote>
<p>Pydantic v2</p>
</blockquote></td>
<td><blockquote>
<p>2.x</p>
</blockquote></td>
<td><blockquote>
<p>Schemas de entrada/saída, prevenção de injection</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORM</p>
</blockquote></td>
<td><blockquote>
<p>SQLAlchemy async</p>
</blockquote></td>
<td><blockquote>
<p>2.x</p>
</blockquote></td>
<td><blockquote>
<p>Queries ao PostgreSQL, transactions, migrations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Banco principal</p>
</blockquote></td>
<td><blockquote>
<p>PostgreSQL</p>
</blockquote></td>
<td><blockquote>
<p>16+</p>
</blockquote></td>
<td><blockquote>
<p>Dados transacionais, ledger, contratos</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cache / Sessions</p>
</blockquote></td>
<td><blockquote>
<p>Redis</p>
</blockquote></td>
<td><blockquote>
<p>7+</p>
</blockquote></td>
<td><blockquote>
<p>Cache de KPIs, sessões JWT, rate limiting</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Filas / Background</p>
</blockquote></td>
<td><blockquote>
<p>Celery + Redis broker</p>
</blockquote></td>
<td><blockquote>
<p>5.x</p>
</blockquote></td>
<td><blockquote>
<p>Jobs do Agentic AI, notificações, relatórios</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Migrations</p>
</blockquote></td>
<td><blockquote>
<p>Alembic</p>
</blockquote></td>
<td><blockquote>
<p>1.x</p>
</blockquote></td>
<td><blockquote>
<p>Versionamento de schema do banco</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Auth</p>
</blockquote></td>
<td><blockquote>
<p>python-jose + passlib</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>JWT tokens, bcrypt password hashing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HTTP Client</p>
</blockquote></td>
<td><blockquote>
<p>httpx (async)</p>
</blockquote></td>
<td><blockquote>
<p>0.27+</p>
</blockquote></td>
<td><blockquote>
<p>Integração com subadquirente, PIX, Open Finance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Task scheduling</p>
</blockquote></td>
<td><blockquote>
<p>Celery Beat</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Jobs recorrentes: cobrança, relatórios, score</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Monitoramento</p>
</blockquote></td>
<td><blockquote>
<p>Prometheus + Grafana</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Métricas de latência, erros, filas</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Logging</p>
</blockquote></td>
<td><blockquote>
<p>structlog + JSON</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Logs estruturados para auditoria BACEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Testes</p>
</blockquote></td>
<td><blockquote>
<p>pytest-asyncio + httpx</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Testes unitários e de integração async</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Containerização</p>
</blockquote></td>
<td><blockquote>
<p>Docker + Docker Compose</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Deploy local e produção</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CI/CD</p>
</blockquote></td>
<td><blockquote>
<p>GitHub Actions</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Lint, testes, deploy automático</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Segredos</p>
</blockquote></td>
<td><blockquote>
<p>python-decouple + Vault</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>Variáveis de ambiente, secrets em produção</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **2. Diagrama de Camadas do Sistema**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Arquitetura em 5 Camadas (de fora para dentro)</strong></p>
<p>┌─────────────────────────────────────────────────────────────────┐</p>
<p>│ CAMADA 1 — CLIENTES (Frontend / Mobile / Parceiros) │</p>
<p>│ React 18 PWA | App Mobile (React Native) | APIs parceiros │</p>
<p>├─────────────────────────────────────────────────────────────────┤</p>
<p>│ CAMADA 2 — API GATEWAY │</p>
<p>│ Nginx (reverse proxy, SSL termination, rate limiting) │</p>
<p>│ + WAF (Web Application Firewall) │</p>
<p>├─────────────────────────────────────────────────────────────────┤</p>
<p>│ CAMADA 3 — APPLICATION SERVERS (FastAPI) │</p>
<p>│ Auth Service | Credit Service | Ledger Service │</p>
<p>│ Card Service | AE Service | BI/Report Service │</p>
<p>├─────────────────────────────────────────────────────────────────┤</p>
<p>│ CAMADA 4 — DATA &amp; MESSAGING │</p>
<p>│ PostgreSQL (primário + réplica leitura) │</p>
<p>│ Redis (cache, sessions, Celery broker) │</p>
<p>│ Celery Workers (Agentic AI, cobrança, notificações) │</p>
<p>├─────────────────────────────────────────────────────────────────┤</p>
<p>│ CAMADA 5 — INTEGRAÇÕES EXTERNAS │</p>
<p>│ Subadquirente (Dock/BS2) | PIX (BACEN) | Open Finance │</p>
<p>│ ODOO ERP | KYC/AML | Email/SMS | BI Tools │</p>
<p>└─────────────────────────────────────────────────────────────────┘</p>
</blockquote></td>
</tr>
</tbody>
</table>

**2.1 Estrutura de Microsserviços Python**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Serviço</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Arquivo principal</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Responsabilidade</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Porta</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>auth_service</p>
</blockquote></td>
<td><blockquote>
<p>app/auth/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Login, JWT, refresh tokens, OAuth2</p>
</blockquote></td>
<td><blockquote>
<p>8001</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>credit_service</p>
</blockquote></td>
<td><blockquote>
<p>app/credit/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Análise de crédito, score, aprovação</p>
</blockquote></td>
<td><blockquote>
<p>8002</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ledger_service</p>
</blockquote></td>
<td><blockquote>
<p>app/ledger/router.py</p>
</blockquote></td>
<td><blockquote>
<p>MACRO HASH, eventos, audit trail</p>
</blockquote></td>
<td><blockquote>
<p>8003</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>card_service</p>
</blockquote></td>
<td><blockquote>
<p>app/card/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Subadquirente, transações, fatura</p>
</blockquote></td>
<td><blockquote>
<p>8004</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>portfolio_service</p>
</blockquote></td>
<td><blockquote>
<p>app/portfolio/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Portfólios, contratos, distribuição AI</p>
</blockquote></td>
<td><blockquote>
<p>8005</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ae_service</p>
</blockquote></td>
<td><blockquote>
<p>app/ae/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Account Executives, metas, comissão</p>
</blockquote></td>
<td><blockquote>
<p>8006</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>report_service</p>
</blockquote></td>
<td><blockquote>
<p>app/report/router.py</p>
</blockquote></td>
<td><blockquote>
<p>BI, exportação, Power BI, Superset</p>
</blockquote></td>
<td><blockquote>
<p>8007</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>webhook_service</p>
</blockquote></td>
<td><blockquote>
<p>app/webhook/router.py</p>
</blockquote></td>
<td><blockquote>
<p>Callbacks subadquirente, PIX, notificações</p>
</blockquote></td>
<td><blockquote>
<p>8008</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **3. Estrutura de Diretórios do Projeto Python**

**Estrutura de diretórios — nexus-backend/**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>nexus-backend/</p>
<p>├── app/</p>
<p>│ ├── main.py # FastAPI app factory, middlewares, routers</p>
<p>│ ├── config.py # Settings via pydantic-settings + .env</p>
<p>│ ├── database.py # SQLAlchemy async engine + session factory</p>
<p>│ ├── dependencies.py # FastAPI Depends() reutilizáveis</p>
<p>│ │</p>
<p>│ ├── auth/</p>
<p>│ │ ├── router.py # POST /auth/login, /auth/refresh, /auth/logout</p>
<p>│ │ ├── schemas.py # Pydantic: LoginRequest, TokenResponse</p>
<p>│ │ ├── service.py # Lógica: verify_password, create_token</p>
<p>│ │ └── models.py # SQLAlchemy: User, Role, Session</p>
<p>│ │</p>
<p>│ ├── credit/</p>
<p>│ │ ├── router.py # POST /credit/apply, GET /credit/score/{cpf}</p>
<p>│ │ ├── schemas.py # Pydantic: CreditApplication, ScoreResponse</p>
<p>│ │ ├── service.py # Motor de scoring, regras de aprovação</p>
<p>│ │ ├── models.py # SQLAlchemy: CreditApplication, Score</p>
<p>│ │ └── scoring/</p>
<p>│ │ ├── engine.py # Algoritmo de score (RF / XGBoost)</p>
<p>│ │ └── features.py # Feature engineering para o modelo</p>
<p>│ │</p>
<p>│ ├── ledger/</p>
<p>│ │ ├── router.py # GET /ledger/hash/{hash}, GET /ledger/events</p>
<p>│ │ ├── schemas.py # Pydantic: LedgerEvent, HashChain</p>
<p>│ │ ├── service.py # MACRO HASH engine, geração de hashes</p>
<p>│ │ └── models.py # SQLAlchemy: LedgerEvent, HashChain</p>
<p>│ │</p>
<p>│ ├── portfolio/</p>
<p>│ │ ├── router.py # CRUD /portfolio, /portfolio/{id}/contracts</p>
<p>│ │ ├── schemas.py # Pydantic: Portfolio, Contract, Block</p>
<p>│ │ ├── service.py # Fracionamento de capital, alocação AI</p>
<p>│ │ └── models.py # SQLAlchemy: Portfolio, Contract, Block</p>
<p>│ │</p>
<p>│ ├── card/</p>
<p>│ │ ├── router.py # /card/issue, /card/transactions, /card/invoice</p>
<p>│ │ ├── schemas.py # Pydantic: CardIssue, Transaction, Invoice</p>
<p>│ │ ├── service.py # Integração subadquirente, fatura</p>
<p>│ │ └── models.py # SQLAlchemy: Card, Transaction, Invoice</p>
<p>│ │</p>
<p>│ ├── ae/</p>
<p>│ │ ├── router.py # /ae/dashboard, /ae/territory, /ae/commission</p>
<p>│ │ ├── schemas.py # Pydantic: AEProfile, Territory, Commission</p>
<p>│ │ ├── service.py # Cálculo de comissão, metas, ranking</p>
<p>│ │ └── models.py # SQLAlchemy: AccountExecutive, Territory</p>
<p>│ │</p>
<p>│ └── shared/</p>
<p>│ ├── security.py # JWT, bcrypt, OAuth2PasswordBearer</p>
<p>│ ├── middleware.py # Rate limiting, request ID, logging</p>
<p>│ ├── exceptions.py # HTTPExceptions customizadas NEXUS</p>
<p>│ └── utils.py # CPF/CNPJ validation, formatters</p>
<p>│</p>
<p>├── workers/</p>
<p>│ ├── celery_app.py # Celery app factory + Beat scheduler</p>
<p>│ ├── agentic_ai.py # Worker: distribuição de blocos de crédito</p>
<p>│ ├── billing.py # Worker: geração de faturas, cobrança</p>
<p>│ ├── notifications.py # Worker: email, SMS, push</p>
<p>│ └── reports.py # Worker: geração de relatórios BI</p>
<p>│</p>
<p>├── alembic/</p>
<p>│ ├── env.py # Config async do Alembic</p>
<p>│ └── versions/ # Migrations versionadas</p>
<p>│</p>
<p>├── tests/</p>
<p>│ ├── conftest.py # Fixtures: async client, test DB</p>
<p>│ ├── test_auth.py</p>
<p>│ ├── test_credit.py</p>
<p>│ ├── test_ledger.py</p>
<p>│ └── test_portfolio.py</p>
<p>│</p>
<p>├── docker/</p>
<p>│ ├── Dockerfile # Multi-stage build Python 3.12-slim</p>
<p>│ └── docker-compose.yml # App + PostgreSQL + Redis + Celery</p>
<p>│</p>
<p>├── .env.example # Template de variáveis de ambiente</p>
<p>├── requirements.txt # Dependências de produção</p>
<p>├── requirements-dev.txt # pytest, black, ruff, mypy</p>
<p>└── pyproject.toml # black, ruff, mypy config</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **4. Configuração e Segurança**

**4.1 app/config.py — Settings com Pydantic**

**app/config.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>from pydantic_settings import BaseSettings</p>
<p>from pydantic import PostgresDsn, RedisDsn, SecretStr</p>
<p>class Settings(BaseSettings):</p>
<p># App</p>
<p>APP_NAME: str = 'NEXUS API'</p>
<p>DEBUG: bool = False</p>
<p>API_V1_PREFIX: str = '/api/v1'</p>
<p># Security</p>
<p>SECRET_KEY: SecretStr # bcrypt/JWT signing key</p>
<p>ACCESS_TOKEN_EXPIRE_MINUTES: int = 30</p>
<p>REFRESH_TOKEN_EXPIRE_DAYS: int = 7</p>
<p>ALGORITHM: str = 'HS256'</p>
<p>ALLOWED_HOSTS: list[str] = ['nexus.com.br', 'app.nexus.com.br']</p>
<p>CORS_ORIGINS: list[str] = []</p>
<p># Database</p>
<p>DATABASE_URL: PostgresDsn # postgresql+asyncpg://user:pass@host/db</p>
<p>DB_POOL_SIZE: int = 20</p>
<p>DB_MAX_OVERFLOW: int = 40</p>
<p># Redis</p>
<p>REDIS_URL: RedisDsn # redis://host:6379/0</p>
<p>CACHE_TTL_SECONDS: int = 300</p>
<p># Celery</p>
<p>CELERY_BROKER_URL: str # redis://host:6379/1</p>
<p>CELERY_RESULT_BACKEND: str # redis://host:6379/2</p>
<p># Subadquirente (Dock / BS2)</p>
<p>SUBACQUIRER_API_URL: str</p>
<p>SUBACQUIRER_API_KEY: SecretStr</p>
<p>SUBACQUIRER_WEBHOOK_SECRET: SecretStr</p>
<p># PIX / Open Finance</p>
<p>PIX_API_URL: str</p>
<p>PIX_CLIENT_ID: str</p>
<p>PIX_CLIENT_SECRET: SecretStr</p>
<p># ODOO ERP</p>
<p>ODOO_URL: str</p>
<p>ODOO_DB: str</p>
<p>ODOO_API_KEY: SecretStr</p>
<p>class Config:</p>
<p>env_file = '.env'</p>
<p>case_sensitive = True</p>
<p>settings = Settings()</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.2 app/main.py — FastAPI App com Middlewares de Segurança**

**app/main.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>from fastapi import FastAPI</p>
<p>from fastapi.middleware.cors import CORSMiddleware</p>
<p>from fastapi.middleware.trustedhost import TrustedHostMiddleware</p>
<p>from slowapi import Limiter, _rate_limit_exceeded_handler</p>
<p>from slowapi.util import get_remote_address</p>
<p>from slowapi.errors import RateLimitExceeded</p>
<p>import structlog</p>
<p>from app.config import settings</p>
<p>from app.shared.middleware import RequestIDMiddleware, AuditLogMiddleware</p>
<p>from app.auth.router import router as auth_router</p>
<p>from app.credit.router import router as credit_router</p>
<p>from app.ledger.router import router as ledger_router</p>
<p>from app.portfolio.router import router as portfolio_router</p>
<p>from app.card.router import router as card_router</p>
<p>limiter = Limiter(key_func=get_remote_address)</p>
<p>def create_app() -&gt; FastAPI:</p>
<p>app = FastAPI(</p>
<p>title='NEXUS API',</p>
<p>version='1.0.0',</p>
<p>docs_url='/api/docs', # Swagger UI</p>
<p>redoc_url='/api/redoc', # ReDoc</p>
<p>openapi_url='/api/openapi.json',</p>
<p>)</p>
<p># Rate limiting — bloqueia ataques de força bruta</p>
<p>app.state.limiter = limiter</p>
<p>app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)</p>
<p># Segurança de hosts</p>
<p>app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)</p>
<p># CORS</p>
<p>app.add_middleware(CORSMiddleware,</p>
<p>allow_origins=settings.CORS_ORIGINS,</p>
<p>allow_methods=['GET','POST','PUT','PATCH','DELETE'],</p>
<p>allow_headers=['Authorization','Content-Type','X-Request-ID'],</p>
<p>allow_credentials=True,</p>
<p>)</p>
<p># Request ID + Audit Log (obrigatório para compliance BACEN)</p>
<p>app.add_middleware(RequestIDMiddleware)</p>
<p>app.add_middleware(AuditLogMiddleware)</p>
<p># Routers</p>
<p>prefix = settings.API_V1_PREFIX</p>
<p>app.include_router(auth_router, prefix=f'{prefix}/auth')</p>
<p>app.include_router(credit_router, prefix=f'{prefix}/credit')</p>
<p>app.include_router(ledger_router, prefix=f'{prefix}/ledger')</p>
<p>app.include_router(portfolio_router, prefix=f'{prefix}/portfolio')</p>
<p>app.include_router(card_router, prefix=f'{prefix}/card')</p>
<p>return app</p>
<p>app = create_app()</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.3 Camadas de Segurança**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Camada</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mecanismo</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Implementação Python</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Ameaça Bloqueada</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Entrada de dados</p>
</blockquote></td>
<td><blockquote>
<p>Pydantic v2 strict mode</p>
</blockquote></td>
<td><blockquote>
<p>BaseModel + Field validators</p>
</blockquote></td>
<td><blockquote>
<p>SQL injection, XSS, type coercion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Autenticação</p>
</blockquote></td>
<td><blockquote>
<p>OAuth2 + JWT RS256</p>
</blockquote></td>
<td><blockquote>
<p>python-jose + fastapi.security</p>
</blockquote></td>
<td><blockquote>
<p>Session hijacking, CSRF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Senha</p>
</blockquote></td>
<td><blockquote>
<p>bcrypt (cost=12)</p>
</blockquote></td>
<td><blockquote>
<p>passlib[bcrypt]</p>
</blockquote></td>
<td><blockquote>
<p>Brute force, rainbow tables</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rate Limiting</p>
</blockquote></td>
<td><blockquote>
<p>slowapi (Redis backend)</p>
</blockquote></td>
<td><blockquote>
<p>limiter.limit('100/minute')</p>
</blockquote></td>
<td><blockquote>
<p>DDoS, força bruta, scraping</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CORS</p>
</blockquote></td>
<td><blockquote>
<p>Whitelist de origens</p>
</blockquote></td>
<td><blockquote>
<p>CORSMiddleware</p>
</blockquote></td>
<td><blockquote>
<p>Cross-origin attacks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hosts</p>
</blockquote></td>
<td><blockquote>
<p>TrustedHostMiddleware</p>
</blockquote></td>
<td><blockquote>
<p>ALLOWED_HOSTS config</p>
</blockquote></td>
<td><blockquote>
<p>Host header injection</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQL</p>
</blockquote></td>
<td><blockquote>
<p>SQLAlchemy ORM (paramétrico)</p>
</blockquote></td>
<td><blockquote>
<p>Nunca string SQL raw</p>
</blockquote></td>
<td><blockquote>
<p>SQL injection</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Segredos</p>
</blockquote></td>
<td><blockquote>
<p>pydantic SecretStr + .env</p>
</blockquote></td>
<td><blockquote>
<p>Nunca logar SecretStr</p>
</blockquote></td>
<td><blockquote>
<p>Credential leakage em logs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Auditoria</p>
</blockquote></td>
<td><blockquote>
<p>structlog JSON + Request ID</p>
</blockquote></td>
<td><blockquote>
<p>AuditLogMiddleware</p>
</blockquote></td>
<td><blockquote>
<p>Não repúdio, compliance BACEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TLS</p>
</blockquote></td>
<td><blockquote>
<p>Nginx + Let's Encrypt</p>
</blockquote></td>
<td><blockquote>
<p>SSL termination no gateway</p>
</blockquote></td>
<td><blockquote>
<p>Man-in-the-middle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Webhooks</p>
</blockquote></td>
<td><blockquote>
<p>HMAC-SHA256 signature verify</p>
</blockquote></td>
<td><blockquote>
<p>hmac.compare_digest()</p>
</blockquote></td>
<td><blockquote>
<p>Webhook spoofing (subadquirente)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **5. Banco de Dados — Schema PostgreSQL**

**5.1 Modelo de Entidades Principal**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Hierarquia de Entidades NEXUS</strong></p>
<p>Platform (1) ──&gt; Investor/Aplicante (N)</p>
<p>Investor (1) ──&gt; Portfolio (N)</p>
<p>Portfolio (1) ──&gt; Contract / Micro-contrato (N) [até 1.800]</p>
<p>Contract (1) ──&gt; Block (N) [blocos de crédito R$40 cada]</p>
<p>Contract (1) ──&gt; CardTransaction (N)</p>
<p>Contract (1) ──&gt; LedgerEvent (N) [MACRO HASH trail]</p>
<p>User/Usuário (1) ──&gt; Contract (N) [em diferentes portfólios]</p>
<p>User (1) ──&gt; Card (1) [cartão pré-pago Visa/MC]</p>
<p>AccountExecutive (1) ──&gt; Territory (N)</p>
<p>Territory (1) ──&gt; User (N)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**5.2 Tabelas Principais — SQLAlchemy Models**

**app/portfolio/models.py (trecho)**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># app/auth/models.py</p>
<p>class User(Base):</p>
<p>__tablename__ = 'users'</p>
<p>id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)</p>
<p>cpf: Mapped[str] = mapped_column(String(11), unique=True, index=True)</p>
<p>email: Mapped[str] = mapped_column(String(255), unique=True)</p>
<p>hashed_password: Mapped[str] = mapped_column(String(255))</p>
<p>role: Mapped[str] = mapped_column(Enum('USER','INVESTOR','AE','ADMIN','BOARD'))</p>
<p>kyc_status: Mapped[str] = mapped_column(Enum('PENDING','APPROVED','REJECTED'))</p>
<p>is_active: Mapped[bool] = mapped_column(default=True)</p>
<p>created_at: Mapped[datetime] = mapped_column(server_default=func.now())</p>
<p>updated_at: Mapped[datetime] = mapped_column(onupdate=func.now())</p>
<p># app/portfolio/models.py</p>
<p>class Portfolio(Base):</p>
<p>__tablename__ = 'portfolios'</p>
<p>id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)</p>
<p>investor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), index=True)</p>
<p>name: Mapped[str] = mapped_column(String(100))</p>
<p>category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))</p>
<p>aum: Mapped[Decimal] = mapped_column(Numeric(15,2)) # Assets Under Management</p>
<p>target_return_pct: Mapped[Decimal] = mapped_column(Numeric(5,4))</p>
<p>max_contracts: Mapped[int] = mapped_column(default=1800)</p>
<p>status: Mapped[str] = mapped_column(Enum('ACTIVE','PAUSED','LIQUIDATING','CLOSED'))</p>
<p>platform_hash: Mapped[str] = mapped_column(String(64), unique=True) # MACRO HASH L1</p>
<p>investor_hash: Mapped[str] = mapped_column(String(64), unique=True) # MACRO HASH L2</p>
<p>portfolio_hash: Mapped[str] = mapped_column(String(64), unique=True) # MACRO HASH L3</p>
<p>class Contract(Base):</p>
<p>__tablename__ = 'contracts'</p>
<p>id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)</p>
<p>portfolio_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('portfolios.id'), index=True)</p>
<p>user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'), index=True)</p>
<p>credit_limit: Mapped[Decimal] = mapped_column(Numeric(10,2)) # R$500–R$2.500</p>
<p>current_balance: Mapped[Decimal] = mapped_column(Numeric(10,2), default=0)</p>
<p>fee_pct: Mapped[Decimal] = mapped_column(Numeric(5,4), default=Decimal('0.06')) # 6%</p>
<p>status: Mapped[str] = mapped_column(Enum('ACTIVE','OVERDUE','LIQUIDATED','BLOCKED'))</p>
<p>contract_hash: Mapped[str] = mapped_column(String(64), unique=True) # MACRO HASH L4</p>
<p>due_date: Mapped[date]</p>
<p>issued_at: Mapped[datetime] = mapped_column(server_default=func.now())</p>
<p>class LedgerEvent(Base):</p>
<p>__tablename__ = 'ledger_events'</p>
<p>id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)</p>
<p>contract_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('contracts.id'), index=True)</p>
<p>event_type: Mapped[str] = mapped_column(Enum(</p>
<p>'EMISSAO','USO','COBRANCA','PAGAMENTO','BLOQUEIO','LIQUIDACAO','AJUSTE'))</p>
<p>amount: Mapped[Decimal] = mapped_column(Numeric(15,2))</p>
<p>block_state_hash: Mapped[str] = mapped_column(String(64)) # SHA256 do estado</p>
<p>prev_hash: Mapped[str] = mapped_column(String(64)) # hash anterior (chain)</p>
<p>payload: Mapped[dict] = mapped_column(JSONB) # dados completos do evento</p>
<p>ts: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)</p>
<p># Imutável: nunca update, nunca delete — append-only ledger</p>
</blockquote></td>
</tr>
</tbody>
</table>

**5.3 Tabela de Categorias de Consumo (12 Verticais)**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Categoria</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Risco</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Taxa Base</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Exemplos</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>01</p>
</blockquote></td>
<td><blockquote>
<p>Saúde</p>
</blockquote></td>
<td><blockquote>
<p>Baixo</p>
</blockquote></td>
<td><blockquote>
<p>5.2% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Farmácias, clínicas, planos</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02</p>
</blockquote></td>
<td><blockquote>
<p>Educação</p>
</blockquote></td>
<td><blockquote>
<p>Baixo</p>
</blockquote></td>
<td><blockquote>
<p>4.8% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Cursos, material, faculdade</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03</p>
</blockquote></td>
<td><blockquote>
<p>Alimentação</p>
</blockquote></td>
<td><blockquote>
<p>Médio</p>
</blockquote></td>
<td><blockquote>
<p>6.1% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Supermercados, restaurantes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04</p>
</blockquote></td>
<td><blockquote>
<p>Transporte</p>
</blockquote></td>
<td><blockquote>
<p>Baixo</p>
</blockquote></td>
<td><blockquote>
<p>5.5% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Combustível, Uber, passagens</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05</p>
</blockquote></td>
<td><blockquote>
<p>Utilidades</p>
</blockquote></td>
<td><blockquote>
<p>Baixo</p>
</blockquote></td>
<td><blockquote>
<p>5.0% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Contas de luz, água, gás</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06</p>
</blockquote></td>
<td><blockquote>
<p>Vestuário</p>
</blockquote></td>
<td><blockquote>
<p>Médio</p>
</blockquote></td>
<td><blockquote>
<p>6.4% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Roupas, calçados, acessórios</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07</p>
</blockquote></td>
<td><blockquote>
<p>Tecnologia</p>
</blockquote></td>
<td><blockquote>
<p>Médio</p>
</blockquote></td>
<td><blockquote>
<p>6.8% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Celular, eletrônicos, TI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08</p>
</blockquote></td>
<td><blockquote>
<p>Casa e Móveis</p>
</blockquote></td>
<td><blockquote>
<p>Alto</p>
</blockquote></td>
<td><blockquote>
<p>7.2% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Móveis, eletrodomésticos</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09</p>
</blockquote></td>
<td><blockquote>
<p>Lazer</p>
</blockquote></td>
<td><blockquote>
<p>Alto</p>
</blockquote></td>
<td><blockquote>
<p>7.5% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Viagens, shows, academia</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Serviços Pes.</p>
</blockquote></td>
<td><blockquote>
<p>Médio</p>
</blockquote></td>
<td><blockquote>
<p>6.2% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Salão, pet shop, estética</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Agro/Rural</p>
</blockquote></td>
<td><blockquote>
<p>Baixo</p>
</blockquote></td>
<td><blockquote>
<p>5.8% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Insumos, ferramentas rurais</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>B2B Micro</p>
</blockquote></td>
<td><blockquote>
<p>Médio</p>
</blockquote></td>
<td><blockquote>
<p>6.6% a.m.</p>
</blockquote></td>
<td><blockquote>
<p>Suprimentos para MEI</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **6. Sistema MACRO HASH — Ledger Imutável**

O MACRO HASH é o coração da rastreabilidade do NEXUS. Toda movimentação financeira gera um hash encadeado (blockchain-like), garantindo que nenhum centavo seja alterado retroativamente. Essencial para auditoria BACEN e compliance CMN 5050/2022.

**6.1 Hierarquia de Hashes**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Nível</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Nome</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Composição do Hash</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Escopo</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>L1</p>
</blockquote></td>
<td><blockquote>
<p>Platform Hash</p>
</blockquote></td>
<td><blockquote>
<p>SHA256(platform_id + timestamp + salt)</p>
</blockquote></td>
<td><blockquote>
<p>Hash raiz da plataforma</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>L2</p>
</blockquote></td>
<td><blockquote>
<p>Investor Hash</p>
</blockquote></td>
<td><blockquote>
<p>SHA256(L1 + investor_id + aum + timestamp)</p>
</blockquote></td>
<td><blockquote>
<p>Por Aplicante</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L3</p>
</blockquote></td>
<td><blockquote>
<p>Portfolio Hash</p>
</blockquote></td>
<td><blockquote>
<p>SHA256(L2 + portfolio_id + categoria + max_contracts)</p>
</blockquote></td>
<td><blockquote>
<p>Por portfólio</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>L4</p>
</blockquote></td>
<td><blockquote>
<p>Contract Hash</p>
</blockquote></td>
<td><blockquote>
<p>SHA256(L3 + contract_id + user_cpf + credit_limit)</p>
</blockquote></td>
<td><blockquote>
<p>Por micro-contrato</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L5</p>
</blockquote></td>
<td><blockquote>
<p>Block State Hash</p>
</blockquote></td>
<td><blockquote>
<p>SHA256(L4 + prev_hash + event_type + amount + timestamp)</p>
</blockquote></td>
<td><blockquote>
<p>Por evento/transação</p>
</blockquote></td>
</tr>
</tbody>
</table>

**6.2 Implementação Python — app/ledger/service.py**

**app/ledger/service.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>import hashlib, json</p>
<p>from datetime import datetime, timezone</p>
<p>from decimal import Decimal</p>
<p>from sqlalchemy.ext.asyncio import AsyncSession</p>
<p>from app.ledger.models import LedgerEvent</p>
<p>from app.config import settings</p>
<p>class MacroHashService:</p>
<p>@staticmethod</p>
<p>def _sha256(data: dict) -&gt; str:</p>
<p>payload = json.dumps(data, sort_keys=True, default=str)</p>
<p>return hashlib.sha256(payload.encode()).hexdigest()</p>
<p>@classmethod</p>
<p>def generate_platform_hash(cls) -&gt; str:</p>
<p>return cls._sha256({</p>
<p>'platform': 'NEXUS',</p>
<p>'ts': datetime.now(timezone.utc).isoformat(),</p>
<p>'salt': settings.SECRET_KEY.get_secret_value()[:8]</p>
<p>})</p>
<p>@classmethod</p>
<p>def generate_contract_hash(cls, portfolio_hash: str,</p>
<p>contract_id: str, cpf_hash: str,</p>
<p>credit_limit: Decimal) -&gt; str:</p>
<p>return cls._sha256({</p>
<p>'parent': portfolio_hash,</p>
<p>'contract_id': contract_id,</p>
<p>'cpf_hash': cpf_hash, # CPF nunca em plain text no hash</p>
<p>'limit': str(credit_limit),</p>
<p>})</p>
<p>@classmethod</p>
<p>async def record_event(</p>
<p>cls, db: AsyncSession,</p>
<p>contract_id: str,</p>
<p>event_type: str,</p>
<p>amount: Decimal,</p>
<p>payload: dict,</p>
<p>prev_hash: str,</p>
<p>contract_hash: str,</p>
<p>) -&gt; LedgerEvent:</p>
<p>block_state = cls._sha256({</p>
<p>'parent': contract_hash,</p>
<p>'prev_hash': prev_hash,</p>
<p>'event_type': event_type,</p>
<p>'amount': str(amount),</p>
<p>'ts': datetime.now(timezone.utc).isoformat(),</p>
<p>})</p>
<p>event = LedgerEvent(</p>
<p>contract_id=contract_id,</p>
<p>event_type=event_type,</p>
<p>amount=amount,</p>
<p>block_state_hash=block_state,</p>
<p>prev_hash=prev_hash,</p>
<p>payload=payload,</p>
<p>)</p>
<p>db.add(event)</p>
<p>await db.commit() # commit imediato — append-only, nunca rollback de ledger</p>
<p>return event</p>
<p>@classmethod</p>
<p>async def verify_chain(cls, db: AsyncSession, contract_id: str) -&gt; bool:</p>
<p>'''Verifica integridade da cadeia de hashes de um contrato'''</p>
<p>events = await db.execute(</p>
<p>select(LedgerEvent).where(LedgerEvent.contract_id == contract_id)</p>
<p>.order_by(LedgerEvent.ts.asc())</p>
<p>)</p>
<p>prev = None</p>
<p>for event in events.scalars():</p>
<p>if prev and event.prev_hash != prev.block_state_hash:</p>
<p>return False # cadeia quebrada — alerta de fraude</p>
<p>prev = event</p>
<p>return True</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **7. Agentic AI — Motor de Distribuição de Crédito**

O Agentic AI é o cérebro operacional do NEXUS. Roda como worker Celery em background, distribuindo blocos de crédito (R$40 cada) entre usuários elegíveis de forma automática, usando lógica FIFO e regras de risco por categoria.

**7.1 Arquitetura do Agente**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Fluxo do Agentic AI (Celery Worker)</strong></p>
<p>1. TRIGGER: Novo aporte de Aplicante confirmado via webhook PIX</p>
<p>2. CALCULO: capital / R$40 = N blocos disponíveis por portfólio</p>
<p>3. SELEÇÃO: Query FIFO — usuários elegíveis por categoria, ordenados por score desc</p>
<p>4. DISTRIBUIÇÃO: Aloca blocos a contratos ativos (máx 1.800/portfólio)</p>
<p>5. LEDGER: Registra evento EMISSAO no MACRO HASH para cada bloco</p>
<p>6. NOTIFICAÇÃO: Envia push/email ao usuário sobre novo crédito disponível</p>
<p>7. ATUALIZAÇÃO: Recalcula KPIs do portfólio em tempo real (Redis cache)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**7.2 workers/agentic\_ai.py**

**workers/agentic\_ai.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>from celery import shared_task</p>
<p>from sqlalchemy import select, and_</p>
<p>from decimal import Decimal</p>
<p>from app.database import get_async_session</p>
<p>from app.portfolio.models import Portfolio, Contract, Block</p>
<p>from app.ledger.service import MacroHashService</p>
<p>from app.shared.utils import BLOCK_VALUE # R$40.00</p>
<p>@shared_task(bind=True, max_retries=3, default_retry_delay=60)</p>
<p>def distribute_credit_blocks(self, portfolio_id: str, new_capital: float):</p>
<p>'''</p>
<p>Tarefa Celery: distribui blocos de crédito após aporte confirmado.</p>
<p>FIFO: usuários mais antigos na fila têm prioridade.</p>
<p>'''</p>
<p>try:</p>
<p>async with get_async_session() as db:</p>
<p>portfolio = await db.get(Portfolio, portfolio_id)</p>
<p>n_blocks = int(Decimal(str(new_capital)) / BLOCK_VALUE)</p>
<p># Busca contratos elegíveis FIFO por score e data</p>
<p>eligible = await db.execute(</p>
<p>select(Contract)</p>
<p>.where(and_(</p>
<p>Contract.portfolio_id == portfolio_id,</p>
<p>Contract.status == 'ACTIVE',</p>
<p>Contract.current_balance &lt; Contract.credit_limit,</p>
<p>))</p>
<p>.order_by(Contract.score.desc(), Contract.issued_at.asc())</p>
<p>.limit(n_blocks)</p>
<p>)</p>
<p>prev_hash = portfolio.portfolio_hash</p>
<p>allocated = 0</p>
<p>for contract in eligible.scalars():</p>
<p>available = contract.credit_limit - contract.current_balance</p>
<p>alloc = min(BLOCK_VALUE, available)</p>
<p>contract.current_balance += alloc</p>
<p># Registra no MACRO HASH</p>
<p>event = await MacroHashService.record_event(</p>
<p>db=db,</p>
<p>contract_id=str(contract.id),</p>
<p>event_type='EMISSAO',</p>
<p>amount=alloc,</p>
<p>payload={'block_value': str(alloc), 'portfolio': portfolio_id},</p>
<p>prev_hash=prev_hash,</p>
<p>contract_hash=contract.contract_hash,</p>
<p>)</p>
<p>prev_hash = event.block_state_hash</p>
<p>allocated += 1</p>
<p>if allocated &gt;= n_blocks:</p>
<p>break</p>
<p>await db.commit()</p>
<p>return {'allocated_blocks': allocated, 'capital': new_capital}</p>
<p>except Exception as exc:</p>
<p>raise self.retry(exc=exc)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**7.3 Regras do Motor de Score e Elegibilidade**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Regra</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Critério</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Valor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Ação se falhar</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Score mínimo</p>
</blockquote></td>
<td><blockquote>
<p>credit_score &gt;= threshold</p>
</blockquote></td>
<td><blockquote>
<p>500 (0–1000)</p>
</blockquote></td>
<td><blockquote>
<p>Contrato não elegível para novos blocos</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DPD máximo</p>
</blockquote></td>
<td><blockquote>
<p>days_past_due &lt;= 5</p>
</blockquote></td>
<td><blockquote>
<p>5 dias</p>
</blockquote></td>
<td><blockquote>
<p>Bloqueio temporário de novos blocos</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Uso máximo</p>
</blockquote></td>
<td><blockquote>
<p>current_balance &lt; credit_limit</p>
</blockquote></td>
<td><blockquote>
<p>100% do limite</p>
</blockquote></td>
<td><blockquote>
<p>Sem novos blocos até pagamento</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KYC</p>
</blockquote></td>
<td><blockquote>
<p>kyc_status == APPROVED</p>
</blockquote></td>
<td><blockquote>
<p>Obrigatório</p>
</blockquote></td>
<td><blockquote>
<p>Bloqueio total do contrato</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Categoria match</p>
</blockquote></td>
<td><blockquote>
<p>contract.category == portfolio.category</p>
</blockquote></td>
<td><blockquote>
<p>Match</p>
</blockquote></td>
<td><blockquote>
<p>Não aloca — portfólio segmentado</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Limite portfólio</p>
</blockquote></td>
<td><blockquote>
<p>contracts &lt;= max_contracts</p>
</blockquote></td>
<td><blockquote>
<p>1.800</p>
</blockquote></td>
<td><blockquote>
<p>Portfólio fechado para novos contratos</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Fraude AML</p>
</blockquote></td>
<td><blockquote>
<p>aml_flag == False</p>
</blockquote></td>
<td><blockquote>
<p>Sem flag</p>
</blockquote></td>
<td><blockquote>
<p>Bloqueio imediato + alerta compliance</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **8. Integração Subadquirente e Cartão Pré-Pago**

O NEXUS utiliza um subadquirente (Dock, BS2, Conductor ou Matera) como BIN Sponsor para emissão dos cartões Visa/Mastercard pré-pagos. Toda transação gera um evento no MACRO HASH.

**8.1 Parceiros de Subadquirência**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Parceiro</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>BIN Sponsor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>API</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Custo estimado</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Recomendação</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Dock</p>
</blockquote></td>
<td><blockquote>
<p>Visa + MC</p>
</blockquote></td>
<td><blockquote>
<p>REST + Webhooks</p>
</blockquote></td>
<td><blockquote>
<p>R$8–15/cartão/mês</p>
</blockquote></td>
<td><blockquote>
<p>RECOMENDADO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BS2</p>
</blockquote></td>
<td><blockquote>
<p>Visa</p>
</blockquote></td>
<td><blockquote>
<p>REST + Webhooks</p>
</blockquote></td>
<td><blockquote>
<p>R$10–18/cartão/mês</p>
</blockquote></td>
<td><blockquote>
<p>Alternativa sólida</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Conductor</p>
</blockquote></td>
<td><blockquote>
<p>MC</p>
</blockquote></td>
<td><blockquote>
<p>REST + Webhooks</p>
</blockquote></td>
<td><blockquote>
<p>R$12–20/cartão/mês</p>
</blockquote></td>
<td><blockquote>
<p>Foco no varejo</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Matera</p>
</blockquote></td>
<td><blockquote>
<p>Visa + MC</p>
</blockquote></td>
<td><blockquote>
<p>REST + Webhooks</p>
</blockquote></td>
<td><blockquote>
<p>Sob consulta</p>
</blockquote></td>
<td><blockquote>
<p>Open Finance nativo</p>
</blockquote></td>
</tr>
</tbody>
</table>

**8.2 Fluxo de Emissão de Cartão (Python)**

**app/card/service.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># app/card/service.py</p>
<p>import httpx</p>
<p>from app.config import settings</p>
<p>from app.ledger.service import MacroHashService</p>
<p>class CardService:</p>
<p>@staticmethod</p>
<p>async def issue_card(user_id: str, credit_limit: float, contract_hash: str) -&gt; dict:</p>
<p>'''Emite cartão pré-pago via API do subadquirente (Dock)'''</p>
<p>async with httpx.AsyncClient(timeout=30.0) as client:</p>
<p>response = await client.post(</p>
<p>f'{settings.SUBACQUIRER_API_URL}/cards/issue',</p>
<p>headers={</p>
<p>'Authorization': f'Bearer {settings.SUBACQUIRER_API_KEY.get_secret_value()}',</p>
<p>'Content-Type': 'application/json',</p>
<p>},</p>
<p>json={</p>
<p>'holder_id': user_id,</p>
<p>'card_type': 'PREPAID',</p>
<p>'brand': 'VISA',</p>
<p>'currency': 'BRL',</p>
<p>'credit_limit': credit_limit,</p>
<p>'metadata': {'contract_hash': contract_hash},</p>
<p>}</p>
<p>)</p>
<p>response.raise_for_status()</p>
<p>return response.json()</p>
<p>@staticmethod</p>
<p>async def verify_webhook(payload: bytes, signature: str) -&gt; bool:</p>
<p>'''Verifica assinatura HMAC do webhook do subadquirente'''</p>
<p>import hmac, hashlib</p>
<p>secret = settings.SUBACQUIRER_WEBHOOK_SECRET.get_secret_value().encode()</p>
<p>expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()</p>
<p>return hmac.compare_digest(expected, signature) # timing-safe comparison</p>
</blockquote></td>
</tr>
</tbody>
</table>

**8.3 Fluxo de Fatura e Cobrança**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Ciclo de Vida do Contrato — Estados e Transições</strong></p>
<p>ATIVO ──&gt; (uso do cartão) ──&gt; ATIVO [saldo aumenta]</p>
<p>ATIVO ──&gt; (data vencimento) ──&gt; COBRANÇA GERADA [Celery Beat task]</p>
<p>COBRANÇA ──&gt; (pagamento confirmado PIX) ──&gt; LIQUIDADO [evento PAGAMENTO no ledger]</p>
<p>COBRANÇA ──&gt; (5 dias atraso) ──&gt; OVERDUE [multa 2% + juros 1%/dia, bloqueio de novos blocos]</p>
<p>OVERDUE ──&gt; (pagamento) ──&gt; ATIVO [reabilitação automática se score &gt;= 500]</p>
<p>OVERDUE ──&gt; (30 dias) ──&gt; BLOQUEADO [AE notificado, negativação CPC]</p>
<p>BLOQUEADO ──&gt; (negociação) ──&gt; LIQUIDADO [acordo + registro ledger LIQUIDACAO]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **9. API Endpoints Principais (FastAPI)**

Todos os endpoints usam validação Pydantic, autenticação JWT e são documentados automaticamente no Swagger UI (/api/docs). Versão: /api/v1/

**9.1 Auth Service**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Método</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Endpoint</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Body/Params</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resposta</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Rate Limit</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/auth/login</p>
</blockquote></td>
<td><blockquote>
<p>email, password</p>
</blockquote></td>
<td><blockquote>
<p>access_token, refresh_token</p>
</blockquote></td>
<td><blockquote>
<p>10/min</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/auth/refresh</p>
</blockquote></td>
<td><blockquote>
<p>refresh_token</p>
</blockquote></td>
<td><blockquote>
<p>novo access_token</p>
</blockquote></td>
<td><blockquote>
<p>20/min</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/auth/logout</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
<td><blockquote>
<p>204 No Content</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/auth/register</p>
</blockquote></td>
<td><blockquote>
<p>cpf, email, password, role</p>
</blockquote></td>
<td><blockquote>
<p>user_id, status</p>
</blockquote></td>
<td><blockquote>
<p>5/min</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/auth/me</p>
</blockquote></td>
<td><blockquote>
<p>Bearer token</p>
</blockquote></td>
<td><blockquote>
<p>UserProfile</p>
</blockquote></td>
<td><blockquote>
<p>60/min</p>
</blockquote></td>
</tr>
</tbody>
</table>

**9.2 Credit Service**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Método</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Endpoint</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Descrição</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Autorização</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/apply</p>
</blockquote></td>
<td><blockquote>
<p>Submete pedido de crédito</p>
</blockquote></td>
<td><blockquote>
<p>USER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/score/{cpf}</p>
</blockquote></td>
<td><blockquote>
<p>Consulta score de um CPF</p>
</blockquote></td>
<td><blockquote>
<p>AE, ADMIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/applications</p>
</blockquote></td>
<td><blockquote>
<p>Lista pedidos (com filtros)</p>
</blockquote></td>
<td><blockquote>
<p>AE, ADMIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATCH</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/{id}/approve</p>
</blockquote></td>
<td><blockquote>
<p>Aprova pedido manualmente</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PATCH</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/{id}/reject</p>
</blockquote></td>
<td><blockquote>
<p>Rejeita pedido com motivo</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/credit/{id}/report</p>
</blockquote></td>
<td><blockquote>
<p>Relatório completo de análise</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN, BOARD</p>
</blockquote></td>
</tr>
</tbody>
</table>

**9.3 Portfolio Service**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Método</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Endpoint</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Descrição</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Autorização</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/</p>
</blockquote></td>
<td><blockquote>
<p>Lista portfólios do Aplicante</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/</p>
</blockquote></td>
<td><blockquote>
<p>Cria novo portfólio</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/{id}</p>
</blockquote></td>
<td><blockquote>
<p>Detalhe + KPIs do portfólio</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/{id}/contracts</p>
</blockquote></td>
<td><blockquote>
<p>Lista contratos do portfólio</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/{id}/performance</p>
</blockquote></td>
<td><blockquote>
<p>Histórico de performance (candle)</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/{id}/deposit</p>
</blockquote></td>
<td><blockquote>
<p>Novo aporte (trigger Agentic AI)</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/{id}/withdraw</p>
</blockquote></td>
<td><blockquote>
<p>Solicitação de resgate</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/portfolio/market</p>
</blockquote></td>
<td><blockquote>
<p>Mercado secundário — portfólios</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR</p>
</blockquote></td>
</tr>
</tbody>
</table>

**9.4 Ledger Service**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Método</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Endpoint</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Descrição</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Autorização</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/ledger/events</p>
</blockquote></td>
<td><blockquote>
<p>Lista eventos com filtros</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN, BOARD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/ledger/hash/{hash}</p>
</blockquote></td>
<td><blockquote>
<p>Busca por qualquer hash da cadeia</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN, BOARD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/ledger/contract/{id}</p>
</blockquote></td>
<td><blockquote>
<p>Timeline completa de um contrato</p>
</blockquote></td>
<td><blockquote>
<p>INVESTOR, ADMIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/ledger/verify/{id}</p>
</blockquote></td>
<td><blockquote>
<p>Verifica integridade da cadeia</p>
</blockquote></td>
<td><blockquote>
<p>ADMIN, COMPLIANCE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/ledger/export</p>
</blockquote></td>
<td><blockquote>
<p>Exporta trilha de auditoria (CSV)</p>
</blockquote></td>
<td><blockquote>
<p>COMPLIANCE, BOARD</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **10. Celery Beat — Jobs Agendados**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Job</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tarefa</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Frequência</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Serviço</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>distribute_credit_blocks</p>
</blockquote></td>
<td><blockquote>
<p>Distribuição de blocos pós-aporte</p>
</blockquote></td>
<td><blockquote>
<p>Trigger (webhook PIX)</p>
</blockquote></td>
<td><blockquote>
<p>agentic_ai.py</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>generate_invoices</p>
</blockquote></td>
<td><blockquote>
<p>Geração de faturas por vencimento</p>
</blockquote></td>
<td><blockquote>
<p>Diário 02:00</p>
</blockquote></td>
<td><blockquote>
<p>billing.py</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>process_payments</p>
</blockquote></td>
<td><blockquote>
<p>Confirmação de pagamentos PIX</p>
</blockquote></td>
<td><blockquote>
<p>A cada 5 min</p>
</blockquote></td>
<td><blockquote>
<p>billing.py</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>flag_overdue</p>
</blockquote></td>
<td><blockquote>
<p>Marca contratos vencidos (DPD)</p>
</blockquote></td>
<td><blockquote>
<p>Diário 06:00</p>
</blockquote></td>
<td><blockquote>
<p>billing.py</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>recalculate_scores</p>
</blockquote></td>
<td><blockquote>
<p>Recalcula scores de usuários</p>
</blockquote></td>
<td><blockquote>
<p>Semanal Domingo 03:00</p>
</blockquote></td>
<td><blockquote>
<p>credit worker</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>refresh_kpi_cache</p>
</blockquote></td>
<td><blockquote>
<p>Atualiza KPIs em Redis</p>
</blockquote></td>
<td><blockquote>
<p>A cada 15 min</p>
</blockquote></td>
<td><blockquote>
<p>report worker</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>send_due_notifications</p>
</blockquote></td>
<td><blockquote>
<p>Notifica usuários com venc. 3 dias</p>
</blockquote></td>
<td><blockquote>
<p>Diário 08:00</p>
</blockquote></td>
<td><blockquote>
<p>notifications.py</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>generate_bacen_report</p>
</blockquote></td>
<td><blockquote>
<p>Relatório regulatório BACEN</p>
</blockquote></td>
<td><blockquote>
<p>Mensal 1º dia 04:00</p>
</blockquote></td>
<td><blockquote>
<p>report worker</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>verify_hash_chain</p>
</blockquote></td>
<td><blockquote>
<p>Auditoria automática de integridade</p>
</blockquote></td>
<td><blockquote>
<p>Diário 01:00</p>
</blockquote></td>
<td><blockquote>
<p>ledger worker</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sync_odoo_entries</p>
</blockquote></td>
<td><blockquote>
<p>Sincroniza lançamentos com ODOO</p>
</blockquote></td>
<td><blockquote>
<p>A cada 2h</p>
</blockquote></td>
<td><blockquote>
<p>report worker</p>
</blockquote></td>
</tr>
</tbody>
</table>

**workers/celery\_app.py**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># workers/celery_app.py</p>
<p>from celery import Celery</p>
<p>from celery.schedules import crontab</p>
<p>from app.config import settings</p>
<p>celery_app = Celery('nexus')</p>
<p>celery_app.conf.update(</p>
<p>broker_url=settings.CELERY_BROKER_URL,</p>
<p>result_backend=settings.CELERY_RESULT_BACKEND,</p>
<p>task_serializer='json',</p>
<p>result_serializer='json',</p>
<p>accept_content=['json'],</p>
<p>timezone='America/Sao_Paulo',</p>
<p>enable_utc=True,</p>
<p>beat_schedule={</p>
<p>'generate-invoices-daily': {</p>
<p>'task': 'workers.billing.generate_invoices',</p>
<p>'schedule': crontab(hour=2, minute=0),</p>
<p>},</p>
<p>'flag-overdue-daily': {</p>
<p>'task': 'workers.billing.flag_overdue',</p>
<p>'schedule': crontab(hour=6, minute=0),</p>
<p>},</p>
<p>'refresh-kpi-cache': {</p>
<p>'task': 'workers.reports.refresh_kpi_cache',</p>
<p>'schedule': 900, # a cada 15 min</p>
<p>},</p>
<p>'verify-hash-chain': {</p>
<p>'task': 'workers.ledger.verify_chain',</p>
<p>'schedule': crontab(hour=1, minute=0),</p>
<p>},</p>
<p>}</p>
<p>)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **11. Docker e Infraestrutura de Deploy**

**11.1 docker-compose.yml**

**docker/docker-compose.yml**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>version: '3.9'</p>
<p>services:</p>
<p># ── API FastAPI ───────────────────────────────────</p>
<p>api:</p>
<p>build: .</p>
<p>command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4</p>
<p>ports: ['8000:8000']</p>
<p>env_file: .env</p>
<p>depends_on: [postgres, redis]</p>
<p>healthcheck:</p>
<p>test: ['CMD', 'curl', '-f', 'http://localhost:8000/health']</p>
<p>interval: 30s</p>
<p># ── Celery Worker ────────────────────────────────</p>
<p>worker:</p>
<p>build: .</p>
<p>command: celery -A workers.celery_app worker --loglevel=info --concurrency=4</p>
<p>env_file: .env</p>
<p>depends_on: [redis, postgres]</p>
<p># ── Celery Beat (scheduler) ───────────────────────</p>
<p>beat:</p>
<p>build: .</p>
<p>command: celery -A workers.celery_app beat --loglevel=info</p>
<p>env_file: .env</p>
<p>depends_on: [redis]</p>
<p># ── PostgreSQL ────────────────────────────────────</p>
<p>postgres:</p>
<p>image: postgres:16-alpine</p>
<p>volumes: ['pg_data:/var/lib/postgresql/data']</p>
<p>environment:</p>
<p>POSTGRES_DB: nexus_db</p>
<p>POSTGRES_USER: nexus_user</p>
<p>POSTGRES_PASSWORD: ${DB_PASSWORD}</p>
<p>healthcheck:</p>
<p>test: ['CMD-SHELL', 'pg_isready -U nexus_user']</p>
<p># ── Redis ─────────────────────────────────────────</p>
<p>redis:</p>
<p>image: redis:7-alpine</p>
<p>command: redis-server --requirepass ${REDIS_PASSWORD} --maxmemory 512mb</p>
<p>volumes: ['redis_data:/data']</p>
<p># ── Nginx (API Gateway) ───────────────────────────</p>
<p>nginx:</p>
<p>image: nginx:alpine</p>
<p>volumes:</p>
<p>- ./docker/nginx.conf:/etc/nginx/nginx.conf</p>
<p>- ./certs:/etc/ssl/certs</p>
<p>ports: ['80:80', '443:443']</p>
<p>depends_on: [api]</p>
<p>volumes:</p>
<p>pg_data:</p>
<p>redis_data:</p>
</blockquote></td>
</tr>
</tbody>
</table>

**11.2 Dockerfile — Multi-stage Build**

**docker/Dockerfile**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># Stage 1: builder</p>
<p>FROM python:3.12-slim AS builder</p>
<p>WORKDIR /app</p>
<p>RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends build-essential libpq-dev</p>
<p>COPY requirements.txt .</p>
<p>RUN pip install --no-cache-dir --user -r requirements.txt</p>
<p># Stage 2: runtime (imagem mínima — menor superfície de ataque)</p>
<p>FROM python:3.12-slim AS runtime</p>
<p>WORKDIR /app</p>
<p>RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends libpq5 curl &amp;&amp; rm -rf /var/lib/apt/lists/*</p>
<p>RUN useradd --no-create-home --shell /bin/false nexusapp</p>
<p>COPY --from=builder /root/.local /home/nexusapp/.local</p>
<p>COPY . .</p>
<p>RUN chown -R nexusapp:nexusapp /app</p>
<p>USER nexusapp</p>
<p>ENV PATH=/home/nexusapp/.local/bin:$PATH</p>
<p>EXPOSE 8000</p>
<p>HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **12. requirements.txt — Dependências de Produção**

**requirements.txt**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># API Framework</p>
<p>fastapi==0.115.0</p>
<p>uvicorn[standard]==0.32.0</p>
<p>pydantic==2.9.0</p>
<p>pydantic-settings==2.6.0</p>
<p># Database</p>
<p>sqlalchemy[asyncio]==2.0.36</p>
<p>asyncpg==0.30.0 # driver async PostgreSQL</p>
<p>alembic==1.14.0</p>
<p>psycopg2-binary==2.9.10 # para Alembic sync migrations</p>
<p># Cache &amp; Messaging</p>
<p>redis[hiredis]==5.2.0</p>
<p>celery[redis]==5.4.0</p>
<p># Auth &amp; Security</p>
<p>python-jose[cryptography]==3.3.0</p>
<p>passlib[bcrypt]==1.7.4</p>
<p>slowapi==0.1.9 # rate limiting</p>
<p># HTTP Client (integrações externas)</p>
<p>httpx==0.27.2</p>
<p># Utilities</p>
<p>structlog==24.4.0 # logging estruturado JSON</p>
<p>python-decouple==3.8 # .env management</p>
<p>python-multipart==0.0.12 # upload de arquivos</p>
<p># Financeiro</p>
<p>python-dateutil==2.9.0</p>
<p>babel==2.16.0 # formatação monetária pt-BR</p>
<p># ML / Scoring (Agentic AI)</p>
<p>scikit-learn==1.5.2</p>
<p>joblib==1.4.2</p>
</blockquote></td>
</tr>
</tbody>
</table>

**requirements-dev.txt**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># requirements-dev.txt</p>
<p>pytest==8.3.3</p>
<p>pytest-asyncio==0.24.0</p>
<p>pytest-cov==6.0.0</p>
<p>httpx==0.27.2 # test client async</p>
<p>factory-boy==3.3.1 # fixtures de dados</p>
<p>black==24.10.0</p>
<p>ruff==0.7.0</p>
<p>mypy==1.13.0</p>
<p>pre-commit==4.0.1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **13. Roadmap Técnico de Implementação**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Sprint</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Duração</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Entregáveis</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Dependências</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Sprint 1</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Setup projeto, Docker, PostgreSQL, modelos base, auth JWT</p>
</blockquote></td>
<td><blockquote>
<p>Ambiente dev pronto</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sprint 2</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Credit service + scoring model + MACRO HASH ledger</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sprint 3</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Portfolio service + Agentic AI worker + Celery</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sprint 4</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Card service + integração subadquirente (sandbox Dock)</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sprint 5</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>AE service + território + comissão + notificações</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sprint 6</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>PIX integration + billing jobs + ciclo completo de cobrança</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sprint 7</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Report service + Superset views + Power BI + export</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 3,5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sprint 8</p>
</blockquote></td>
<td><blockquote>
<p>2 semanas</p>
</blockquote></td>
<td><blockquote>
<p>Testes de carga, pentest, hardening segurança, go-live checklist</p>
</blockquote></td>
<td><blockquote>
<p>Sprint 1-7</p>
</blockquote></td>
</tr>
</tbody>
</table>

NEXUS | Arquitetura Técnica v1.0 | FastAPI + PostgreSQL + Redis + Celery + Docker

Confidencial — Uso Interno | Python 3.12 | Backend NEXUS P2P Lending Platform
