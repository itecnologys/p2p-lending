# Antigravity - Diagnostico e Plano de Integracao

## Escopo analisado
Diretorio: `p2p-lending by Antigravity`

## O que existe hoje
- Conteudo estrategico e financeiro em Markdown (`01` a `07`).
- Artefatos de apresentacao/exportacao (`.doc`, `.docx`, `.html`, `.pdf`).
- Dashboards financeiros evolutivos (`08` a `15`, varias versoes).
- Scripts Python para:
  - simulacao financeira (`financial_model.py`, `financial_model_realistic.py`);
  - conversao de markdown para Word (`convert_to_word.py`);
  - geracao de documentos executivos (`create_pitch_word.py`, `create_whitepaper_word.py`).

## Valor real para o projeto
1. Base forte de narrativa executiva e tese financeira.
2. Material pronto para pitch/compliance interno (board e controladoria).
3. Modelos financeiros reaproveitaveis para transformar em modulo de dominio.

## Principais lacunas tecnicas
- Nao ha empacotamento Python (`requirements.txt` ou `pyproject.toml`).
- Scripts com caminhos absolutos fixos e execucao manual.
- Ausencia de testes automatizados para formulas financeiras.
- Multipla versao de dashboards sem criterio de "source of truth".
- Mistura de artefatos finais e fonte no mesmo nivel de pasta.

## Itens reaproveitaveis imediatamente
- `05_Projecao_Financeira_24_Meses.md` e `06_Projecao_Financeira_Crescimento_Realista.md` como base de regras de negocio.
- `financial_model.py` e `financial_model_realistic.py` como semente para um modulo `finance_engine`.
- `07_NEXUS_Stablecoin_Whitepaper.md` e `06_Manual_NEXUS_Controladoria_e_Tese.md` para docs oficiais no `nexus-platform/docs`.

## Itens que devem ser tratados como legado
- Versoes antigas de dashboard (`08` a `14`) apos consolidar uma versao canonicamente valida.
- Arquivos `.doc` intermediarios quando existir `.md` e `.docx` equivalentes.
- Arquivos de captura/rascunho sem uso operacional direto.

## Plano de integracao com nexus-platform
### Fase 1 - Organizacao (rapida)
- Criar estrutura alvo:
  - `nexus-platform/docs/business/`
  - `nexus-platform/tools/finance/`
  - `nexus-platform/artifacts/presentations/`
- Copiar e normalizar os Markdown principais para `docs/business`.
- Definir uma unica versao oficial do dashboard DRE e marcar as demais como historicas.

### Fase 2 - Produto tecnico
- Extrair formulas dos scripts Python para modulo reutilizavel:
  - `nexus-platform/tools/finance/engine.py`
  - `nexus-platform/tools/finance/scenarios.py`
- Remover caminhos absolutos, usar CLI com parametros.
- Adicionar testes unitarios das funcoes de calculo.

### Fase 3 - Governanca
- Definir regra de versionamento de documentos (vX.Y no nome ou metadado interno).
- Separar claramente:
  - fonte editavel (`.md`, `.py`);
  - artefato final (`.docx`, `.pdf`, `.html`).
- Criar rotina de exportacao unica para gerar artefatos com comando padrao.

## Decisao recomendada
Manter `p2p-lending by Antigravity` como acervo historico temporario, e migrar de forma controlada os itens de alto valor para `nexus-platform`, que deve permanecer como repositorio canonico do produto.

## Backlog imediato (acao pratica)
- [ ] Consolidar dashboard corporativo em versao unica oficial.
- [ ] Migrar 4 documentos de negocio principais para `nexus-platform/docs/business`.
- [ ] Criar `requirements.txt` para os scripts Python atuais.
- [ ] Refatorar scripts para parametros de entrada/saida (sem path fixo).
- [ ] Implementar testes das formulas financeiras criticas.
