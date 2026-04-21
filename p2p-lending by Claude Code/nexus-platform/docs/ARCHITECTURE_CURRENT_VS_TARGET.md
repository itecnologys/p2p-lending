# NEXUS - Arquitetura Atual vs Alvo

## Objetivo
Registrar o estado tecnico atual do projeto, comparar com a arquitetura alvo e explicitar os gaps para execucao.

## Estado atual (as-is)
- Frontend e prototipos em HTML/CSS/JS estatico.
- Mock de dados centralizado em `platform/shared/mock-data.js`.
- Documentacao funcional e tecnica madura (whitepapers, arquitetura, OpenAPI).
- Scripts Python auxiliares para material financeiro/documental.
- Sem backend de API executavel no repositorio.
- Sem pipeline CI/CD ativo e sem suite de testes automatizados padronizada.

## Arquitetura alvo (to-be)
- Backend FastAPI como camada de negocio e integracao.
- Persistencia em PostgreSQL + cache/fila com Redis.
- Processamento assincrono com worker (Celery/RQ).
- Frontend web aplicacional (evolucao do prototipo).
- Contrato de API versionado e validado por CI.
- Observabilidade (logs estruturados, metricas, healthchecks).
- Seguranca baseline (gestao de segredos, scans, hardening de pipeline).

## Gap matrix
| Dominio | Atual | Alvo | Gap | Prioridade |
|---|---|---|---|---|
| API | Apenas OpenAPI documental | FastAPI executavel | Falta servico real | Alta |
| Dados | Mock JS e artefatos docs | PostgreSQL + migracoes | Falta modelagem implementada | Alta |
| Assincronia | Nao implementado | Worker + fila | Falta jobs e filas | Media |
| Frontend app | HTML estatico | App web modular | Falta componentizacao e estado real | Media |
| QA | Validacao manual | Testes unit/integration/contract | Falta automacao de qualidade | Alta |
| CI/CD | Nao configurado | Pipeline com gates | Falta esteira de entrega | Alta |
| Observabilidade | Nao implementado | Logs + metricas + alertas | Falta instrumentacao | Media |
| Seguranca | Sem baseline tecnico formal | Secret scan + SAST + policy | Falta controle preventivo | Alta |

## Decisoes de consolidacao
1. Definir `nexus-platform` como diretorio canonico de produto.
2. Tratar prototipos legados como referencia historica, nao como source of truth.
3. Manter contrato OpenAPI como artefato vivo, validado em pipeline.

## Proximos passos imediatos
1. Criar skeleton de backend com rotas basicas (`/health`, `/auth/login`, `/credit/request` mock).
2. Formalizar dependencias e comandos padrao de desenvolvimento.
3. Implantar CI minimo (lint + testes + validacao de contrato).
4. Substituir dependencias criticas de mock por camada de persistencia progressiva.
