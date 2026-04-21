# NEXUS - Plano de Execucao 30-60-90

## Meta
Transformar o projeto de prototipo/documentacao em plataforma tecnica executavel, com base consistente para expansao.

## 0-30 dias (fundacao)
### Entregas
- Estrutura backend minima com FastAPI e healthcheck.
- Contrato OpenAPI conectado ao ciclo de desenvolvimento.
- Padrao de ambiente local (`.env.example`, dependencias e comandos).
- CI inicial com gates basicos.

### Indicadores de sucesso
- Ambiente sobe localmente em menos de 10 minutos.
- Pipeline valida automaticamente cada mudanca.
- Primeiro endpoint de negocio respondendo com contrato definido.

## 31-60 dias (fluxo vertical)
### Entregas
- Fluxo ponta a ponta: autenticacao + solicitacao de credito.
- Persistencia inicial em Postgres com migracao.
- Testes de integracao para fluxo principal.
- Documentacao operacional (runbook de desenvolvimento).

### Indicadores de sucesso
- Fluxo principal validado por testes automatizados.
- Reducao de dependencia de mock em modulo critico.
- Time consegue reproduzir setup sem suporte ad-hoc.

## 61-90 dias (maturidade)
### Entregas
- Trilhas de auditoria iniciais (ledger/hash simplificado).
- Observabilidade basica (logs estruturados e metricas essenciais).
- Controles de seguranca no pipeline (scan de segredos/dependencias).
- Estrutura de deploy para homologacao.

### Indicadores de sucesso
- Visibilidade de erros e performance em ambiente de teste.
- Risco tecnico reduzido para expansao funcional.
- Base pronta para evolucao regulatoria e operacional.

## Riscos e mitigacoes
- Risco: excesso de frentes paralelas sem entrega vertical.
  - Mitigacao: priorizar fluxo unico ponta a ponta antes de novos modulos.
- Risco: divergencia entre OpenAPI e implementacao.
  - Mitigacao: validação de contrato obrigatoria no CI.
- Risco: proliferacao de prototipos sem consolidacao.
  - Mitigacao: definir repositorio canonico e politicas de deprecacao.
