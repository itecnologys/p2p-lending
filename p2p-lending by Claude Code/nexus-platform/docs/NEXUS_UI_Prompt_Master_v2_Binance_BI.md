---
title: "NEXUS — NEXUS_UI_Prompt_Master_v2_Binance_BI"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>[ NEXUS · UI/UX DESIGN SPECIFICATION v2.0 · BINANCE-GRADE FINANCIAL INTERFACE ]</strong></p>
<p><strong>PROMPT MESTRE DE DESIGN v2</strong></p>
<p><strong>Binance-Style · Dribbble Inspirations · BI APIs · Power BI Templates</strong></p>
<p><em>Aplicante · Usuario · Executivo · 360 BOARD · Apache Superset · Metabase · Grafana · Power BI</em></p></td>
</tr>
</tbody>
</table>

*Versao 2.0 do Prompt Mestre — migrado de estilo OpenSea para BINANCE-GRADE financial UI. Inclui: (1) Design System Binance-inspired com tokens exatos, (2) inspiracoes catalogadas do Dribbble/Behance para cada modulo, (3) especificacoes de API para BI open source (Apache Superset, Metabase, Grafana) e (4) templates e integracao Power BI REST API.*

**PARTE 1 — DESIGN SYSTEM BINANCE-GRADE (NEXUS v2)**

O redesign segue os principios do Binance UI Refined (2024): densidade maxima de informacao, hierarquia visual clara com amarelo/verde/vermelho como linguagem universal de mercado, e componentes que comunicam dados financeiros sem ambiguidade. Referencia tecnica: Figma Binance Market Trade Dashboard (community file 1216086272130411012) + Design System Binance por Absinthe Wu + Advanced Trade Interface Binance.US (2024).

**1.1 Paleta de Cores — Binance Specification**

| **Token**             | **Hex**  | **Uso Binance Original**               | **Uso NEXUS**                         |
| --------------------- | -------- | -------------------------------------- | ------------------------------------- |
| \--bnb-bg-primary     | \#0B0E11 | Background absoluto da pagina          | Base de todas as telas dark           |
| \--bnb-bg-card        | \#161A1F | Cards, paineis, modais                 | NexusCard, sidebars, dropdowns        |
| \--bnb-bg-hover       | \#1E242B | Hover states, rows alternadas, inputs  | Estados interativos, tabelas          |
| \--bnb-bg-input       | \#2B3038 | Background de inputs e selects         | Todos os campos de formulario         |
| \--bnb-border         | \#2B3038 | Bordas de cards e separadores          | border: 1px solid \#2B3038            |
| \--bnb-yellow         | \#F0B90B | CTA principal, preco BNB, brand        | CTAs primarios, logo, destaques       |
| \--bnb-yellow-hover   | \#D4A800 | Hover do CTA principal                 | Hover dos botoes primarios            |
| \--bnb-green          | \#03C076 | Preco subindo, ganho, positivo, buy    | Adimplente, retorno, saldo positivo   |
| \--bnb-red            | \#F6465C | Preco caindo, perda, negativo, sell    | Inadimplente, deficit, alerta critico |
| \--bnb-text-primary   | \#EAECEF | Texto principal                        | Todos os textos de conteudo           |
| \--bnb-text-secondary | \#848E9C | Texto secundario, labels, placeholders | Labels, captions, helper text         |
| \--bnb-text-tertiary  | \#474D57 | Texto terciario, desabilitado          | Itens desabilitados, meta info        |
| \--bnb-blue           | \#0091FF | Links, info, accent secundario         | Links, badges info, highlights        |
| \--bnb-purple         | \#6C3ABD | Hash/blockchain, premium, stablecoin   | NexusHash components, features crypto |

**1.2 Tipografia — Binance Flex inspired**

<table>
<tbody>
<tr class="odd">
<td><p><strong>TIPOGRAFIA NEXUS v2 — BINANCE-GRADE</strong></p>
<p>Font Principal: 'IBM Plex Sans' (substituto open source da Binance Flex) — Google Fonts</p>
<p>Motivo: geometrica, tecnologica, excelente legibilidade em densidades altas de dados</p>
<p>Font Monoespacada: 'IBM Plex Mono' — para precos, hashes, codigos, numeros de contratos</p>
<p>Mesmo ecossistema IBM Plex — consistencia visual total</p>
<p>ESCALA TIPOGRAFICA:</p>
<p>Display (hero prices): IBM Plex Mono 48px Bold | color: --bnb-yellow | letter-spacing: -1px</p>
<p>H1 Page Title: IBM Plex Sans 24px SemiBold | color: --bnb-text-primary | ls: -0.3px</p>
<p>H2 Section: IBM Plex Sans 18px SemiBold | color: --bnb-text-primary</p>
<p>H3 Card Title: IBM Plex Sans 14px SemiBold | color: --bnb-text-primary | UPPERCASE</p>
<p>H4 Label: IBM Plex Sans 12px Medium | color: --bnb-text-secondary | UPPERCASE + ls: 0.8px</p>
<p>Body: IBM Plex Sans 14px Regular | color: --bnb-text-primary | line-height: 1.5</p>
<p>Caption: IBM Plex Sans 12px Regular | color: --bnb-text-secondary</p>
<p>Micro: IBM Plex Sans 11px Regular | color: --bnb-text-tertiary</p>
<p>Price Up: IBM Plex Mono 14px SemiBold | color: --bnb-green</p>
<p>Price Down: IBM Plex Mono 14px SemiBold | color: --bnb-red</p>
<p>Hash/Code: IBM Plex Mono 13px | color: --bnb-purple | bg: rgba(108,58,189,0.1) | px:8 py:3 rounded-4</p></td>
</tr>
</tbody>
</table>

**1.3 Componentes — Binance UI Kit NEXUS**

<table>
<tbody>
<tr class="odd">
<td><p><strong>COMPONENTES BASE — BINANCE-STYLE NEXUS KIT</strong></p>
<p>NexusCard:</p>
<p>background: --bnb-bg-card | border: 1px solid --bnb-border | border-radius: 8px</p>
<p>padding: 20px | box-shadow: none (Binance nao usa sombras — usa bordas)</p>
<p>hover: border-color: rgba(240,185,11,0.3) | transition: 200ms ease</p>
<p>NexusButton Primary (Buy/CTA):</p>
<p>background: --bnb-yellow | color: #0B0E11 (preto no botao amarelo, como Binance)</p>
<p>border-radius: 4px (Binance usa cantos menos arredondados que material design)</p>
<p>padding: 12px 24px | font: IBM Plex Sans 14px SemiBold | hover: --bnb-yellow-hover</p>
<p>NexusButton Danger (Sell/Alert):</p>
<p>background: --bnb-red | color: white | mesmos specs do primary</p>
<p>NexusInput:</p>
<p>background: --bnb-bg-input | border: 1px solid --bnb-border | border-radius: 4px</p>
<p>padding: 10px 12px | font: IBM Plex Sans 14px | color: --bnb-text-primary</p>
<p>focus: border-color: --bnb-yellow | placeholder: --bnb-text-tertiary</p>
<p>NexusBadge:</p>
<p>border-radius: 2px (quase quadrado, estilo Binance) | padding: 2px 8px | font: 12px SemiBold</p>
<p>Variantes: success(#03C076 bg 10% + text verde) | danger(#F6465C bg 10% + text vermelho)</p>
<p>warning(#F0B90B bg 10% + text amarelo) | info(#0091FF bg 10% + text azul)</p>
<p>NexusTicker (componente exclusivo — como o ticker do Binance):</p>
<p>Linha horizontal scrolling com pares de metricas: [Vertical: SAUDE] [3,5%] [+0.2% 24h]</p>
<p>Background: --bnb-bg-card | border-bottom: 1px --bnb-border | height: 36px</p>
<p>Auto-scroll infinito | Pause ao hover</p>
<p>NexusCandleChart (TradingView-style mas para portfolio NEXUS):</p>
<p>Usar: lightweight-charts (lib TradingView, open source MIT)</p>
<p>Candles: verde=--bnb-green | vermelho=--bnb-red | background: --bnb-bg-primary</p>
<p>Grid: rgba(255,255,255,0.04) | Crosshair: --bnb-text-secondary</p>
<p>Volume bars abaixo do chart principal (padrao Binance)</p>
<p>NexusOrderBook (adaptado para NEXUS — lista de contratos por status):</p>
<p>2 colunas: Adimplentes (verde) | Inadimplentes (vermelho)</p>
<p>Barras de profundidade de fundo (como order book do Binance) em rgba</p>
<p>Scroll infinito | Atualizacao em tempo real com animacao de flash</p>
<p>NexusDepthChart (grafico de profundidade do portfolio):</p>
<p>Area chart com 2 lados: retorno acumulado (verde) vs inadimplencia acumulada (vermelho)</p>
<p>X-axis: tempo | Y-axis: valor em R$ | Tooltip com detalhes do ponto</p>
<p>NexusSidebar:</p>
<p>width: 240px | background: --bnb-bg-card | border-right: 1px --bnb-border</p>
<p>Collapsible para 56px (icon only) | Animacao: 200ms ease</p>
<p>Menu items: padding 12px 16px | hover bg: --bnb-bg-hover | active: border-left 3px --bnb-yellow</p>
<p>NexusDataGrid (tabela densa estilo Binance):</p>
<p>Row height: 40px (compacto) | Header: 32px | font: 13px</p>
<p>Hover row: background --bnb-bg-hover | sort indicators nos headers</p>
<p>Virtualizacao obrigatoria para &gt;50 linhas | sticky header</p>
<p>Paginacao: estilo Binance (&lt;&lt; &lt; 1 2 3 &gt; &gt;&gt; | 10 por pagina)</p></td>
</tr>
</tbody>
</table>

**PARTE 2 — CATALOGO DE INSPIRACOES DRIBBBLE/BEHANCE POR MODULO**

Catalogo estruturado das melhores referencias visuais encontradas nas pesquisas de Dribbble (tags: stock-market-dashboard, trading-dashboard, stock-market-ui) e Behance (trading dashboard UIUX). Cada referencia e catalogada com o modulo NEXUS onde aplicar.

**2.1 Referencias para Dashboard do Aplicante (Portfolio View)**

| **Referencia Visual**                                      | **Fonte**                                     | **Elementos a Adaptar para NEXUS**                                                                  |
| ---------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Trading Dashboard dark com candlestick + metricas laterais | Dribbble: trading-dashboard (200+ resultados) | Layout 3 paineis: chart central + metricas esq + ordem dir; candle chart para evolucao do portfolio |
| Portfolio Analytics dark com donut + sparklines            | Dribbble: stock-dashboard                     | Donut de alocacao por vertical + sparklines por vertical na mesma tela                              |
| Crypto Portfolio Tracker (Binance-inspired)                | Dribbble: binance tag                         | Cards de ativos com % change + mini charts; adaptar para verticais NEXUS                            |
| Wealth Management Dashboard (Bloomberg-style)              | Behance: Trading Dashboard UIUX 2024          | Grade densa de KPIs no topo + grafico principal + tabela abaixo; exatamente o layout A-02           |
| Real-time Market Overview com ticker                       | Dribbble: stock-market-ui                     | NexusTicker na topbar + painel de destaques com maiores retornos/riscos do dia                      |
| Investment Forecast UI com cenarios                        | Dribbble: stock-market (1900+ designs)        | Slider de cenario (pessimista/base/otimista) com curvas projetadas — usar no Composer A-03          |

**2.2 Referencias para Ledger / Hash View (A-04)**

| **Referencia Visual**                      | **Fonte**                                 | **Elementos a Adaptar**                                                                 |
| ------------------------------------------ | ----------------------------------------- | --------------------------------------------------------------------------------------- |
| Blockchain Explorer dark (Etherscan-style) | Pesquisa: blockchain explorer UI Dribbble | Timeline de transacoes com hash + estado + valor; adaptar para micro-contratos NEXUS    |
| GitHub Contribution Graph (heatmap)        | GitHub.com (referencia direta)            | Grid de blocos coloridos por estado do contrato — visual imediato da saude do portfolio |
| Network Transaction Visualization          | Dribbble: blockchain dashboard            | Grafico de nos e conexoes para mostrar Aplicante→microcontratos→usuarios                |
| Audit Trail / Log Viewer                   | Behance: fintech audit UI                 | Timeline scrollavel de eventos com filtros por tipo; usar na aba de historico do ledger |

**2.3 Referencias para 360 Board (B-01)**

| **Referencia Visual**                       | **Fonte**                                    | **Elementos a Adaptar**                                                                    |
| ------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Bloomberg Terminal dark (densidade maxima)  | Bloomberg Terminal (referencia classica)     | Grade densa de dados financeiros; usar na aba Financeiro do Board                          |
| Palantir Gotham-style operational dashboard | Pesquisa: operational intelligence dashboard | Mapa geografico + alertas em tempo real + metricas de campo; usar na aba Executivos        |
| Grafana monitoring board                    | Grafana.com (referencia direta)              | Multi-panel layout com widgets independentes; drag-and-drop para o Board customizar layout |
| TradingView multi-chart layout              | TradingView.com (referencia direta)          | Layout de 4 graficos simultâneos para comparar verticais; usar na aba Risco                |
| Retool-style admin dashboard                | Retool.com (referencia)                      | Tabelas + formularios integrados no mesmo painel; usar nas telas de gestao                 |

**2.4 Referencias para App do Usuario (U-02)**

| **Referencia Visual**               | **Fonte**                           | **Elementos a Adaptar**                                                       |
| ----------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------- |
| Nubank home card com gradiente dark | Nubank app (referencia direta BR)   | Cartao virtual animado + valor disponivel em destaque; usar como hero do U-02 |
| Wise/Revolut transfer flow          | Wise app (referencia internacional) | Simplicidade do fluxo de pagamento; usar no U-04 (pagamento de fatura)        |
| C6 Bank extrato estilo lista        | C6 Bank app (referencia BR)         | Lista de transacoes clean com agrupamento por data; usar no U-03              |
| Binance Pay mobile (light mode)     | Binance Pay app                     | QR code de pagamento + confirmacao animada; usar no U-04 (Pix)                |

**PARTE 3 — PROMPT MESTRE v2 (BINANCE-STYLE)**

ATUALIZACOES vs v1: design system Binance completo, NexusTicker, NexusCandleChart, NexusOrderBook adaptado, NexusDepthChart, tipografia IBM Plex, densidade de informacao Binance-grade.

**TELA A-02 v2 — Dashboard Aplicante (Binance-Grade)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT v2 — TELA A-02: DASHBOARD APLICANTE (BINANCE-STYLE)</strong></p>
<p>Crie o dashboard do investidor NEXUS no estilo BINANCE — alta densidade de informacao,</p>
<p>dark mode profundo (#0B0E11), tipografia IBM Plex Sans/Mono, cantos menos arredondados (4-8px).</p>
<p>TOPBAR (56px, fixed): NexusTicker scrollando — metricas das verticais em tempo real</p>
<p>Ex: [SAUDE 3,5% ▲0,1%] [EDUCACAO 3,8% — 0] [TRANSPORTE 4,0% ▼0,2%] [AGRO 4,8% ▲0,3%]</p>
<p>Fundo: --bnb-bg-card | border-bottom: 1px --bnb-border | Auto-scroll | Pause ao hover</p>
<p>SIDEBAR (240px): Logo NEXUS (hexagono dourado) | Avatar + nome + Tier badge amarelo</p>
<p>Menu com icones Lucide: Dashboard / Portfolio / Mercado / Contratos / Gerente / Relatorios</p>
<p>Active state: border-left 3px --bnb-yellow + bg --bnb-bg-hover</p>
<p>Footer: versao | status dot verde 'Online' | link 'ODOO Console'</p>
<p>AREA PRINCIPAL — LAYOUT BINANCE (3 zonas verticais):</p>
<p>ZONA SUPERIOR (full width, 4 KPI cards lado a lado):</p>
<p>Cada card: label 12px uppercase grey2 + valor IBM Plex Mono 28px + delta 14px (verde/vermelho)</p>
<p>Card 1: CAPITAL APLICADO — valor R$ + delta vs ontem</p>
<p>Card 2: RENDIMENTO DO MES — valor R$ + percentual vs meta (badge amarelo)</p>
<p>Card 3: CAPITAL EM USO — valor R$ + barra de progresso fina (4px height, estilo Binance)</p>
<p>Card 4: ADIMPLENCIA — percentual grande + dot verde pulsando se &gt;93%</p>
<p>ZONA MEDIA — SPLIT BINANCE-STYLE (70/30):</p>
<p>ESQUERDA (70%): NexusCandleChart — evolucao do portfolio ao longo do tempo</p>
<p>Candles representam: abertura/fechamento do periodo (semanal ou mensal)</p>
<p>Cores: verde se rendimento &gt; meta | vermelho se abaixo da meta</p>
<p>Volume bars abaixo: volume de transacoes no periodo</p>
<p>Controles: [1S] [1M] [3M] [6M] [1A] [MAX] — exatamente como Binance</p>
<p>Indicadores tecnicos opcionais: MA7, MA30 (medias moveis de retorno)</p>
<p>DIREITA (30%): NexusOrderBook adaptado — 'BOOK DE CONTRATOS'</p>
<p>Topo: titulo 'CONTRATOS ATIVOS' | sub: 'Preco = Taxa de Retorno'</p>
<p>Lado Verde (Adimplentes): lista de verticais ordenada por retorno decrescente</p>
<p>[VERTICAL] [RETORNO%] [QTD CONTRATOS] — com barra de fundo verde proporcional</p>
<p>Separador central: percentual total de adimplencia (numero grande, cor dinamica)</p>
<p>Lado Vermelho (Inadimplentes): verticais com contratos inadimplentes</p>
<p>[VERTICAL] [VALOR EXPOSTO] [CONTRATOS] — com barra de fundo vermelho</p>
<p>ZONA INFERIOR (full width): NexusDataGrid — tabela de contratos recentes</p>
<p>Colunas: [HASH] [VERTICAL] [USUARIO ID] [VALOR] [RETORNO%] [STATUS badge] [VENCIMENTO] [ACOES]</p>
<p>Row height: 40px | Hover: bg --bnb-bg-hover | Status: badge Binance-style</p>
<p>Acoes: icone olho (ver) | icone mercado (listar no mercado sec.) | icone sino (alertar)</p></td>
</tr>
</tbody>
</table>

**TELA A-03 v2 — Composer de Portfolio (Binance-Grade)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT v2 — TELA A-03: COMPOSER (BINANCE-STYLE)</strong></p>
<p>Redesign do Composer no estilo da tela de compra de cripto do Binance.</p>
<p>LAYOUT: Tela full-width dividida em 2 grandes paineis (esquerda + direita) + topbar de contexto.</p>
<p>TOPBAR DE CONTEXTO (fundo --bnb-bg-card, border-bottom):</p>
<p>'Compor Portfolio NEXUS' | [Conservador] [Moderado] [Arrojado] tabs (estilo Binance tabs)</p>
<p>Ao selecionar tab: preenche automaticamente o composer com configuracao sugerida</p>
<p>PAINEL ESQUERDO (480px) — CONFIGURADOR (estilo formulario de ordem Binance):</p>
<p>Label: 'VALOR A APLICAR' | Input numerico grande (IBM Plex Mono 28px) com prefixo R$</p>
<p>Abaixo: slider Binance-style (thumb quadrado, track fino dourado)</p>
<p>Quick amounts: [R$ 10k] [R$ 50k] [R$ 100k] [R$ 500k] — chips clicaveis</p>
<p>Label: 'PRAZO DO CONTRATO' | Select estilo Binance: [18M] [24M] [36M]</p>
<p>Label: 'DISTRIBUICAO POR VERTICAL'</p>
<p>Grid de verticais (3 colunas): cada vertical como um 'par de ativo'</p>
<p>[icone] SAUDE | 3,5% | slider % alocacao | badge BAIXO RISCO</p>
<p>Estilo exatamente como a grade de pares BTC/USDT da Binance</p>
<p>Aviso amber se concentracao &gt; 25%: linha vermelha no slider + tooltip</p>
<p>Botao 'APLICAR AGORA' (full width, --bnb-yellow, texto preto, 48px height)</p>
<p>Embaixo: 'Taxa de servico: 0%' | 'Prazo de ativacao: 60 dias' | 'Hash gerado apos confirmacao'</p>
<p>PAINEL DIREITO (flex) — PREVIEW + FORECAST (estilo painel de mercado Binance):</p>
<p>Topo: 'PREVIEW DO PORTFOLIO' | hash placeholder 'NXS-????...????' em NexusHash</p>
<p>NexusDepthChart: verde = retorno projetado acumulado | vermelho = inadimplencia projetada</p>
<p>X-axis: meses do contrato | Y-axis: R$ | Shaded area entre as duas curvas</p>
<p>Tooltip ao hover: mes X | retorno R$ Y | inadimplencia R$ Z | saldo liquido R$ W</p>
<p>Tabela de cenarios (3 linhas, estilo compact Binance):</p>
<p>[CENARIO] [RETORNO TOTAL] [ADIMPLENCIA] [LUCRO LIQUIDO]</p>
<p>Pessimista (vermelho) | Base (amarelo) | Otimista (verde)</p>
<p>Box 'RESUMO DA ORDEM' (fundo --bnb-bg-input):</p>
<p>Capital: R$ X | Duracao: 18M | Verticais: N | Retorno estimado: R$ Y (Z%)</p>
<p>Exposicao maxima a risco: R$ W | Score medio projetado: A+</p></td>
</tr>
</tbody>
</table>

**TELA B-01 v2 — 360 Board (Bloomberg + Grafana style)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT v2 — TELA B-01: 360 BOARD (BLOOMBERG/GRAFANA STYLE)</strong></p>
<p>Redesign do 360 Board como uma grade de widgets drag-and-drop (estilo Grafana).</p>
<p>Layout completamente customizavel pelo BOARD — cada modulo e um widget independente.</p>
<p>TOPBAR BINANCE-STYLE (64px):</p>
<p>Logo | 'NEXUS 360 — BOARD EXECUTIVO' | Data/hora UTC | Status operacional</p>
<p>Botao 'Editar Layout' (ativa modo drag-and-drop dos widgets)</p>
<p>Seletor de periodo global: [Hoje] [7D] [30D] [90D] [YTD] | Date range picker</p>
<p>Botao 'Exportar Dashboard PDF' | Botao 'Conectar BI' (dropdown: Power BI | Superset | Metabase | Grafana)</p>
<p>WIDGET GRID (12 colunas, drag-and-drop com react-grid-layout):</p>
<p>WIDGET 1 (3 cols) — KPI TICKER VERTICAL: lista de 8 KPIs scrollando</p>
<p>Capital Sob Gestao | Cartoes Ativos | Adimplencia% | MDR Hoje | Novos Usuarios | Receita Mes</p>
<p>Cada linha: label + valor IBM Plex Mono + delta verde/vermelho vs periodo anterior</p>
<p>WIDGET 2 (6 cols) — GRAFICO PRINCIPAL: NexusCandleChart da operacao completa</p>
<p>Metricas disponiveis para plotar (multiselect overlay): receita | carteira | adimplencia | MDR</p>
<p>Toggle: Candlestick | Line | Area | Bar (como Binance chart type selector)</p>
<p>WIDGET 3 (3 cols) — MAPA DE CALOR GEOGRAFICO:</p>
<p>Mapa BR estilo Binance dark | cores: mais claro = mais ativo</p>
<p>Hover em estado: popup com KPIs do estado</p>
<p>WIDGET 4 (4 cols) — BOOK DE EXECUTIVOS (Binance Order Book style):</p>
<p>Top performers (verde): Executivo | Usuarios | MDR | Adimplencia%</p>
<p>Bottom performers (vermelho): mesmos campos</p>
<p>Anonimizado para nao expor nomes se configurado</p>
<p>WIDGET 5 (4 cols) — DISTRIBUICAO DE VERTICAIS (donut + tabela):</p>
<p>Donut chart compacto + lista de verticais com: volume | retorno medio | adimplencia</p>
<p>WIDGET 6 (4 cols) — ALERTAS TEMPO REAL (live feed):</p>
<p>Stream de eventos: [critico/warning/info] | timestamp | descricao | link acao</p>
<p>Filtro por severidade | Auto-scroll | Pause ao hover</p>
<p>WIDGET 7 (6 cols) — P&amp;L WATERFALL CHART:</p>
<p>Receitas (verde) → Custos (vermelho) → EBITDA (amarelo) → Impostos (laranja) → Lucro (verde)</p>
<p>Estilo Bloomberg waterfall | Valores em R$ | Tooltip com breakdown detalhado</p>
<p>WIDGET 8 (6 cols) — CHAT IA DO BOARD:</p>
<p>Interface de chat minimalista | Pergunta em NL, resposta com grafico gerado on-the-fly</p>
<p>Exemplos pre-configurados como chips clicaveis abaixo do input</p>
<p>Ex: 'Qual vertical tem maior risco proximo mes?' | 'Projecao de receita em 90 dias?'</p></td>
</tr>
</tbody>
</table>

**PARTE 4 — INTEGRACAO COM BI OPEN SOURCE (Superset, Metabase, Grafana)**

A plataforma NEXUS expoe uma camada de API padronizada para integracao com as principais ferramentas de BI open source. Cada ferramenta tem seu endpoint dedicado e seu conjunto de datasets/dashboards pre-configurados como templates.

**4.1 Arquitetura da NEXUS Data API (para BI)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>NEXUS DATA API — ARQUITETURA GERAL</strong></p>
<p>Base URL: https://api.nexus.finance/v1/bi/</p>
<p>Autenticacao: Bearer Token (JWT) | Escopos: read:portfolio | read:board | read:executive | read:platform</p>
<p>Formato: JSON | Compressao: gzip | Rate limit: 1000 req/min (tier padrao) | 10000 req/min (institutional)</p>
<p>WebSocket: wss://stream.nexus.finance/v1/realtime — para dados em tempo real nos dashboards BI</p>
<p>ENDPOINTS PRINCIPAIS:</p>
<p>GET /metrics/platform — KPIs globais da plataforma (uso: Board)</p>
<p>GET /metrics/portfolio/{hash} — metricas do portfolio do Aplicante</p>
<p>GET /metrics/executive/{id} — metricas da base do Executivo (scope restrito por hash)</p>
<p>GET /contracts — lista de contratos com filtros (status, vertical, data)</p>
<p>GET /cashflow — fluxo de caixa por periodo (uso: CFO, ODOO)</p>
<p>GET /delinquency/heatmap — mapa de calor de inadimplencia por regiao/vertical</p>
<p>GET /merchants/performance — performance dos merchants por executivo/regiao</p>
<p>GET /users/segmentation — segmentacao anonimizada de usuarios por perfil</p>
<p>POST /ai/query — pergunta em linguagem natural, retorna dados estruturados</p>
<p>WEBHOOK EVENTS (para push de dados ao BI):</p>
<p>contract.deployed | contract.active | contract.repaid | contract.defaulted</p>
<p>payment.received | merchant.transaction | investor.joined | user.qualified</p></td>
</tr>
</tbody>
</table>

**4.2 Apache Superset — Integracao e Templates**

Apache Superset oferece a API REST mais completa entre os BI open source, com suporte a embed de dashboards via iframe seguro e autenticacao OAuth2.

| **Endpoint Superset**        | **Metodo** | **Acao NEXUS**                          | **Payload/Params**                           |
| ---------------------------- | ---------- | --------------------------------------- | -------------------------------------------- |
| /api/v1/dataset/             | POST       | Criar dataset NEXUS no Superset         | database\_id, table\_name (view SQL), schema |
| /api/v1/chart/               | POST       | Criar grafico (candlestick, donut, bar) | datasource\_id, viz\_type, params (JSON)     |
| /api/v1/dashboard/           | POST       | Criar dashboard de template             | title, position\_json (layout), published    |
| /api/v1/dashboard/{id}/embed | GET        | Obter token de embed para iframe        | allowed\_domains, resources                  |
| /api/v1/security/login       | POST       | Autenticar service account NEXUS        | username, password, provider: db             |
| /api/v1/security/refresh     | POST       | Renovar JWT token                       | refresh\_token                               |
| /api/v1/chart/data           | POST       | Executar query de grafico via API       | datasource, queries\[\], form\_data          |
| /api/v1/explore/form\_data   | GET        | Obter config de um chart existente      | chart\_id                                    |

<table>
<tbody>
<tr class="odd">
<td><p><strong>SUPERSET — DATASETS NEXUS PRE-CONFIGURADOS (SQL Views)</strong></p>
<p>-- VIEW 1: Portfolio Overview por Aplicante</p>
<p>CREATE VIEW nexus_portfolio_overview AS</p>
<p>SELECT investor_hash, portfolio_hash, vertical_name, total_value,</p>
<p>delinquency_rate, monthly_return, active_contracts, idle_value</p>
<p>FROM portfolios p JOIN investors i ON p.investor_id = i.id</p>
<p>JOIN verticals v ON p.vertical_id = v.id;</p>
<p>-- VIEW 2: Executive Performance</p>
<p>CREATE VIEW nexus_executive_kpis AS</p>
<p>SELECT exec_hash, region, active_users, mdr_current_month,</p>
<p>delinquency_rate, new_users_month, commission_estimate</p>
<p>FROM executives e JOIN user_bases ub ON e.id = ub.executive_id;</p>
<p>-- VIEW 3: Platform Financials (Board only)</p>
<p>CREATE VIEW nexus_financials AS</p>
<p>SELECT period, total_revenue, mdr_revenue, intermediation_fee,</p>
<p>operational_cost, ebitda, net_profit, aum, active_cards</p>
<p>FROM financials_daily;</p>
<p>-- VIEW 4: Delinquency Heatmap</p>
<p>CREATE VIEW nexus_delinquency_map AS</p>
<p>SELECT state_code, city, vertical_name, delinquency_count,</p>
<p>delinquency_value, delinquency_rate, period</p>
<p>FROM contracts c JOIN users u ON c.user_id = u.id</p>
<p>JOIN addresses a ON u.address_id = a.id;</p></td>
</tr>
</tbody>
</table>

**4.3 Metabase — Integracao e Templates**

Metabase e recomendado para os Executivos de Contas e usuarios nao-tecnicos da equipe. Sua API de embedding e mais simples e o MetaBot AI assistant permite perguntas em linguagem natural diretamente no dashboard.

| **Endpoint Metabase**           | **Metodo** | **Acao NEXUS**                         | **Notas**                                        |
| ------------------------------- | ---------- | -------------------------------------- | ------------------------------------------------ |
| /api/session                    | POST       | Login e obtencao de session token      | Usar service account dedicado para NEXUS         |
| /api/embed/token                | POST       | Gerar signed JWT para embed            | exp, resource.dashboard ou resource.question     |
| /api/dashboard/{id}             | GET        | Obter configuracao do dashboard        | Para clonar templates entre ambientes            |
| /api/card/                      | POST       | Criar nova 'question' (grafico/tabela) | dataset\_query, display, visualization\_settings |
| /api/database/                  | POST       | Registrar NEXUS DB no Metabase         | engine: postgres, host, port, dbname, user, pass |
| /api/table/{id}/query\_metadata | GET        | Obter schema de uma tabela/view        | Para auto-discovery dos datasets NEXUS           |
| /api/pulse/                     | POST       | Criar alerta de email/Slack agendado   | Para reports diarios dos Executivos              |
| /api/user/                      | POST       | Criar usuario com permissoes restritas | Grupos: board | executive | compliance           |

**4.4 Grafana — Integracao para Monitoramento em Tempo Real**

Grafana e indicado para o 360 Board em tempo real (operacional) e para o CTO/DevOps monitorarem a saude da plataforma. Excelente para dados de series temporais via WebSocket.

| **Endpoint Grafana**      | **Metodo** | **Acao NEXUS**                     | **Config**                                  |
| ------------------------- | ---------- | ---------------------------------- | ------------------------------------------- |
| /api/datasources          | POST       | Registrar NEXUS como datasource    | type: postgres ou infinity (para REST API)  |
| /api/dashboards/db        | POST       | Importar dashboard JSON template   | dashboard: {JSON do template NEXUS}         |
| /api/dashboards/uid/{uid} | GET        | Obter dashboard para clonar        | Para replicar em novos ambientes            |
| /api/alerts               | POST       | Criar alerta de inadimplencia      | condition, threshold, notification channel  |
| /api/annotations          | POST       | Anotar eventos na timeline         | Ex: lancamento de nova vertical, incidentes |
| /api/org/users            | POST       | Adicionar usuario Grafana com role | role: Admin|Editor|Viewer por dashboard     |
| /api/serviceaccounts      | POST       | Criar service account para NEXUS   | Para autenticacao programatica via API key  |

<table>
<tbody>
<tr class="odd">
<td><p><strong>GRAFANA — DATASOURCE INFINITY (REST API NEXUS → Grafana em tempo real)</strong></p>
<p>Plugin: Infinity datasource (suporte nativo a REST/JSON/GraphQL)</p>
<p>Configuracao do datasource:</p>
<p>URL: https://api.nexus.finance/v1/bi/</p>
<p>Auth: Bearer token (service account JWT)</p>
<p>Headers: Content-Type: application/json | X-Nexus-Scope: read:board</p>
<p>Panels configurados via Infinity:</p>
<p>Panel 1: Stat — Capital Sob Gestao</p>
<p>URL: /metrics/platform | JSONPath: $.data.aum | Refresh: 30s</p>
<p>Panel 2: Time series — Transacoes por hora</p>
<p>URL: /metrics/platform/hourly?period=24h | JSONPath: $.data.transactions[*]</p>
<p>Panel 3: Gauge — Taxa de Adimplencia</p>
<p>URL: /metrics/platform | JSONPath: $.data.delinquency_rate | Thresholds: 0=red 7=yellow 95=green</p>
<p>Panel 4: Geomap — Calor geografico</p>
<p>URL: /delinquency/heatmap | Formato: GeoJSON | Refresh: 5min</p>
<p>Panel 5: Logs panel — Stream de eventos via WebSocket</p>
<p>URL: wss://stream.nexus.finance/v1/realtime | Filter: level=critical</p></td>
</tr>
</tbody>
</table>

**PARTE 5 — POWER BI REST API E TEMPLATES (.PBIX)**

Power BI e a ferramenta mais usada por gestores e diretores financeiros no Brasil. A integracao NEXUS-PowerBI permite: (1) embed de relatorios no 360 Board, (2) distribuicao automatica de relatorios para Aplicantes e Executivos, (3) templates .pbix prontos para importar e conectar ao banco de dados NEXUS.

**5.1 Arquitetura de Integracao Power BI**

<table>
<tbody>
<tr class="odd">
<td><p><strong>ARQUITETURA NEXUS → POWER BI</strong></p>
<p>METODO 1 — POWER BI EMBEDDED (recomendado para o 360 Board):</p>
<p>A plataforma NEXUS embeda relatorios Power BI diretamente no frontend via JavaScript SDK</p>
<p>Autenticacao: Azure AD App Registration (service principal) — sem login do usuario necessario</p>
<p>Token: POST /generateToken → embed token com validade de 1h (renovacao automatica)</p>
<p>Workspace: NEXUS cria um Workspace dedicado no Power BI Service por cliente institucional</p>
<p>METODO 2 — POWER BI REST API (para automacao e gestao):</p>
<p>Base URL: https://api.powerbi.com/v1.0/myorg/</p>
<p>Autenticacao: OAuth2 com Azure AD | Escopos: Report.ReadWrite.All | Dataset.ReadWrite.All</p>
<p>Uso: deploy automatico de relatorios, refresh de datasets, criacao de dashboards por Aplicante</p>
<p>METODO 3 — DIRECT QUERY (para dados em tempo real):</p>
<p>Power BI conecta diretamente ao PostgreSQL da NEXUS via gateway</p>
<p>As views SQL (criadas no Superset — secao 4.2) sao reutilizadas aqui</p>
<p>Refresh: Direct Query (sem cache) para relatorios do Board | Scheduled para relatorios do Aplicante</p></td>
</tr>
</tbody>
</table>

**5.2 Endpoints Power BI REST API — NEXUS Integration**

| **Endpoint Power BI**                                           | **Metodo** | **Acao NEXUS**                          | **Parametros Chave**                                  |
| --------------------------------------------------------------- | ---------- | --------------------------------------- | ----------------------------------------------------- |
| POST /groups/{groupId}/reports/{reportId}/GenerateToken         | POST       | Gerar embed token para 360 Board        | accessLevel: View | identities: \[{username, roles}\] |
| POST /groups/{groupId}/datasets/{datasetId}/refreshes           | POST       | Forcar refresh do dataset NEXUS         | notifyOption: MailOnFailure                           |
| POST /groups/{groupId}/imports                                  | POST       | Deploy de novo relatorio .pbix          | datasetDisplayName, nameConflict: Overwrite           |
| GET /groups/{groupId}/reports                                   | GET        | Listar todos os relatorios do workspace | filter, top, skip para paginacao                      |
| POST /groups/{groupId}/dashboards                               | POST       | Criar dashboard programaticamente       | name: 'Portfolio {hash} - {mes/ano}'                  |
| POST /groups/{groupId}/dashboards/{id}/tiles                    | POST       | Adicionar tile ao dashboard             | reportId, visualizationId, rowSpan, columnSpan        |
| POST /groups                                                    | POST       | Criar workspace por Aplicante           | name: 'NEXUS-Aplicante-{hash}'                        |
| POST /groups/{groupId}/users                                    | POST       | Dar acesso ao Aplicante ao workspace    | emailAddress, groupUserAccessRight: Viewer            |
| GET /groups/{groupId}/datasets/{id}/parameters                  | GET        | Obter parametros do dataset             | Para verificar conexao com DB NEXUS                   |
| PATCH /groups/{groupId}/datasets/{id}/Default/updatedParameters | PATCH      | Atualizar connection string             | Para apontar para ambiente prod/staging               |

**5.3 Templates Power BI (.PBIX) — Especificacao para Construcao**

Os seguintes templates devem ser construidos e distribuidos aos usuarios da plataforma. Cada template e um arquivo .PBIX parametrizado que conecta automaticamente ao banco NEXUS ao ser importado.

| **Template .PBIX**               | **Destinatario**                         | **Paginas do Relatorio**                                                      | **Fonte de Dados**               | **Refresh**             |
| -------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------- | ----------------------- |
| NEXUS\_Portfolio\_Aplicante.pbix | Aplicante (individual)                   | 1:Overview | 2:Por Vertical | 3:Contratos | 4:Forecast | 5:Fiscal             | View: nexus\_portfolio\_overview | Agendado: diario 6h     |
| NEXUS\_Executive\_Dashboard.pbix | Executivo de Contas                      | 1:Minha Base | 2:Adimplencia | 3:Merchants | 4:Comissoes | 5:Mapa             | View: nexus\_executive\_kpis     | Agendado: hora em hora  |
| NEXUS\_Board\_Financial.pbix     | CFO / Board / CEO                        | 1:P\&L | 2:Fluxo de Caixa | 3:Receitas | 4:Custos | 5:Projecoes               | View: nexus\_financials          | Direct Query            |
| NEXUS\_Board\_Operational.pbix   | COO / Diretores                          | 1:Cartoes Ativos | 2:Verticais | 3:Executivos | 4:Mapa BR | 5:Alertas         | View: nexus\_operational         | Direct Query            |
| NEXUS\_Risk\_Report.pbix         | CRO / Compliance                         | 1:Adimplencia | 2:Heatmap | 3:Stress Test | 4:VaR | 5:COAF Alertas            | View: nexus\_delinquency\_map    | Direct Query            |
| NEXUS\_Investor\_Report.pbix     | Relatorio mensal p/ Aplicante (PDF auto) | 1:Resumo Mes | 2:Rendimentos | 3:Inadimplencia | 4:Forecast | 5:Fiscal (DARF) | View: nexus\_portfolio\_overview | Mensal: dia 5           |
| NEXUS\_Regulatory\_Bacen.pbix    | CFO para reporte SCR Bacen               | 1:Carteira Total | 2:Operacoes | 3:Provisoes | 4:Capital Reg.                 | View: nexus\_regulatory          | Mensal: ultimo dia util |

**5.4 Especificacao dos Templates — Paginas e Visuais**

<table>
<tbody>
<tr class="odd">
<td><p><strong>TEMPLATE: NEXUS_Portfolio_Aplicante.pbix — ESPECIFICACAO COMPLETA</strong></p>
<p>TEMA: Importar tema JSON 'NEXUS Dark Theme' — fundo #0B0E11, amarelo #F0B90B, verde #03C076</p>
<p>PAGINA 1 — OVERVIEW DO PORTFOLIO:</p>
<p>Visual 1: Card — Capital Total Aplicado (R$) | Condicional: verde se crescendo</p>
<p>Visual 2: Card — Rendimento do Mes (R$ e %) | Seta dinamica verde/vermelho</p>
<p>Visual 3: Card — Taxa de Adimplencia (%) | Gauge de 0 a 100</p>
<p>Visual 4: Card — Capital em Uso vs Ocioso | 2 barras side-by-side</p>
<p>Visual 5: Line chart — Evolucao do capital nos ultimos 12 meses</p>
<p>Visual 6: Donut chart — Distribuicao por vertical (slice por vertical)</p>
<p>Filtros de pagina: Data picker | Vertical (multiselect)</p>
<p>PAGINA 2 — POR VERTICAL:</p>
<p>Visual 1: Matrix table — Vertical x Metricas (valor, retorno%, adimplencia%, qtd contratos)</p>
<p>Visual 2: Bar chart — Retorno por vertical (ordenado decrescente)</p>
<p>Visual 3: Scatter plot — Risco vs Retorno por vertical (bolhas = tamanho da exposicao)</p>
<p>Visual 4: Waterfall — variacao de retorno vs mes anterior por vertical</p>
<p>PAGINA 3 — CONTRATOS:</p>
<p>Visual 1: Table — lista de contratos com colunas: hash, vertical, estado, valor, retorno, vencimento</p>
<p>Visual 2: Bar chart — contratos por estado (ativo/ocioso/repago/inadimplente)</p>
<p>Visual 3: Map (se geo disponivel) — distribuicao geografica dos contratos</p>
<p>Filtro: Estado do contrato | Vertical | Faixa de valor</p>
<p>PAGINA 4 — FORECAST:</p>
<p>Visual 1: Line chart — projecao de capital + juros compostos em 3 cenarios ate fim do contrato</p>
<p>Visual 2: Card — retorno total projetado (cenario base)</p>
<p>Visual 3: What-if parameter — slider de taxa de inadimplencia para stress test</p>
<p>Visual 4: KPI com target — meta de retorno vs projecao atual</p>
<p>PAGINA 5 — FISCAL (DARF helper):</p>
<p>Visual 1: Table — rendimentos por mes (base de calculo IR)</p>
<p>Visual 2: Card — Total de IR estimado no periodo</p>
<p>Visual 3: Card — Valor de DARF a pagar este trimestre</p>
<p>Botao: 'Gerar PDF para Contador' (Exportar pagina como PDF automatico)</p>
<p>Aviso: 'Este relatorio e informativo. Consulte seu contador para declaracao oficial.'</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>TEMA JSON NEXUS PARA POWER BI (colar em: Ver &gt; Temas &gt; Personalizar tema atual)</strong></p>
<p>{</p>
<p>"name": "NEXUS Dark Financial",</p>
<p>"dataColors": ["#F0B90B","#03C076","#F6465C","#0091FF","#6C3ABD","#F39C12","#00B4D8","#848E9C"],</p>
<p>"background": "#0B0E11",</p>
<p>"foreground": "#EAECEF",</p>
<p>"tableAccent": "#F0B90B",</p>
<p>"visualStyles": {</p>
<p>"page": { "*": { "background": [{"color": {"solid": {"color": "#0B0E11"}}}] } },</p>
<p>"card": { "*": { "labels": [{"color": {"solid": {"color": "#F0B90B"}}}] } },</p>
<p>"lineChart": { "*": { "plotArea": [{"transparency": 90}] } }</p>
<p>}</p>
<p>}</p></td>
</tr>
</tbody>
</table>

**PARTE 6 — COMPARATIVO FERRAMENTAS BI E RECOMENDACAO POR PERFIL**

| **Criterio**          | **Apache Superset**                 | **Metabase**                    | **Grafana**                    | **Power BI**                       |
| --------------------- | ----------------------------------- | ------------------------------- | ------------------------------ | ---------------------------------- |
| Licenca               | Open Source (Apache 2.0) — gratuito | Open Source + Plano pago        | Open Source + Enterprise       | Pago (R$ 60/usuario/mes)           |
| Embed em app React    | ★★★★★ — API + token de embed        | ★★★★☆ — embed signed JWT        | ★★★★★ — iframe + provisioning  | ★★★★★ — SDK JavaScript oficial     |
| Real-time / WebSocket | ★★★★☆ — via live datasets           | ★★★☆☆ — polling apenas          | ★★★★★ — nativo, excelente      | ★★★☆☆ — via DirectQuery            |
| Facilidade de uso     | ★★★☆☆ — tecnico (SQL obrigatorio)   | ★★★★★ — mais facil de todos     | ★★★☆☆ — tecnico (PromQL/JSON)  | ★★★★☆ — Power Query (M)            |
| Drag-and-drop         | ★★★★☆ — Smart Dashboard Builder     | ★★★★☆ — intuitivo               | ★★★★★ — grid customizavel      | ★★★★★ — canvas visual              |
| Conectores nativos    | 70+ databases/APIs                  | 50+ databases                   | 100+ datasources com plugins   | 300+ conectores nativos            |
| IA/NL Query           | Askdata integration (beta)          | MetaBot (2025, excelente)       | Experimental com LLMs          | Copilot (Microsoft 365)            |
| Deploy self-hosted    | Docker Compose — facil              | Docker — muito facil            | Docker — padrao de mercado     | Requer cloud Azure/365             |
| Perfil ideal NEXUS    | CTO / Data Engineers / Board tech   | Executivos de Contas / Gerentes | DevOps / CTO / Real-time Board | CFO / Diretores / Aplicantes inst. |
| Prioridade NEXUS      | ★★★★☆ — BI principal open source    | ★★★★★ — para usuarios campo     | ★★★★☆ — monitoramento ops      | ★★★★★ — relatorios executivos      |

**RECOMENDACAO NEXUS: Implementar TODOS os 4 de forma paralela com papeis distintos — Grafana para monitoramento operacional em tempo real (DevOps + Board live) | Metabase para Executivos de Contas e gerentes de campo (facilidade) | Superset para analistas de dados e BI corporativo (flexibilidade SQL) | Power BI para relatorios executivos e distribuicao a Aplicantes institucionais (credibilidade).**

*NEXUS UI Specification v2.0 | Binance-Grade Design + BI Integration | Abril 2026 | Confidencial*
