# NEXUS - Backlog Tecnico Priorizado

## Criterio de prioridade
- P0: bloqueia evolucao do produto.
- P1: acelera entrega com risco controlado.
- P2: melhora qualidade e escalabilidade.

## P0 - Fundacao executavel
- [ ] Criar `backend/` com FastAPI minimo e endpoint `/health`.
- [ ] Implementar modulo inicial de autenticacao (stub) com JWT local de desenvolvimento.
- [ ] Publicar `requirements.txt` ou `pyproject.toml` para backend.
- [ ] Criar `.env.example` com variaveis essenciais e placeholders.
- [ ] Definir padrao de comandos (`Makefile` ou scripts equivalentes).
- [ ] Configurar CI minimo: lint + testes + validacao OpenAPI.

## P1 - Primeira cadeia de valor
- [ ] Implementar rota `POST /credit/request` com validacoes basicas.
- [ ] Implementar persistencia inicial (PostgreSQL + migracao inicial).
- [ ] Integrar camada de score em modo mock com interface de provider.
- [ ] Criar testes de integracao para fluxo auth -> solicitacao de credito.
- [ ] Adicionar verificacao de breaking change da OpenAPI no CI.

## P2 - Maturidade operacional
- [ ] Estruturar logs JSON e correlacao por request id.
- [ ] Expor metricas de aplicacao e healthchecks dependentes.
- [ ] Introduzir fila/worker para tarefas assincronas.
- [ ] Adicionar scans de seguranca (segredos e dependencias) no pipeline.
- [ ] Definir padrao de ADR para decisoes arquiteturais.

## Debito tecnico identificado
- Duplicacao de conteudo entre diretorios de website/prototipo.
- Referencias de telas no hub sem implementacao correspondente.
- Ausencia de padrao unico de versionamento de artefatos tecnicos.

## Definicao de pronto (DoD tecnico minimo)
- Codigo com teste automatico correspondente.
- Contrato da API atualizado e validado.
- Lint e CI passando.
- Documentacao de execucao atualizada.
