---
title: "NEXUS — NEXUS_UI_Prompt_Master_v3_Dribbble_Full"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>NEXUS</strong></p>
<p>UI/UX Prompt Master v3</p>
<p>Binance Design System + Dribbble Reference Library + Full BI Integration</p>
<p>React 18 · TypeScript · Tailwind CSS · shadcn/ui · lightweight-charts · Framer Motion</p></td>
</tr>
</tbody>
</table>

> **1. Por que Binance Style para o NEXUS?**

O estilo Binance foi escolhido por ser o padrão de-facto para plataformas financeiras de alta densidade de dados. Ao contrário do estilo OpenSea (NFT marketplace — foco em imagens, espaçamento generoso, identidade visual de coleção), o Binance prioriza legibilidade de métricas, densidade informacional e cognição rápida em ambiente de trading.

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dimensão</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>OpenSea (v1)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Binance (v3)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Impacto no NEXUS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Fundo</p>
</blockquote></td>
<td><blockquote>
<p>Navy (#1A1D2E)</p>
</blockquote></td>
<td><blockquote>
<p>Preto (#0B0E11)</p>
</blockquote></td>
<td><blockquote>
<p>Menor fadiga visual em uso contínuo</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cards</p>
</blockquote></td>
<td><blockquote>
<p>Glass morphism</p>
</blockquote></td>
<td><blockquote>
<p>Border sólida #2B3139</p>
</blockquote></td>
<td><blockquote>
<p>Hierarquia mais clara em dashboards</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Border-radius</p>
</blockquote></td>
<td><blockquote>
<p>16–24px</p>
</blockquote></td>
<td><blockquote>
<p>4–8px</p>
</blockquote></td>
<td><blockquote>
<p>Mais profissional para BI corporativo</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tipografia</p>
</blockquote></td>
<td><blockquote>
<p>Inter</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans/Mono</p>
</blockquote></td>
<td><blockquote>
<p>Mono para números — leitura precisa</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sombra</p>
</blockquote></td>
<td><blockquote>
<p>Drop shadow</p>
</blockquote></td>
<td><blockquote>
<p>Sem sombra (borda)</p>
</blockquote></td>
<td><blockquote>
<p>Performance melhor em tabelas densas</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Gráficos</p>
</blockquote></td>
<td><blockquote>
<p>Area chart simples</p>
</blockquote></td>
<td><blockquote>
<p>Candlestick TradingView</p>
</blockquote></td>
<td><blockquote>
<p>Mostra volatilidade de portfólio</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Estado hover</p>
</blockquote></td>
<td><blockquote>
<p>Escala (scale)</p>
</blockquote></td>
<td><blockquote>
<p>Bg muda (#1E2329)</p>
</blockquote></td>
<td><blockquote>
<p>Menos distração, mais foco</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CTA primário</p>
</blockquote></td>
<td><blockquote>
<p>Gradiente roxo</p>
</blockquote></td>
<td><blockquote>
<p>Sólido #F0B90B</p>
</blockquote></td>
<td><blockquote>
<p>Reconhecimento imediato de ação</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **2. Design Tokens — Sistema de Cores e Tipografia**

**2.1 Paleta de Cores**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Token</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Hex</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Uso</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>bg-deep</p>
</blockquote></td>
<td><blockquote>
<p>#0B0E11</p>
</blockquote></td>
<td><blockquote>
<p>Canvas principal, fundo máximo</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>bg-card</p>
</blockquote></td>
<td><blockquote>
<p>#161A1E</p>
</blockquote></td>
<td><blockquote>
<p>Cards, painéis, sidebars</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg-hover</p>
</blockquote></td>
<td><blockquote>
<p>#1E2329</p>
</blockquote></td>
<td><blockquote>
<p>Hover state de rows e itens</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>border</p>
</blockquote></td>
<td><blockquote>
<p>#2B3139</p>
</blockquote></td>
<td><blockquote>
<p>Todas as bordas e divisores</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>gold</p>
</blockquote></td>
<td><blockquote>
<p>#F0B90B</p>
</blockquote></td>
<td><blockquote>
<p>CTA primário, destaques, ícones ativos</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>green</p>
</blockquote></td>
<td><blockquote>
<p>#03C076</p>
</blockquote></td>
<td><blockquote>
<p>Valores positivos, rentabilidade, sucesso</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>red</p>
</blockquote></td>
<td><blockquote>
<p>#F6465C</p>
</blockquote></td>
<td><blockquote>
<p>Valores negativos, inadimplência, alerta</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>blue</p>
</blockquote></td>
<td><blockquote>
<p>#0091FF</p>
</blockquote></td>
<td><blockquote>
<p>Links, info, badge secundário</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>purple</p>
</blockquote></td>
<td><blockquote>
<p>#6C3ABD</p>
</blockquote></td>
<td><blockquote>
<p>Premium tier, Aplicante Qualificado</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text-pri</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
<td><blockquote>
<p>Texto principal, labels</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>text-sec</p>
</blockquote></td>
<td><blockquote>
<p>#848E9C</p>
</blockquote></td>
<td><blockquote>
<p>Labels secundários, placeholders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text-dis</p>
</blockquote></td>
<td><blockquote>
<p>#474D57</p>
</blockquote></td>
<td><blockquote>
<p>Disabled, linhas de separação leve</p>
</blockquote></td>
</tr>
</tbody>
</table>

**2.2 Tipografia — IBM Plex**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Elemento</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fonte</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tamanho</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Peso</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cor</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Display (hero número)</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Mono</p>
</blockquote></td>
<td><blockquote>
<p>32–48px</p>
</blockquote></td>
<td><blockquote>
<p>700</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H1 — título de seção</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>24px</p>
</blockquote></td>
<td><blockquote>
<p>600</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H2 — subtítulo card</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>18px</p>
</blockquote></td>
<td><blockquote>
<p>600</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H3 — label de campo</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>14px</p>
</blockquote></td>
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>#848E9C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Body</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>14px</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Caption / meta</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>12px</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>#848E9C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Código / hash</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Mono</p>
</blockquote></td>
<td><blockquote>
<p>12px</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>#F0B90B</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tabela numérica</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Mono</p>
</blockquote></td>
<td><blockquote>
<p>13px</p>
</blockquote></td>
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>#EAECEF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Badge / chip</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Sans</p>
</blockquote></td>
<td><blockquote>
<p>11px</p>
</blockquote></td>
<td><blockquote>
<p>600</p>
</blockquote></td>
<td><blockquote>
<p>contextual</p>
</blockquote></td>
</tr>
</tbody>
</table>

**2.3 Espaçamento e Grid**

**Base unit: 4px. Escala: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px.**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Elemento</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Valor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DXA equiv.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Card padding interno</p>
</blockquote></td>
<td><blockquote>
<p>16px</p>
</blockquote></td>
<td><blockquote>
<p>240</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Gap entre cards (grid)</p>
</blockquote></td>
<td><blockquote>
<p>12px</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sidebar width</p>
</blockquote></td>
<td><blockquote>
<p>240px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Topbar height</p>
</blockquote></td>
<td><blockquote>
<p>56px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Border-radius card</p>
</blockquote></td>
<td><blockquote>
<p>6px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Border-radius button</p>
</blockquote></td>
<td><blockquote>
<p>4px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Border-radius chip</p>
</blockquote></td>
<td><blockquote>
<p>100px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Border width padrão</p>
</blockquote></td>
<td><blockquote>
<p>1px solid #2B3139</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Icon size padrão</p>
</blockquote></td>
<td><blockquote>
<p>16x16px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Table row height</p>
</blockquote></td>
<td><blockquote>
<p>48px</p>
</blockquote></td>
<td><blockquote>
<p>—</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **3. Biblioteca de Referências Dribbble**

Cada tela do NEXUS é mapeada para uma ou mais referências de alta votação do Dribbble. O gerador de IA (v0.dev / Lovable / Bolt.new) deve receber estas referências para estilo e densidade visual.

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Nome</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Autor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Destaque</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Aplicação no NEXUS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>REF-01</p>
</blockquote></td>
<td><blockquote>
<p>ChainScope – Crypto Dashboard</p>
</blockquote></td>
<td><blockquote>
<p>Fikri Ruslandi</p>
</blockquote></td>
<td><blockquote>
<p>25.996k</p>
</blockquote></td>
<td><blockquote>
<p>Dark mode denso, portfolio overview, candle semanal, módulo de conversão inline, métricas de staking. Fundo #0D1117, cards com borda #21262D. Aplica em: A-01, A-02, D-01.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REF-02</p>
</blockquote></td>
<td><blockquote>
<p>Crystal Stock App</p>
</blockquote></td>
<td><blockquote>
<p>Milkinside Team</p>
</blockquote></td>
<td><blockquote>
<p>869 likes / 284k views</p>
</blockquote></td>
<td><blockquote>
<p>App mobile de stocks mais curtido do Dribbble. Cards de preço com sparkline integrado, lista de watchlist compacta, detalhe de ativo com área chart. Aplica em: A-03, E-01.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REF-03</p>
</blockquote></td>
<td><blockquote>
<p>FinVerse – Finance Dashboard</p>
</blockquote></td>
<td><blockquote>
<p>Mike Taylor</p>
</blockquote></td>
<td><blockquote>
<p>Alta avaliação</p>
</blockquote></td>
<td><blockquote>
<p>Dashboard financeiro full dark. Sidebar com ícones monocromáticos, KPI grid 4-colunas, gráfico de barras empilhadas para breakdown de categorias. Aplica em: A-01, C-01, D-01.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REF-04</p>
</blockquote></td>
<td><blockquote>
<p>Fintech Dashboard UI Dark Theme</p>
</blockquote></td>
<td><blockquote>
<p>Olga Furmanchuk</p>
</blockquote></td>
<td><blockquote>
<p>Destaque Dribbble</p>
</blockquote></td>
<td><blockquote>
<p>Fintech dark de referência. Painel esquerdo de navegação com seções colapsáveis, header com search e notificações, tabela de transações com filtros inline. Aplica em: B-01, B-02.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REF-05</p>
</blockquote></td>
<td><blockquote>
<p>Overpay – Finance Dashboard UI Kit</p>
</blockquote></td>
<td><blockquote>
<p>Barly Design Team</p>
</blockquote></td>
<td><blockquote>
<p>50+ telas</p>
</blockquote></td>
<td><blockquote>
<p>Kit completo Light/Dark. Padrões de KPI card com delta % + sparkline. Card de saldo com gradiente sutil. Aplica em: A-01, B-01.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REF-06</p>
</blockquote></td>
<td><blockquote>
<p>Modern Financial Dashboard (Fintech/Corp)</p>
</blockquote></td>
<td><blockquote>
<p>Jahangir Hussain</p>
</blockquote></td>
<td><blockquote>
<p>2024</p>
</blockquote></td>
<td><blockquote>
<p>Dashboard corporativo com tema dark + accents laranja e azul. Breakdown de receita em donut chart, tabela de transações recentes, histórico de saques. Aplica em: D-02, F-01.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REF-07</p>
</blockquote></td>
<td><blockquote>
<p>Components Library for Fintech Dashboard</p>
</blockquote></td>
<td><blockquote>
<p>Ajo Jose</p>
</blockquote></td>
<td><blockquote>
<p>Lending/Borrowing</p>
</blockquote></td>
<td><blockquote>
<p>Biblioteca de componentes para plataforma de empréstimo digital indiana. Input de valor com slider, status badge de contrato (Active/Overdue/Paid), tabela de parcelas. Aplica em: B-01, B-03, E-02.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REF-08</p>
</blockquote></td>
<td><blockquote>
<p>Crypto Trading Dashboard UI Concept</p>
</blockquote></td>
<td><blockquote>
<p>Sheik Hassain / ADBUX</p>
</blockquote></td>
<td><blockquote>
<p>17.210k</p>
</blockquote></td>
<td><blockquote>
<p>Tela de trading com order book à direita, candle chart central com indicadores, lista de pares à esquerda com delta %. Aplica em: A-02, E-01, E-02.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REF-09</p>
</blockquote></td>
<td><blockquote>
<p>Fintech Dashboard UI Kit (Envato)</p>
</blockquote></td>
<td><blockquote>
<p>Envato Elements</p>
</blockquote></td>
<td><blockquote>
<p>UI Kit completo</p>
</blockquote></td>
<td><blockquote>
<p>Template profissional com Risk Score visual, mapa geográfico de risco, tabela de NPL por categoria. Aplica em: C-02, D-03, D-04.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REF-10</p>
</blockquote></td>
<td><blockquote>
<p>Binance Market Trade Dashboard</p>
</blockquote></td>
<td><blockquote>
<p>Figma Community</p>
</blockquote></td>
<td><blockquote>
<p>Binance oficial</p>
</blockquote></td>
<td><blockquote>
<p>Réplica fiel do Binance. Order book com acumulação, gráfico lightweight-charts, ticker strip no topo. Base de referência para todo Design System NEXUS. Aplica em: todos os módulos.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **4. Componentes Globais Reutilizáveis**

**4.1 NexusTopBar**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusTopBar</strong></p>
<p>Altura: 56px | Background: #161A1E | Borda inferior: 1px solid #2B3139</p>
<p>Esquerda: Logo NEXUS (texto IBM Plex Mono, 18px, bold, #F0B90B) + separador vertical + breadcrumb</p>
<p>Centro: NexusTicker horizontal (scroll automático com 12 métricas rotativas)</p>
<p>Direita: NotificationBell (badge vermelho com contagem) + Avatar + DropdownMenu</p>
<p>NexusTicker item: '[LABEL] [VALOR em IBM Plex Mono] [DELTA com seta + cor green/red]'</p>
<p>Ticker anima com CSS marquee ou Framer Motion (loop infinito, pausa no hover)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.2 NexusSidebar**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusSidebar</strong></p>
<p>Largura expandida: 240px | Recolhida: 64px | Transição: 200ms ease-in-out</p>
<p>Background: #161A1E | Borda direita: 1px solid #2B3139</p>
<p>Topo: Avatar + Nome do usuário + Role badge (chip colorido por perfil)</p>
<p>Nav items: ícone 20px + label | Ativo: bg #1E2329 + borda esquerda 3px #F0B90B + texto #EAECEF</p>
<p>Inativo: texto #848E9C | Hover: bg #1E2329 + texto #EAECEF</p>
<p>Rodapé sidebar: versão da plataforma + link de suporte</p>
<p>Grupos de nav: Dashboard / Portfólio / Mercado / Relatórios / Configurações</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.3 NexusKPICard**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusKPICard</strong></p>
<p>Dimensão: flex-1, mín 200px | Background: #161A1E | Borda: 1px solid #2B3139 | Radius: 6px</p>
<p>Padding interno: 16px | Layout: 2 linhas</p>
<p>Linha 1: Label (12px, #848E9C, uppercase, letter-spacing 0.5px) + ícone contextual (direita)</p>
<p>Linha 2: Valor principal (IBM Plex Mono, 28–32px, bold, #EAECEF)</p>
<p>Linha 3: Delta badge (chip: '+2.3% vs mês ant.' com bg verde/vermelho 15% opacity + texto full)</p>
<p>Linha 4: Sparkline 60px altura (Recharts ResponsiveContainer, sem eixos, cor contextual)</p>
<p>Hover: borda muda para #F0B90B com transition 150ms</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.4 NexusCandleChart**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusCandleChart</strong></p>
<p>Biblioteca: lightweight-charts (TradingView) — npm i lightweight-charts</p>
<p>Background: #0B0E11 | Grid lines: #1E2329 | Crosshair: #2B3139</p>
<p>Candle alta: #03C076 (body) + #03C076 (wick) | Candle baixa: #F6465C + #F6465C</p>
<p>Volume bars: altura 20% do chart, mesma cor do candle, opacity 0.4</p>
<p>Toolbar: seletor de período [1H | 4H | 1D | 1S | 1M] com botões estilo Binance</p>
<p>Tooltip (crosshair): card flutuante #161A1E com OHLCV formatado em IBM Plex Mono</p>
<p>Indicadores opcionais: MA7 (#F0B90B, dashed) + MA30 (#0091FF, dashed)</p>
<p>Adaptar para NEXUS: eixo Y = Rentabilidade acumulada do portfólio (%), eixo X = datas de liquidação</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.5 NexusOrderBook (adaptado para contratos)**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusOrderBook</strong></p>
<p>Inspiração: REF-08 (Sheik Hassain) + REF-10 (Binance Market Trade)</p>
<p>Adaptar ordem de compra/venda -&gt; contratos disponíveis / contratos liquidados</p>
<p>Coluna esquerda: 'Blocos Ativos' (verde) | Coluna direita: 'Blocos Liquidados' (vermelho)</p>
<p>Cada linha: Categoria (12 verticais) | Volume (R$ formatado) | Taxa (%) | Status badge</p>
<p>Barra de profundidade horizontal: largura proporcional ao volume, cores green/red</p>
<p>Atualização em tempo real via WebSocket (polling fallback a cada 5s)</p>
<p>Header: spread atual + timestamp última atualização</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.6 NexusDataGrid**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Especificação de Componente: NexusDataGrid</strong></p>
<p>Base: TanStack Table v8 (react-table) ou shadcn/ui DataTable</p>
<p>Header: sticky top | Background: #161A1E | Sort icon: seta dupla #848E9C -&gt; #F0B90B</p>
<p>Row height: 48px | Alternância: #0B0E11 / #161A1E</p>
<p>Row hover: background #1E2329 com transition 100ms</p>
<p>Colunas numéricas: IBM Plex Mono, alinhamento à direita</p>
<p>Status badges inline: chip arredondado (radius 100px) com cor semântica</p>
<p>Paginação: shadcn/ui Pagination, 20 itens/página padrão</p>
<p>Filtros inline: Input de busca + Select de status + DateRangePicker</p>
<p>Export: botão 'Exportar CSV' + 'Exportar XLSX' no header da grid</p>
</blockquote></td>
</tr>
</tbody>
</table>

**4.7 NexusStatusBadge**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Label PT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Background</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Texto</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Borda</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>Ativo</p>
</blockquote></td>
<td><blockquote>
<p>03C076/15</p>
</blockquote></td>
<td><blockquote>
<p>03C076</p>
</blockquote></td>
<td><blockquote>
<p>03C076</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OVERDUE</p>
</blockquote></td>
<td><blockquote>
<p>Inadimplente</p>
</blockquote></td>
<td><blockquote>
<p>F6465C/15</p>
</blockquote></td>
<td><blockquote>
<p>F6465C</p>
</blockquote></td>
<td><blockquote>
<p>F6465C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PENDING</p>
</blockquote></td>
<td><blockquote>
<p>Pendente</p>
</blockquote></td>
<td><blockquote>
<p>F0B90B/15</p>
</blockquote></td>
<td><blockquote>
<p>F0B90B</p>
</blockquote></td>
<td><blockquote>
<p>F0B90B</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LIQUIDATED</p>
</blockquote></td>
<td><blockquote>
<p>Liquidado</p>
</blockquote></td>
<td><blockquote>
<p>0091FF/15</p>
</blockquote></td>
<td><blockquote>
<p>0091FF</p>
</blockquote></td>
<td><blockquote>
<p>0091FF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BLOCKED</p>
</blockquote></td>
<td><blockquote>
<p>Bloqueado</p>
</blockquote></td>
<td><blockquote>
<p>474D57/15</p>
</blockquote></td>
<td><blockquote>
<p>848E9C</p>
</blockquote></td>
<td><blockquote>
<p>474D57</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREMIUM</p>
</blockquote></td>
<td><blockquote>
<p>Qualificado</p>
</blockquote></td>
<td><blockquote>
<p>6C3ABD/15</p>
</blockquote></td>
<td><blockquote>
<p>6C3ABD</p>
</blockquote></td>
<td><blockquote>
<p>6C3ABD</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **5. Módulo A — Aplicante (Investidor)**

Ator: Pessoa Física ou Jurídica que aporta capital na plataforma. Recebe 3–5% de retorno/mês. Capital fracionado em até 1.800 micro-contratos por portfólio.

<table>
<tbody>
<tr class="odd">
<td><strong>A-01</strong></td>
<td><blockquote>
<p><strong>Dashboard Principal do Aplicante</strong> [Ref: REF-01 ChainScope + REF-05 Overpay]</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Layout Grid**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Estrutura de Grid — A-01</strong></p>
<p>Layout: CSS Grid 12 colunas | Topbar (56px) + Sidebar (240px) + Main content area</p>
<p>Row 1: 4x NexusKPICard — [Saldo Total] [Rentabilidade Mês] [Portfólios Ativos] [Contratos Ativos]</p>
<p>Row 2: NexusCandleChart (8 colunas) + NexusOrderBook adaptado (4 colunas)</p>
<p>Row 3: Tabela de Portfólios (8 colunas) + Breakdown por Categoria (4 colunas — donut chart)</p>
<p>Row 4: Feed de Atividade Recente (largura total) com NexusStatusBadge inline</p>
<p>Gaps: 12px entre todos os elementos | Padding container: 24px</p>
</blockquote></td>
</tr>
</tbody>
</table>

**KPI Cards Detalhados — A-01**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Card</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Valor Principal</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Delta</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sparkline</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Ícone</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Saldo Total</p>
</blockquote></td>
<td><blockquote>
<p>R$ 47.830,00 (IBM Plex Mono 32px)</p>
</blockquote></td>
<td><blockquote>
<p>+12.4% este mês</p>
</blockquote></td>
<td><blockquote>
<p>Linha verde 60px</p>
</blockquote></td>
<td><blockquote>
<p>Carteira #F0B90B</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rentabilidade Mês</p>
</blockquote></td>
<td><blockquote>
<p>4.2% a.m. (IBM Plex Mono 32px)</p>
</blockquote></td>
<td><blockquote>
<p>+0.3% vs anterior</p>
</blockquote></td>
<td><blockquote>
<p>Área verde</p>
</blockquote></td>
<td><blockquote>
<p>TrendingUp #03C076</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Portfólios Ativos</p>
</blockquote></td>
<td><blockquote>
<p>3 (IBM Plex Sans 32px bold)</p>
</blockquote></td>
<td><blockquote>
<p>1 novo esta semana</p>
</blockquote></td>
<td><blockquote>
<p>Barras azuis</p>
</blockquote></td>
<td><blockquote>
<p>Briefcase #0091FF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Contratos Ativos</p>
</blockquote></td>
<td><blockquote>
<p>5.400 (IBM Plex Mono 28px)</p>
</blockquote></td>
<td><blockquote>
<p>98.2% adimplência</p>
</blockquote></td>
<td><blockquote>
<p>Linha verde</p>
</blockquote></td>
<td><blockquote>
<p>Link #03C076</p>
</blockquote></td>
</tr>
</tbody>
</table>

**NexusCandleChart — A-01**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Gráfico de Rentabilidade do Portfólio — Candle por Período</strong></p>
<p>Ref: REF-01 ChainScope (candle semanal de reward ratio)</p>
<p>Eixo Y: Rentabilidade acumulada (%) | Eixo X: Ciclos de liquidação (quinzenal)</p>
<p>Cada candle = abertura/fechamento/max/min de rentabilidade no período</p>
<p>Toolbar: [1C | 3C | 6C | 1A | Tudo] onde C = ciclo de cobrança</p>
<p>Overlay: MA7 em #F0B90B tracejado | Volume bars = volume de liquidações</p>
<p>Tooltip: Ciclo / Abertura / Fechamento / Máx / Mín / Liquidações / Taxa média</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Prompt Completo para Gerador de IA — A-01**

**Prompt A-01 — para v0.dev / Lovable / Bolt.new / Cursor**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Crie uma tela de Dashboard Principal para investidor (Aplicante) de plataforma P2P lending</p>
<p>chamada NEXUS. Use EXATAMENTE o Binance Design System:</p>
<p>PALETA:</p>
<p>bg: #0B0E11 (canvas) | card: #161A1E | border: #2B3139 | hover: #1E2329</p>
<p>gold: #F0B90B | green: #03C076 | red: #F6465C | blue: #0091FF</p>
<p>text-primary: #EAECEF | text-secondary: #848E9C</p>
<p>TIPOGRAFIA: IBM Plex Sans (labels, body) + IBM Plex Mono (todos os números)</p>
<p>Valores monetários: Mono 32px bold #EAECEF</p>
<p>Labels de KPI: Sans 12px uppercase letter-spacing-0.5 #848E9C</p>
<p>Delta badges: chip radius-full, bg opacity-15, texto full color</p>
<p>LAYOUT:</p>
<p>Sidebar esquerda 240px (#161A1E, borda #2B3139)</p>
<p>Topbar 56px com NexusTicker animado</p>
<p>Grid 12 colunas, gap 12px, padding 24px</p>
<p>ROW 1 — 4 KPI Cards iguais:</p>
<p>[Saldo Total R$47.830] [Rentabilidade 4.2%a.m.] [3 Portfólios] [5.400 Contratos]</p>
<p>Cada card: padding 16px, borda #2B3139, hover borda #F0B90B, sparkline recharts 60px</p>
<p>ROW 2 — split 8/4:</p>
<p>Esquerda (8col): Candle chart lightweight-charts, rentabilidade por ciclo,</p>
<p>toolbar [1C|3C|6C|1A], MA7 #F0B90B tracejado, volume bars opacity-40</p>
<p>Direita (4col): Order book adaptado — 'Blocos Ativos' (verde) vs 'Liquidados' (vermelho)</p>
<p>por categoria de consumo, barra de profundidade horizontal</p>
<p>ROW 3 — split 8/4:</p>
<p>Esquerda (8col): Tabela de portfólios (NexusDataGrid) colunas:</p>
<p>[Nome] [Aporte R$] [Contratos] [Rentab.%] [Adimplência%] [Status badge] [Ações]</p>
<p>Direita (4col): Donut chart (Recharts PieChart) breakdown por 12 categorias</p>
<p>legenda lateral com cor e percentual, hover mostra valor em R$</p>
<p>STACK: React 18 + TypeScript + Tailwind CSS + shadcn/ui + Recharts + lightweight-charts</p>
<p>Framer Motion para animações de entrada (fade+slide 300ms)</p>
<p>Usar apenas classes Tailwind utilitárias (sem CSS customizado)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>A-02</strong></td>
<td><blockquote>
<p><strong>Detalhe do Portfólio</strong> [Ref: REF-08 Crypto Trading + REF-10 Binance Market]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout e Componentes — A-02</strong></p>
<p>Header: Nome do portfólio + Categoria dominante + Status badge + Botões [Aportar] [Retirar]</p>
<p>Row 1: Stats bar horizontal — Aporte Total | Saldo Atual | Retorno R$ | Retorno % | Contratos | DPD bucket</p>
<p>Row 2 (split 7/5): Candle chart com histórico de ciclos | Painel de composição</p>
<p>Painel de composição: barras horizontais por categoria (12 verticais), cada barra = % do portfólio</p>
<p>Row 3: NexusDataGrid de micro-contratos — [ID hash curto] [Usuário] [Limite R$] [Uso%] [Status] [Próx. venc.]</p>
<p>Filtros: busca por hash + filtro status + filtro categoria + DateRange de emissão</p>
<p>Row 4: Timeline de eventos (MACRO HASH log) — cada evento com ícone, timestamp e hash parcial</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Prompt A-02**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Tela de detalhe de portfólio P2P lending NEXUS. Binance Design System idêntico ao A-01.</p>
<p>HEADER (sticky):</p>
<p>'Portfólio Saúde &amp; Educação' + chip categoria + NexusStatusBadge 'Ativo'</p>
<p>Botões: [Aportar +] gold background | [Retirar] ghost border</p>
<p>STATS BAR (1 linha, 6 métricas):</p>
<p>Aporte: R$10.000 | Saldo: R$11.240 | Retorno: +R$1.240 (+12.4%) verde</p>
<p>Contratos: 1.800/1.800 | Adimplência: 98.2% verde | DPD30: 1.8% amarelo</p>
<p>SPLIT 7/5:</p>
<p>Candle chart de rentabilidade por ciclo quinzenal (lightweight-charts)</p>
<p>Painel direito: barras de composição por categoria, cada barra animada (Framer Motion)</p>
<p>DATAGRID de contratos (TanStack Table):</p>
<p>Colunas: Hash | CPF mascarado | Limite | Uso atual | Status badge | Próximo vencimento</p>
<p>Row expansível: ao clicar abre MACRO HASH timeline do contrato específico</p>
<p>TIMELINE MACRO HASH (expandível no rodapé):</p>
<p>Cada evento: dot colorido + timestamp + tipo_evento + hash parcial (Mono #F0B90B)</p>
<p>Tipos: EMISSAO | COBRANCA | PAGAMENTO | BLOQUEIO | LIQUIDACAO</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>A-03</strong></td>
<td><blockquote>
<p><strong>Mercado Secundário — Aplicante View</strong> [Ref: REF-02 Crystal Stock + REF-08 Trading]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout e Componentes — A-03</strong></p>
<p>Ref: REF-02 Crystal Stock App (watchlist compacta + detalhe de ativo com área chart)</p>
<p>Esquerda: Lista de portfólios disponíveis para aquisição (tipo order book Binance)</p>
<p>Cada item da lista: Nome portfólio | Categoria | Rentab. histórica | Preço de transferência | Volume 24h</p>
<p>Centro: Candle chart do portfólio selecionado com histórico de performance</p>
<p>Direita: Painel de aquisição — formulário de oferta com slider de alocação parcial</p>
<p>Header: Volume total negociado hoje | Número de portfólios ofertados | Spread médio</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Prompt A-03**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Tela de mercado secundário para Aplicante NEXUS. Layout tipo Binance exchange.</p>
<p>TRÊS COLUNAS:</p>
<p>Esquerda (280px): Lista de portfólios com search e filtros de categoria/rentab.</p>
<p>Cada linha: nome + badge categoria + '4.2% a.m.' (verde Mono) + preço R$</p>
<p>Ativo selecionado: bg #1E2329 + borda esquerda 3px #F0B90B</p>
<p>Centro (flex-1): Candle chart lightweight-charts do portfólio selecionado</p>
<p>Toolbar período + indicadores MA | Abaixo: tabs [Descrição | Contratos | Histórico]</p>
<p>Direita (320px): Painel de compra/transferência</p>
<p>Preço de aquisição (Mono 24px bold gold) | Saldo disponível</p>
<p>Slider de alocação parcial (0-100% do portfólio) com valor em R$ ao lado</p>
<p>Projeção de retorno mensal baseada no histórico</p>
<p>Botão [Adquirir Portfólio] gold, full-width, radius-4px</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **6. Módulo B — Usuário (Tomador de Crédito)**

Ator: Pessoa física que recebe crédito via cartão pré-pago Visa/Mastercard. Limite R$500–R$2.500. Paga 6% de taxa sobre o uso total na data de vencimento da fatura.

<table>
<tbody>
<tr class="odd">
<td><strong>B-01</strong></td>
<td><blockquote>
<p><strong>Dashboard do Usuário — App Mobile (PWA)</strong> [Ref: REF-04 Fintech Dashboard Olga + REF-07 Components Lending]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout e Componentes — B-01</strong></p>
<p>Dispositivo alvo: Mobile first (375px) + Desktop (1440px) responsive</p>
<p>Ref: REF-04 (sidebar colapsável, tabela de transações) + REF-07 (status de contrato, parcelas)</p>
<p>Hero card: Representação visual do cartão pré-pago NEXUS (Visa/MC branding)</p>
<p>Saldo disponível (grande, IBM Plex Mono) + Limite total + % usado como barra de progresso</p>
<p>CTA primário: [Ver Fatura] gold | CTA secundário: [Bloquear Cartão] ghost red</p>
<p>Seção: Últimas Transações (lista compacta com ícone de categoria, valor, data)</p>
<p>Seção: Fatura do Ciclo Atual — breakdown por categoria de consumo (barras horizontais)</p>
<p>Seção: Score de Adimplência (gauge circular com valor e classificação)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Prompt B-01**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Dashboard mobile/PWA para tomador de crédito NEXUS. Design mobile-first.</p>
<p>Mesma paleta Binance. Componentes adaptados para toque.</p>
<p>HERO SECTION:</p>
<p>Cartão virtual com gradiente sutil (#161A1E -&gt; #1E2329)</p>
<p>Logo NEXUS + bandeira Visa/MC | Número mascarado •••• •••• •••• 4242</p>
<p>Nome do usuário | Validade | 'CRÉDITO PRÉ-PAGO'</p>
<p>Abaixo do cartão: 'Disponível: R$ 1.840,00' (Mono 32px bold gold)</p>
<p>Barra de uso: 'R$ 660 usados de R$ 2.500' — barra #F0B90B, fundo #2B3139</p>
<p>BOTÕES RÁPIDOS (grid 2x2 com ícones):</p>
<p>[Ver Fatura] [Histórico] [Bloquear] [Suporte]</p>
<p>ÚLTIMAS TRANSAÇÕES (lista):</p>
<p>Ícone categoria (12 opções com cores distintas) + Nome estabelecimento</p>
<p>Data + valor (vermelho para débito) | Status badge</p>
<p>'Ver todas' link em #F0B90B</p>
<p>FATURA CICLO:</p>
<p>Total: R$ 660,00 | Taxa 6%: R$ 39,60 | Total a pagar: R$ 699,60</p>
<p>Vencimento: countdown em chips [DD HH MM SS]</p>
<p>Breakdown: barras horizontais por categoria, animadas (Framer Motion)</p>
<p>SCORE ADIMPLÊNCIA:</p>
<p>Gauge semicircular (Recharts RadialBarChart) 0-1000</p>
<p>Classificação: Excelente/Bom/Regular/Ruim com cor semântica</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>B-02</strong></td>
<td><blockquote>
<p><strong>Detalhamento de Fatura</strong> [Ref: REF-04 Fintech Olga + REF-07 Components Lending]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — B-02</strong></p>
<p>Header: Mês/Ano da fatura + Status badge (Aberta/Fechada/Paga/Vencida) + botão [Pagar Agora]</p>
<p>Resumo financeiro: Principal | Taxa 6% | Multa (se houver) | Total em destaque (gold)</p>
<p>Tabela de transações do ciclo: Data | Estabelecimento | Categoria chip | Valor | Comprovante icon</p>
<p>Gráfico de pizza por categoria (Recharts PieChart) com legenda lateral</p>
<p>Seção FAQ inline: accordion com dúvidas frequentes sobre fatura</p>
<p>Histórico de faturas: lista de ciclos anteriores com status e valor (últimos 12)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>B-03</strong></td>
<td><blockquote>
<p><strong>Onboarding e Solicitação de Crédito</strong> [Ref: REF-07 Components Lending (input slider)]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — B-03</strong></p>
<p>Step-by-step wizard (4 etapas): [Dados Pessoais] [Endereço] [Documentos] [Análise]</p>
<p>Progress bar horizontal com etapas numeradas e labels, cor #F0B90B no ativo</p>
<p>Etapa 1: Formulário dados pessoais com validação em tempo real (ícone check verde)</p>
<p>Etapa 2: CEP auto-complete via ViaCEP API, mapa embed opcional</p>
<p>Etapa 3: Upload de documentos com drag &amp; drop, preview de imagem, status de análise</p>
<p>Etapa 4: Tela de análise com loader animado -&gt; resultado: Aprovado/Análise/Reprovado</p>
<p>Resultado aprovado: mostra limite concedido (grande, gold) + CTA [Ativar Cartão]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **7. Módulo C — Account Executive (Campo)**

Hierarquia: Junior AE \> Senior AE \> Manager \> Area Director. Cada nível tem acesso progressivo a métricas de território, comissão e pipeline de captação.

<table>
<tbody>
<tr class="odd">
<td><strong>C-01</strong></td>
<td><blockquote>
<p><strong>Dashboard do Account Executive</strong> [Ref: REF-03 FinVerse + REF-06 Modern Financial Dashboard]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout e Componentes — C-01</strong></p>
<p>Ref: REF-03 (KPI grid 4-colunas, barras empilhadas por categoria) + REF-06 (breakdown receita, tabela recentes)</p>
<p>KPI Row: [Meta Mês] [Captado até agora] [% Atingido] [Comissão Projetada]</p>
<p>Barra de progresso de meta: visual type Binance (tracker horizontal com milestone markers)</p>
<p>Mapa de território: React Simple Maps com calor por densidade de Usuários ativos</p>
<p>Tabela de pipeline: prospects por estágio (Contato &gt; Cadastro &gt; Análise &gt; Ativo)</p>
<p>Ranking da equipe (se Manager+): podium top 3 + tabela completa com pontuação</p>
<p>Feed de alertas: Usuários próximos do vencimento | Novas aprovações | Metas de equipe</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Prompt C-01**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Dashboard Account Executive NEXUS. Mesmo Design System Binance.</p>
<p>KPI ROW (4 cards):</p>
<p>[Meta: R$ 500k] [Captado: R$ 347k] [69.4% atingido] [Comissão: R$ 8.680]</p>
<p>Card 'Captado' tem progress bar interna, fill #F0B90B</p>
<p>MAPA DE TERRITÓRIO (React Simple Maps):</p>
<p>Choropleth por município, escala de cor #0B0E11 -&gt; #F0B90B</p>
<p>Tooltip: município + qtd usuários + volume R$</p>
<p>PIPELINE KANBAN (4 colunas):</p>
<p>Contato (azul) | Cadastro (amarelo) | Análise (roxo) | Ativo (verde)</p>
<p>Cards de prospect com nome mascarado, valor estimado, próxima ação</p>
<p>RANKING EQUIPE (se role Manager ou acima):</p>
<p>Podium top 3 com avatar + nome + valor captado + badge de posição</p>
<p>Tabela abaixo: ranking completo com delta vs período anterior</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>C-02</strong></td>
<td><blockquote>
<p><strong>Relatório de Território e Risco</strong> [Ref: REF-09 Fintech Dashboard UI Kit (NPL/risco)]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — C-02</strong></p>
<p>Ref: REF-09 (Risk Score visual, mapa de risco geográfico, tabela NPL por categoria)</p>
<p>Header: seletor de período + seletor de território + botão [Exportar PDF]</p>
<p>Risk Score por categoria: grid 12 chips com cor semântica (verde/amarelo/vermelho por DPD)</p>
<p>Gráfico NPL trending: área chart com linha de threshold (linha tracejada vermelha em 5%)</p>
<p>Tabela detalhada: Categoria | Volume R$ | Contratos | Adimplência% | DPD30 | DPD60 | DPD90+</p>
<p>Heatmap temporal: matrix mes x categoria com intensidade de cor por inadimplência</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **8. Módulo D — Board 360° / Administração**

<table>
<tbody>
<tr class="odd">
<td><strong>D-01</strong></td>
<td><blockquote>
<p><strong>Board Dashboard — Visão Macro NEXUS</strong> [Ref: REF-01 ChainScope + REF-03 FinVerse]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout — D-01 (densidade máxima estilo Binance Pro)</strong></p>
<p>KPI Row (6 cards menores): AUM Total | Aplicantes Ativos | Usuários Ativos | Contratos | NPL Global | Receita Mês</p>
<p>Row 2: Candle chart de AUM ao longo do tempo (8col) + Composição por trilha GREY/SCD/SEP (4col)</p>
<p>Row 3: Mapa geográfico Brasil — densidade de operações por estado (heat map)</p>
<p>Row 4: Tabela de maiores portfólios com sorting + Alertas de compliance (lista lateral)</p>
<p>Row 5: MACRO HASH ledger — últimos 50 eventos com tipo, valor, hash e timestamp</p>
<p>Permissão: apenas roles Board, CFO, CTO, Compliance Officer</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>D-02</strong></td>
<td><blockquote>
<p><strong>Gestão Financeira e P&amp;L</strong> [Ref: REF-06 Modern Financial Dashboard]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — D-02</strong></p>
<p>Ref: REF-06 (breakdown receita donut, tabela transações, histórico saques)</p>
<p>P&amp;L summary: Receita Bruta | Custos Operacionais | Provisão PDD | Lucro Líquido</p>
<p>Waterfall chart: de receita bruta até lucro líquido (barras verdes/vermelhas empilhadas)</p>
<p>Timeline de fluxo de caixa: linha chart com projeção (linha tracejada gold)</p>
<p>Tabela de contas a receber vs pagar por vencimento (aging report)</p>
<p>Simulador de cenários: sliders para taxa média, inadimplência%, aporte médio -&gt; P&amp;L projetado</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>D-03</strong></td>
<td><blockquote>
<p><strong>MACRO HASH Ledger Explorer</strong> [Ref: REF-10 Binance (blockchain explorer style)]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — D-03</strong></p>
<p>Inspiração: Etherscan / Binance Chain Explorer adaptado para NEXUS</p>
<p>Search bar no topo: busca por hash de plataforma, portfólio, contrato ou bloco</p>
<p>Estrutura hierárquica: Platform Hash -&gt; Investor Hash -&gt; Portfolio Hash -&gt; Contract Hash -&gt; Block State</p>
<p>Tree view expansível com ícones de nível e cor por status</p>
<p>Detalhe de bloco: JSON viewer formatado com syntax highlight (IBM Plex Mono)</p>
<p>Timeline de estados: fluxo visual EMISSAO &gt; USO &gt; COBRANCA &gt; PAGAMENTO &gt; LIQUIDACAO</p>
<p>Exportar trilha de auditoria: botão [Baixar CSV] + [Baixar PDF assinado]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>D-04</strong></td>
<td><blockquote>
<p><strong>Compliance e Monitoramento AML/KYC</strong> [Ref: REF-09 Fintech Risk Dashboard]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — D-04</strong></p>
<p>Score AML por usuário: tabela com indicadores de risco FATF</p>
<p>Alertas de KYC pendente: fila de aprovação com prazo e prioridade</p>
<p>Relatório BACEN: status de envio das declarações regulatórias (CMN 5050/2022)</p>
<p>Mapa de calor de transações suspeitas: volume x horário x categoria</p>
<p>Integração Open Finance: status das conexões por banco parceiro + latência</p>
<p>Log de auditoria de acesso: quem acessou o quê, quando, de qual IP</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **9. Módulo E — Mercado Secundário de Contratos**

<table>
<tbody>
<tr class="odd">
<td><strong>E-01</strong></td>
<td><blockquote>
<p><strong>Order Book de Portfólios</strong> [Ref: REF-08 Crypto Trading + REF-02 Crystal Stock]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Layout — E-01 (3 colunas tipo Binance Exchange)</strong></p>
<p>Ref: REF-08 exato (order book direita, chart centro, lista esquerda)</p>
<p>Esquerda: Lista de portfólios ofertados com ticker, rentabilidade, preço, delta 24h</p>
<p>Centro: Candle chart do portfólio selecionado + volume bars + indicadores</p>
<p>Direita cima: Order book (ofertas de compra verde / ofertas de venda vermelho)</p>
<p>Direita baixo: Formulário de oferta (Comprar / Vender tabs) com campo de valor e quantidade</p>
<p>Rodapé: Histórico de negociações recentes (tabela compacta: preço | qtd | horário | lado)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><strong>E-02</strong></td>
<td><blockquote>
<p><strong>Detalhe de Contrato Individual</strong> [Ref: REF-07 Components Lending + REF-08 Trading]</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Componentes — E-02</strong></p>
<p>Ref: REF-07 (status badge de contrato, tabela de parcelas) + REF-08 (painel de detalhes lateral)</p>
<p>Header: Hash do contrato (IBM Plex Mono gold) + Status badge + Data emissão</p>
<p>Dados do contrato: Categoria | Limite | Uso atual | Taxa | Próx. vencimento | Score do Usuário</p>
<p>MACRO HASH timeline vertical do contrato (todos os eventos desde emissão)</p>
<p>Histórico de pagamentos: tabela com valor pago, data, atraso (dias), multa aplicada</p>
<p>Painel de risco: probability of default, LGD estimado, score comportamental</p>
<p>Botão [Fazer Oferta] para colocar contrato no mercado secundário</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **10. Módulo F — Integração BI (Apache Superset + Metabase + Grafana + Power BI)**

**10.1 Estratégia de BI por Perfil de Usuário**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Ferramenta</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Perfil Alvo</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Caso de Uso Principal</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tipo de Deploy</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Apache Superset</p>
</blockquote></td>
<td><blockquote>
<p>Analistas de Dados / CTO</p>
</blockquote></td>
<td><blockquote>
<p>SQL exploratório, dashboards técnicos ad-hoc</p>
</blockquote></td>
<td><blockquote>
<p>Self-hosted Docker</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Metabase</p>
</blockquote></td>
<td><blockquote>
<p>Account Executives / Field</p>
</blockquote></td>
<td><blockquote>
<p>Relatórios pré-construídos, embed no app</p>
</blockquote></td>
<td><blockquote>
<p>Self-hosted ou Cloud</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Grafana</p>
</blockquote></td>
<td><blockquote>
<p>SRE / Operações em tempo real</p>
</blockquote></td>
<td><blockquote>
<p>Latência, erros, saúde da plataforma</p>
</blockquote></td>
<td><blockquote>
<p>Self-hosted + Prometheus</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Power BI</p>
</blockquote></td>
<td><blockquote>
<p>Board / Investidores Externos</p>
</blockquote></td>
<td><blockquote>
<p>Apresentações institucionais, .pbix templates</p>
</blockquote></td>
<td><blockquote>
<p>Power BI Service (cloud)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.2 Apache Superset — SQL Views e REST API**

**Views SQL para NEXUS**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>View</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Descrição</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Campos Principais</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>nexus_portfolio_overview</p>
</blockquote></td>
<td><blockquote>
<p>Resumo de todos portfólios ativos</p>
</blockquote></td>
<td><blockquote>
<p>investor_id, portfolio_hash, aum, return_pct, contract_count, npl_rate, created_at</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nexus_executive_kpis</p>
</blockquote></td>
<td><blockquote>
<p>KPIs por Account Executive e território</p>
</blockquote></td>
<td><blockquote>
<p>ae_id, territory, target, achieved, commission, pipeline_count, conversion_rate</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nexus_financial_summary</p>
</blockquote></td>
<td><blockquote>
<p>P&amp;L consolidado por período</p>
</blockquote></td>
<td><blockquote>
<p>period, gross_revenue, provisions, opex, net_income, aum_eod, active_users</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nexus_delinquency_map</p>
</blockquote></td>
<td><blockquote>
<p>Mapa de inadimplência por categoria</p>
</blockquote></td>
<td><blockquote>
<p>category_id, category_name, total_contracts, dpd30, dpd60, dpd90_plus, npl_pct</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nexus_macro_hash_events</p>
</blockquote></td>
<td><blockquote>
<p>Log do ledger MACRO HASH</p>
</blockquote></td>
<td><blockquote>
<p>event_type, platform_hash, investor_hash, portfolio_hash, contract_hash, amount, ts</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nexus_user_score_distribution</p>
</blockquote></td>
<td><blockquote>
<p>Distribuição de score de usuários</p>
</blockquote></td>
<td><blockquote>
<p>score_bucket, count, avg_limit, avg_usage_pct, default_rate</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Endpoints REST — Apache Superset**

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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/security/login</p>
</blockquote></td>
<td><blockquote>
<p>Autenticação — retorna access_token JWT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/dashboard/</p>
</blockquote></td>
<td><blockquote>
<p>Lista todos os dashboards disponíveis</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/dashboard/{id}/embedded</p>
</blockquote></td>
<td><blockquote>
<p>Configuração de embed (token de guest)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/security/guest_token/</p>
</blockquote></td>
<td><blockquote>
<p>Gera guest token para embed seguro no NEXUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/chart/{id}/data/</p>
</blockquote></td>
<td><blockquote>
<p>Dados de um gráfico específico</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/sqllab/execute/</p>
</blockquote></td>
<td><blockquote>
<p>Executa query SQL ad-hoc na view</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/dataset/</p>
</blockquote></td>
<td><blockquote>
<p>Lista datasets disponíveis</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/v1/chart/</p>
</blockquote></td>
<td><blockquote>
<p>Cria novo gráfico programaticamente</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Superset Embed — React Integration**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>// Embed Superset dashboard no NEXUS (React)</p>
<p>const embedSuperset = async (dashboardId: string) =&gt; {</p>
<p>const { token } = await fetch('/api/superset/guest-token', {</p>
<p>method: 'POST',</p>
<p>body: JSON.stringify({ dashboardId, user: currentUser.id })</p>
<p>}).then(r =&gt; r.json());</p>
<p>return (</p>
<p>&lt;iframe</p>
<p>src={`${SUPERSET_URL}/superset/dashboard/${dashboardId}/?standalone=3&amp;uiConfig=...`}</p>
<p>style={{ background: '#0B0E11', border: 'none', width: '100%', height: '600px' }}</p>
<p>/&gt;</p>
<p>);</p>
<p>};</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.3 Metabase — Embed API**

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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/session</p>
</blockquote></td>
<td><blockquote>
<p>Login — retorna session token</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/dashboard/{id}</p>
</blockquote></td>
<td><blockquote>
<p>Detalhes de um dashboard</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/embed/dashboard/{token}</p>
</blockquote></td>
<td><blockquote>
<p>URL de embed com JWT assinado</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/card/{id}/query</p>
</blockquote></td>
<td><blockquote>
<p>Executa uma question salva</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/dataset</p>
</blockquote></td>
<td><blockquote>
<p>Query ad-hoc com filtros</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/collection/</p>
</blockquote></td>
<td><blockquote>
<p>Lista coleções (pastas)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>/api/card/</p>
</blockquote></td>
<td><blockquote>
<p>Cria nova question</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>/api/user/current</p>
</blockquote></td>
<td><blockquote>
<p>Perfil do usuário autenticado</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Metabase Signed Embed**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>// Metabase Signed Embed (Node.js / Next.js API route)</p>
<p>import jwt from 'jsonwebtoken';</p>
<p>export async function getMetabaseEmbedUrl(dashboardId: number, params: object) {</p>
<p>const token = jwt.sign(</p>
<p>{ resource: { dashboard: dashboardId }, params, exp: Math.round(Date.now()/1000) + 600 },</p>
<p>process.env.METABASE_SECRET_KEY!</p>
<p>);</p>
<p>return `${process.env.METABASE_URL}/embed/dashboard/${token}#bordered=false&amp;titled=false&amp;theme=night`;</p>
<p>}</p>
<p>// No componente React:</p>
<p>// &lt;iframe src={await getMetabaseEmbedUrl(3, { territory_id: ae.territory })} /&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.4 Grafana — Infinity Datasource + Painéis**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Painel</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tipo</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fonte de Dados</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Thresholds</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Latência API NEXUS (P95)</p>
</blockquote></td>
<td><blockquote>
<p>Time series</p>
</blockquote></td>
<td><blockquote>
<p>Prometheus metrics</p>
</blockquote></td>
<td><blockquote>
<p>verde &lt;200ms / amarelo &lt;500ms / vermelho &gt;500ms</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Taxa de erro por endpoint</p>
</blockquote></td>
<td><blockquote>
<p>Bar gauge</p>
</blockquote></td>
<td><blockquote>
<p>Prometheus rate(errors[5m])</p>
</blockquote></td>
<td><blockquote>
<p>verde &lt;0.1% / vermelho &gt;1%</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Contratos processados/min</p>
</blockquote></td>
<td><blockquote>
<p>Stat panel</p>
</blockquote></td>
<td><blockquote>
<p>Prometheus counter</p>
</blockquote></td>
<td><blockquote>
<p>baseline + alertas de anomalia</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Aporte em tempo real</p>
</blockquote></td>
<td><blockquote>
<p>Time series</p>
</blockquote></td>
<td><blockquote>
<p>Infinity → NEXUS REST API</p>
</blockquote></td>
<td><blockquote>
<p>linha de meta diária (#F0B90B)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Usuários online agora</p>
</blockquote></td>
<td><blockquote>
<p>Stat panel</p>
</blockquote></td>
<td><blockquote>
<p>WebSocket metrics</p>
</blockquote></td>
<td><blockquote>
<p>pico histórico como referência</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Queue depth (Agentic AI jobs)</p>
</blockquote></td>
<td><blockquote>
<p>Gauge</p>
</blockquote></td>
<td><blockquote>
<p>RabbitMQ / Redis exporter</p>
</blockquote></td>
<td><blockquote>
<p>verde &lt;100 / vermelho &gt;500</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Grafana Infinity Datasource Config**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># Grafana Infinity datasource — query para AUM em tempo real</p>
<p># datasource: Infinity (plugin grafana-infinity-datasource)</p>
<p>url: https://api.nexus.com.br/v1/metrics/aum</p>
<p>method: GET</p>
<p>headers:</p>
<p>Authorization: Bearer ${NEXUS_API_KEY}</p>
<p>X-Grafana-Datasource: true</p>
<p>parser: json</p>
<p>root_selector: data.aum_timeseries</p>
<p>columns:</p>
<p>- selector: timestamp</p>
<p>type: timestamp</p>
<p>- selector: value</p>
<p>type: number</p>
<p>alias: AUM (R$)</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.5 Power BI REST API — Endpoints Completos**

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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token</p>
</blockquote></td>
<td><blockquote>
<p>OAuth2 token (service principal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups</p>
</blockquote></td>
<td><blockquote>
<p>Lista workspaces</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports</p>
</blockquote></td>
<td><blockquote>
<p>Lista relatórios do workspace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/GenerateToken</p>
</blockquote></td>
<td><blockquote>
<p>Gera embed token</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets</p>
</blockquote></td>
<td><blockquote>
<p>Lista datasets</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{id}/refreshes</p>
</blockquote></td>
<td><blockquote>
<p>Trigger refresh de dataset</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/imports</p>
</blockquote></td>
<td><blockquote>
<p>Import de arquivo .pbix</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/imports/{importId}</p>
</blockquote></td>
<td><blockquote>
<p>Status do import</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GET</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/capacities</p>
</blockquote></td>
<td><blockquote>
<p>Lista capacidades Premium</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATCH</p>
</blockquote></td>
<td><blockquote>
<p>https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{id}</p>
</blockquote></td>
<td><blockquote>
<p>Atualiza parâmetros do dataset</p>
</blockquote></td>
</tr>
</tbody>
</table>

**Power BI Embed React Component**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>// Power BI Embed — React Component NEXUS</p>
<p>import { models } from 'powerbi-client';</p>
<p>import { PowerBIEmbed } from 'powerbi-client-react';</p>
<p>const NexusPowerBIReport = ({ embedToken, embedUrl, reportId }) =&gt; (</p>
<p>&lt;PowerBIEmbed</p>
<p>embedConfig={{</p>
<p>type: 'report',</p>
<p>id: reportId,</p>
<p>embedUrl,</p>
<p>accessToken: embedToken,</p>
<p>tokenType: models.TokenType.Embed,</p>
<p>settings: {</p>
<p>background: models.BackgroundType.Transparent,</p>
<p>panes: { filters: { visible: false }, pageNavigation: { visible: true } }</p>
<p>}</p>
<p>}}</p>
<p>cssClassName='nexus-pbi-frame'</p>
<p>/&gt;</p>
<p>);</p>
<p>// CSS: .nexus-pbi-frame { background: #0B0E11; height: 600px; border: none; }</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.6 Templates .pbix — Especificações**

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Template</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Arquivo</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tipo</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Conexão</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Atualização</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Board Executivo — AUM &amp; P&amp;L</p>
</blockquote></td>
<td><blockquote>
<p>nexus_board_executive.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>DirectQuery → PostgreSQL</p>
</blockquote></td>
<td><blockquote>
<p>Tempo real</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Portfólio Aplicante</p>
</blockquote></td>
<td><blockquote>
<p>nexus_portfolio_investor.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>Import → REST API NEXUS</p>
</blockquote></td>
<td><blockquote>
<p>A cada 15min</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KPIs Account Executive</p>
</blockquote></td>
<td><blockquote>
<p>nexus_ae_kpis.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>Import → PostgreSQL views</p>
</blockquote></td>
<td><blockquote>
<p>Diário 06h</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Risco e Inadimplência</p>
</blockquote></td>
<td><blockquote>
<p>nexus_risk_delinquency.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>DirectQuery → PostgreSQL</p>
</blockquote></td>
<td><blockquote>
<p>A cada 1h</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MACRO HASH Audit Trail</p>
</blockquote></td>
<td><blockquote>
<p>nexus_macro_hash.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>Import → ledger DB</p>
</blockquote></td>
<td><blockquote>
<p>Diário 00h</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Compliance BACEN</p>
</blockquote></td>
<td><blockquote>
<p>nexus_compliance_bacen.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>Import → compliance schema</p>
</blockquote></td>
<td><blockquote>
<p>Mensal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mapa Geográfico de Operações</p>
</blockquote></td>
<td><blockquote>
<p>nexus_geo_operations.pbix</p>
</blockquote></td>
<td><blockquote>
<p>Report</p>
</blockquote></td>
<td><blockquote>
<p>Import → geo views</p>
</blockquote></td>
<td><blockquote>
<p>Diário 06h</p>
</blockquote></td>
</tr>
</tbody>
</table>

**10.7 Tema Binance-Dark para Power BI (.json)**

**nexus\_binance\_dark\_theme.json — importar em Power BI Desktop via View \> Themes**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>{</p>
<p>"name": "NEXUS Binance Dark",</p>
<p>"dataColors": ["#F0B90B","#03C076","#0091FF","#6C3ABD","#F6465C","#848E9C"],</p>
<p>"background": "#0B0E11",</p>
<p>"foreground": "#EAECEF",</p>
<p>"tableAccent": "#F0B90B",</p>
<p>"visualStyles": {</p>
<p>"*": {</p>
<p>"*": {</p>
<p>"background": [{ "color": { "solid": { "color": "#161A1E" } } }],</p>
<p>"border": [{ "show": true, "color": { "solid": { "color": "#2B3139" } } }],</p>
<p>"fontFamily": ["IBM Plex Sans"],</p>
<p>"fontSize": [11]</p>
<p>}</p>
<p>},</p>
<p>"title": {</p>
<p>"*": {</p>
<p>"fontColor": [{ "solid": { "color": "#EAECEF" } }],</p>
<p>"background": [{ "color": { "solid": { "color": "#161A1E" } } }],</p>
<p>"fontSize": [14],</p>
<p>"fontFamily": ["IBM Plex Sans"]</p>
<p>}</p>
<p>},</p>
<p>"page": {</p>
<p>"*": {</p>
<p>"background": [{ "color": { "solid": { "color": "#0B0E11" } } }],</p>
<p>"outspace": [{ "color": { "solid": { "color": "#0B0E11" } } }]</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **11. Master Prompt Block — Copiar para v0.dev / Lovable / Bolt.new / Cursor**

Cole este bloco INTEIRO no início de qualquer sessão de geração de telas NEXUS. Ele define o contexto completo de Design System, stack técnico e restrições visuais.

**Master Prompt Block — v3**

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>=== NEXUS DESIGN SYSTEM — MASTER CONTEXT v3 ===</p>
<p>Você está criando telas para o NEXUS, plataforma P2P lending brasileira.</p>
<p>USE OBRIGATORIAMENTE o Binance Design System conforme abaixo.</p>
<p>── PALETA DE CORES ──────────────────────────────</p>
<p>bg-deep: #0B0E11 // canvas principal</p>
<p>bg-card: #161A1E // cards e painéis</p>
<p>bg-hover: #1E2329 // hover state</p>
<p>border: #2B3139 // todas as bordas</p>
<p>gold: #F0B90B // CTA primário, destaques</p>
<p>green: #03C076 // positivo, sucesso, alta</p>
<p>red: #F6465C // negativo, erro, baixa</p>
<p>blue: #0091FF // info, links</p>
<p>purple: #6C3ABD // premium, qualificado</p>
<p>text-pri: #EAECEF // texto principal</p>
<p>text-sec: #848E9C // labels secundários</p>
<p>text-dis: #474D57 // disabled</p>
<p>── TIPOGRAFIA ───────────────────────────────────</p>
<p>Números/valores: IBM Plex Mono (todos sem exceção)</p>
<p>Labels/body: IBM Plex Sans</p>
<p>Tamanhos: hero 32-48px | H1 24px | H2 18px | label 12px | body 14px</p>
<p>── COMPONENTES OBRIGATÓRIOS ─────────────────────</p>
<p>Cards: padding 16px | border 1px #2B3139 | radius 6px | hover: border #F0B90B</p>
<p>Buttons primários: bg #F0B90B | text #0B0E11 | radius 4px | padding 8px 16px</p>
<p>Buttons secundários: ghost border #2B3139 | text #EAECEF | hover bg #1E2329</p>
<p>Badges: radius 100px | bg cor/15 opacity | text cor full</p>
<p>Tabelas: header bg #161A1E | row alt #0B0E11/#161A1E | hover #1E2329</p>
<p>colunas numéricas: IBM Plex Mono alinhado à direita</p>
<p>── STACK TÉCNICA ────────────────────────────────</p>
<p>React 18 + TypeScript + Tailwind CSS (somente classes utilitárias)</p>
<p>shadcn/ui para componentes base (Button, Card, Table, Dialog, etc.)</p>
<p>Recharts para: PieChart, BarChart, AreaChart, RadialBarChart, Sparklines</p>
<p>lightweight-charts (TradingView) para: CandlestickChart, LineChart trading</p>
<p>Framer Motion para: fade+slide entrada 300ms, hover transitions 150ms</p>
<p>React Simple Maps para: choropleth geográfico</p>
<p>TanStack Table v8 para: DataGrid com sorting/filtering/pagination</p>
<p>── PROIBIDO ─────────────────────────────────────</p>
<p>NÃO use: fundos brancos ou cinzas claros</p>
<p>NÃO use: border-radius &gt; 8px em cards (exceto chips: 100px)</p>
<p>NÃO use: drop-shadow (use apenas borda)</p>
<p>NÃO use: Inter ou outras fontes (apenas IBM Plex Sans/Mono)</p>
<p>NÃO use: gradientes (exceto hero card do usuário: sutil #161A1E -&gt; #1E2329)</p>
<p>NÃO coloque números em fontes não-Mono</p>
<p>── REFERÊNCIAS VISUAIS ──────────────────────────</p>
<p>Binance.com (exchange interface) — densidade e organização</p>
<p>ChainScope (Fikri Ruslandi / Dribbble) — portfolio dark dashboard</p>
<p>FinVerse (Mike Taylor / Dribbble) — KPI grid e sidebar</p>
<p>Crystal Stock App (Milkinside / Dribbble) — cards de ativo com sparkline</p>
<p>=== FIM DO MASTER CONTEXT ===</p>
<p>Agora crie a tela: [INSERIR TELA AQUI]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **12. Checklist de Validação Visual**

Antes de entregar qualquer tela gerada por IA ao time de desenvolvimento, valide cada item:

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Item de Validação</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Critério de Aprovação</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Ferramenta</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Fundo principal</p>
</blockquote></td>
<td><blockquote>
<p>#0B0E11 (nenhum branco ou cinza claro)</p>
</blockquote></td>
<td><blockquote>
<p>DevTools / Color Picker</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Cards e painéis</p>
</blockquote></td>
<td><blockquote>
<p>#161A1E com borda #2B3139</p>
</blockquote></td>
<td><blockquote>
<p>Inspeção CSS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Tipografia numérica</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex Mono em 100% dos valores numéricos</p>
</blockquote></td>
<td><blockquote>
<p>Font inspector</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>CTA primário</p>
</blockquote></td>
<td><blockquote>
<p>Fundo #F0B90B, texto #0B0E11, radius 4px</p>
</blockquote></td>
<td><blockquote>
<p>Visual + CSS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Valores positivos</p>
</blockquote></td>
<td><blockquote>
<p>Cor #03C076 sem exceção</p>
</blockquote></td>
<td><blockquote>
<p>Visual review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Valores negativos</p>
</blockquote></td>
<td><blockquote>
<p>Cor #F6465C sem exceção</p>
</blockquote></td>
<td><blockquote>
<p>Visual review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Border-radius cards</p>
</blockquote></td>
<td><blockquote>
<p>4–8px (não 16px+)</p>
</blockquote></td>
<td><blockquote>
<p>CSS inspect</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Sem drop-shadow</p>
</blockquote></td>
<td><blockquote>
<p>box-shadow: none em cards</p>
</blockquote></td>
<td><blockquote>
<p>CSS inspect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Gráficos de candle</p>
</blockquote></td>
<td><blockquote>
<p>lightweight-charts (não Chart.js candlestick)</p>
</blockquote></td>
<td><blockquote>
<p>Código</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Sparklines em KPI cards</p>
</blockquote></td>
<td><blockquote>
<p>Recharts 60px height sem eixos</p>
</blockquote></td>
<td><blockquote>
<p>Código</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Responsividade</p>
</blockquote></td>
<td><blockquote>
<p>Mobile 375px + Tablet 768px + Desktop 1440px</p>
</blockquote></td>
<td><blockquote>
<p>DevTools resize</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Animações de entrada</p>
</blockquote></td>
<td><blockquote>
<p>Framer Motion fade+slide 300ms (não CSS puro)</p>
</blockquote></td>
<td><blockquote>
<p>Código</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>Hover em rows de tabela</p>
</blockquote></td>
<td><blockquote>
<p>#1E2329 com transition 100ms</p>
</blockquote></td>
<td><blockquote>
<p>Interação manual</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Status badges</p>
</blockquote></td>
<td><blockquote>
<p>Radius 100px, bg opacity 15%, texto full color</p>
</blockquote></td>
<td><blockquote>
<p>Visual review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>IBM Plex carregada</p>
</blockquote></td>
<td><blockquote>
<p>@import no head ou next/font configurado</p>
</blockquote></td>
<td><blockquote>
<p>Network tab</p>
</blockquote></td>
</tr>
</tbody>
</table>

NEXUS | UI/UX Prompt Master v3 | Binance Design System + Dribbble Reference Library

React 18 + TypeScript + Tailwind CSS + shadcn/ui + lightweight-charts + Recharts + Framer Motion
