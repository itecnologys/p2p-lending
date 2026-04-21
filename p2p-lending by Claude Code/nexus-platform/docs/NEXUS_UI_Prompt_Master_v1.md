---
title: "NEXUS — NEXUS_UI_Prompt_Master_v1"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>[ NEXUS PLATFORM — UI/UX DESIGN SPECIFICATION ]</strong></p>
<p><strong>PROMPT MESTRE DE DESIGN</strong></p>
<p><strong>Especificacao Completa de Telas para IA Generativa</strong></p>
<p><em>Plataforma NEXUS · Aplicante · Usuario · Executivo · 360 BOARD · Admin · Mobile</em></p></td>
</tr>
</tbody>
</table>

*Este documento contem o PROMPT MESTRE completo para que uma IA generativa (v0.dev, Lovable, Bolt.new, Cursor, GPT-4o com visao, Claude Artifacts ou similar) construa todas as telas da plataforma NEXUS. O prompt esta organizado por MODULO, com especificacoes de layout, componentes, dados exibidos, interacoes e design tokens.*

**PARTE 1 — DESIGN SYSTEM & TOKENS GLOBAIS**

Antes de gerar qualquer tela, a IA deve internalizar o Design System do NEXUS. Todos os componentes devem ser construidos com base nestes tokens.

**1.1 Paleta de Cores**

| **Token**          | **Hex**  | **Uso**                                           |
| ------------------ | -------- | ------------------------------------------------- |
| \--nexus-dark      | \#0D1B2A | Background principal (dark mode)                  |
| \--nexus-surface   | \#132135 | Cards, modais, paineis secundarios                |
| \--nexus-surface-2 | \#1C2E45 | Hover states, rows alternadas                     |
| \--nexus-accent    | \#00B4D8 | CTAs primarios, links, destaque de dados          |
| \--nexus-gold      | \#F5A623 | Alertas positivos, retorno financeiro, badges VIP |
| \--nexus-green     | \#27AE60 | Status ativo, adimplente, sucesso                 |
| \--nexus-red       | \#D62228 | Inadimplência, erro, risco alto                   |
| \--nexus-amber     | \#F39C12 | Risco médio, alertas, pendentes                   |
| \--nexus-purple    | \#6C3ABD | Blockchain/hash, stablecoin, features premium     |
| \--nexus-white     | \#FFFFFF | Textos primarios no dark mode                     |
| \--nexus-grey-1    | \#8899AA | Textos secundarios, labels, placeholders          |
| \--nexus-grey-2    | \#44556A | Borders, separadores, inputs inativos             |
| \--nexus-light-bg  | \#F0F7FF | Background light mode (telas de Usuario basico)   |

**1.2 Tipografia**

<table>
<tbody>
<tr class="odd">
<td><p><strong>TIPOGRAFIA — NEXUS DESIGN SYSTEM</strong></p>
<p>Font Family Principal: 'Inter' (Google Fonts) — sem-serif, clean, financeiro</p>
<p>Font Family Monoespacada: 'JetBrains Mono' — para hashes, codigos, valores crypto</p>
<p>H1 (Page Title): Inter 32px Bold | tracking: -0.5px | cor: --nexus-white</p>
<p>H2 (Section Title): Inter 24px SemiBold | tracking: -0.3px | cor: --nexus-white</p>
<p>H3 (Card Title): Inter 18px SemiBold | cor: --nexus-accent</p>
<p>H4 (Label): Inter 14px Medium | cor: --nexus-grey-1 | uppercase + letter-spacing 1px</p>
<p>Body Large: Inter 16px Regular | cor: --nexus-white | line-height: 1.6</p>
<p>Body Small: Inter 14px Regular | cor: --nexus-grey-1</p>
<p>Caption: Inter 12px Regular | cor: --nexus-grey-1</p>
<p>Hash/Code: JetBrains Mono 13px | cor: --nexus-purple | background: rgba(108,58,189,0.12)</p>
<p>Currency Large: Inter 48px Bold | cor: --nexus-gold | para valores principais de portfolio</p>
<p>Currency Medium: Inter 28px SemiBold | cor: --nexus-white</p></td>
</tr>
</tbody>
</table>

**1.3 Componentes Base**

<table>
<tbody>
<tr class="odd">
<td><p><strong>COMPONENTES REUTILIZAVEIS — NEXUS UI KIT</strong></p>
<p>NexusCard: background --nexus-surface | border-radius 16px | border 1px solid rgba(255,255,255,0.08) | shadow: 0 4px 24px rgba(0,0,0,0.4)</p>
<p>NexusButton Primary: background --nexus-accent | color dark | border-radius 10px | padding 14px 28px | font 15px SemiBold | hover: brightness(1.1)</p>
<p>NexusButton Secondary: background transparent | border 1.5px --nexus-accent | color --nexus-accent | mesmo border-radius</p>
<p>NexusButton Danger: background --nexus-red | cor white | usar apenas para acoes destrutivas</p>
<p>NexusBadge: pill shape | padding 4px 12px | font 12px SemiBold | variantes: green/red/amber/purple/grey</p>
<p>NexusInput: background rgba(255,255,255,0.06) | border 1px --nexus-grey-2 | border-radius 10px | padding 14px 16px | focus: border --nexus-accent</p>
<p>NexusHash: family JetBrains Mono | background rgba(108,58,189,0.15) | padding 4px 10px | border-radius 6px | truncate com tooltip no hover</p>
<p>NexusProgress: track --nexus-surface-2 | fill --nexus-accent | height 8px | border-radius 4px | com label de percentual</p>
<p>NexusToast: fixed bottom-right | slide-in animation | variantes: success/error/info/warning | auto-dismiss 4s</p>
<p>NexusModal: backdrop blur(8px) | centered card | max-width 640px | fechar com ESC ou click externo</p>
<p>NexusSidebar: width 260px | background --nexus-surface | border-right 1px --nexus-grey-2 | collapsible para 72px (icon-only)</p>
<p>NexusChart: Recharts ou Chart.js | cores: accent/gold/green/red | grid lines: rgba(255,255,255,0.06) | tooltips com NexusCard style</p>
<p>NexusTable: header background --nexus-surface-2 | rows alternadas com rgba(255,255,255,0.03) | sort/filter nos headers | virtualizacao para &gt;100 linhas</p>
<p>NexusStatusDot: 10px circle | green=ativo | amber=pendente | red=inadimplente | purple=em uso | grey=inativo | com pulse animation se 'em uso'</p></td>
</tr>
</tbody>
</table>

**1.4 Layout Grid**

Todas as telas usam: max-width 1440px, padding horizontal 32px (desktop) / 16px (mobile). Grid de 12 colunas com gap de 24px. Breakpoints: mobile \< 768px, tablet 768-1024px, desktop \> 1024px. Sidebar fixa no desktop, drawer deslizante no mobile. Top bar fixa com altura de 64px.

**PARTE 2 — MODULO DO APLICANTE (INVESTIDOR)**

O Aplicante e o investidor da plataforma. Suas telas devem transmitir CONFIANCA, SOFISTICACAO FINANCEIRA e CONTROLE TOTAL sobre o portfolio. Inspiracoes visuais: Maple Finance dashboard, Nexo portfolio, TradingView, Bloomberg Terminal (mais clean).

**TELA A-01 — Login / Onboarding do Aplicante**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA A-01: LOGIN APLICANTE</strong></p>
<p>Crie uma tela de login para investidor (Aplicante) da plataforma NEXUS de emprestimos P2P.</p>
<p>LAYOUT: Split screen — esquerda (55%): hero visual dark com gradiente de #0D1B2A para #132135,</p>
<p>mostrando um grafico animado de portfolio crescendo + metricas flutuando (ex: 'R$ 48.200 rendidos este mes').</p>
<p>Direita (45%): formulario de login em card NexusCard centralizado.</p>
<p>FORMULARIO: Logo NEXUS no topo (simbolo de hexagono com N + wordmark 'NEXUS')</p>
<p>Headline: 'Seu capital trabalhando 24h por dia' | Subtitulo: 'Retornos de 3,5% a 5% ao mes'</p>
<p>Campo Email (NexusInput) | Campo Senha (NexusInput com toggle show/hide)</p>
<p>Checkbox 'Lembrar dispositivo' | Link 'Esqueci minha senha'</p>
<p>Botao 'Entrar' (NexusButton Primary full-width) | Separador 'ou'</p>
<p>Botao 'Autenticar com biometria' (icone de fingerprint + texto) se dispositivo suportar</p>
<p>Link 'Solicitar acesso como Aplicante' — direciona para formulario de onboarding</p>
<p>SEGURANCA VISUAL: Badge '256-bit SSL' | Badge 'Regulado Bacen' | Badge 'AML/KYC Verificado'</p>
<p>Footer: 'NEXUS Financial Technology | Dubai DIFC | CNPJ XX.XXX.XXX/0001-XX'</p>
<p>Animacao: numero de investidores ativos piscando suavemente no hero | Modo: dark apenas</p></td>
</tr>
</tbody>
</table>

**TELA A-02 — Dashboard Principal do Aplicante**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA A-02: DASHBOARD APLICANTE</strong></p>
<p>Crie o dashboard principal do investidor NEXUS. Dark mode. Layout com sidebar fixa (260px) a esquerda.</p>
<p>SIDEBAR: Logo NEXUS no topo | Avatar do usuario + nome + tier badge (ex: 'Qualificado')</p>
<p>Menu: [Dashboard] [Meu Portfolio] [Mercado] [Contratos] [Gerente de Contas] [Relatorios] [Configuracoes]</p>
<p>Footer sidebar: versao do app | status da plataforma (dot verde 'Online')</p>
<p>TOP BAR (64px): Breadcrumb | Icone sino (notificacoes com badge numerico) | Toggle light/dark | Avatar menu</p>
<p>CONTEUDO PRINCIPAL — 4 ZONAS:</p>
<p>ZONA 1 — HERO METRICS (topo, full width): 4 cards NexusCard em linha:</p>
<p>Card 1: 'Capital Total Aplicado' — valor em R$ grande (currency-large style) + variacao % desde ontem</p>
<p>Card 2: 'Rendimento do Mes' — valor + mini sparkline de 30 dias + badge 'Meta: 4,2%'</p>
<p>Card 3: 'Capital em Uso' — valor + barra de progresso NexusProgress + percentual</p>
<p>Card 4: 'Taxa de Adimplencia' — percentual grande + NexusStatusDot verde + 'Carteira Saudavel'</p>
<p>ZONA 2 — GRAFICO PRINCIPAL (60% largura, esquerda): Area chart interativo mostrando</p>
<p>evolucao do patrimonio aplicado vs rendimentos acumulados vs inadimplencia no tempo.</p>
<p>Filtros: [7D] [30D] [90D] [1A] [Todo o Periodo]</p>
<p>Tooltip ao hover: data + valor + rendimento do periodo + % adimplencia</p>
<p>Linhas: azul=capital, dourada=rendimentos, vermelha pontilhada=inadimplencia (se houver)</p>
<p>ZONA 3 — DISTRIBUICAO DE PORTFOLIO (40% largura, direita): Donut chart com verticais</p>
<p>Legenda ao lado: cada vertical com cor, percentual, valor em R$ e badge de risco</p>
<p>Botao 'Rebalancear Portfolio' abaixo do donut</p>
<p>ZONA 4 — TABELA DE CONTRATOS RECENTES (full width, base): NexusTable com colunas:</p>
<p>[Hash truncado] [Vertical] [Usuario ID anonimo] [Valor] [Estado: badge colorido] [Retorno] [Vencimento]</p>
<p>Paginacao | filtros por estado | botao 'Ver todos os contratos'</p>
<p>SIDEBAR DIREITA (opcional, colapsavel, 300px): Gerente de Contas assignado</p>
<p>Foto/avatar | nome | rating (estrelas) | botao 'Solicitar reuniao' | botao 'Enviar mensagem'</p></td>
</tr>
</tbody>
</table>

**TELA A-03 — Composicao de Portfolio**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA A-03: COMPOSER DE PORTFOLIO</strong></p>
<p>Crie a tela de composicao de portfolio do Aplicante NEXUS. Esta e a tela mais importante</p>
<p>para conversao — deve ser intuitiva como o Spotify (escolher uma playlist) mas sofisticada</p>
<p>como o Bloomberg (mostrar dados de risco).</p>
<p>LAYOUT: 3 colunas em desktop.</p>
<p>COLUNA ESQUERDA (280px) — FILTROS DE COMPOSICAO:</p>
<p>Slider 'Valor a Aplicar': de R$ 1.000 a R$ 1.000.000 (com input numerico sincronizado)</p>
<p>Slider 'Perfil de Risco': Conservador | Moderado | Arrojado | Agressivo</p>
<p>Toggle 'Modo Autopiloto': quando ativo, plataforma compoe automaticamente</p>
<p>Dropdown 'Prazo de Contrato': 18 | 24 | 36 meses</p>
<p>Checkbox group 'Verticais Permitidas': checkboxes para cada uma das 12 verticais</p>
<p>Botao 'Gerar Portfolio Otimizado'</p>
<p>COLUNA CENTRAL (flex) — CANVAS DE COMPOSICAO:</p>
<p>Headline: 'Seu Portfolio Projetado'</p>
<p>Donut chart interativo — ao mover os filtros, o donut se redesenha com animacao suave</p>
<p>Abaixo do donut: cards de cada vertical selecionada com:</p>
<p>- Icone da vertical (saude=coracao, educacao=chapeu formatura, etc.)</p>
<p>- % do portfolio + valor em R$</p>
<p>- Badge de risco (Baixo/Medio/Alto) colorido</p>
<p>- Retorno projetado para a vertical (ex: '3,8% ao mes')</p>
<p>- Slider individual para ajustar % manualmente (respeitando limite de 25%)</p>
<p>Aviso em amber se qualquer vertical ultrapassar 25%: 'Limite de concentracao atingido'</p>
<p>COLUNA DIREITA (320px) — PAINEL DE PROJECAO:</p>
<p>Headline: 'Forecast de Retorno'</p>
<p>NexusCard com cenarios: [Pessimista] [Base] [Otimista]</p>
<p>Para cada cenario: retorno total ao fim do contrato em R$ e em %</p>
<p>Grafico de linha projetado: capital + juros compostos ao longo dos meses do contrato</p>
<p>Metricas: 'Ponto de empate (break-even): Mes 2' | 'Retorno total: R$ X'</p>
<p>'Taxa de adimplencia estimada: 93%' | 'Exposicao maxima a inadimplencia: R$ X'</p>
<p>Stress test: 'Se inadimplencia chegar a 15%: seu retorno seria X%'</p>
<p>Botao 'Confirmar e Aplicar' (NexusButton Primary, grande, fixo no bottom desta coluna)</p>
<p>MODAL DE CONFIRMACAO ao clicar em 'Confirmar e Aplicar':</p>
<p>Resumo do portfolio em texto | Hash do portfolio gerado (NexusHash component)</p>
<p>Checkbox 'Li e aceito o Contrato de Participacao' + link para o PDF</p>
<p>Botao 'Assinar e Investir' | countdown de 5 segundos antes de habilitar o botao</p></td>
</tr>
</tbody>
</table>

**TELA A-04 — Rastreamento MACRO HASH (Ledger View)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA A-04: MACRO HASH LEDGER</strong></p>
<p>Crie a tela de rastreamento de ledger do portfolio NEXUS. Visual inspirado em exploradores</p>
<p>de blockchain (Etherscan, Solscan) mas com UX muito mais acessivel para nao-tecnicos.</p>
<p>LAYOUT: Full width com sidebar de navegacao por portfolio.</p>
<p>TOPO — SELECTOR DE PORTFOLIO:</p>
<p>Dropdown com todos os portfolios do Aplicante | cada item mostra: hash truncado + data + valor</p>
<p>Ao selecionar: toda a pagina se atualiza com animacao fade</p>
<p>HERO — HASH DO PORTFOLIO:</p>
<p>NexusHash gigante (full width, centralizado): ex: 'NXS-7F4A2B...E91C'</p>
<p>Botao de copiar | botao de verificar no ledger publico | botao de compartilhar (gera link de auditoria)</p>
<p>Timestamp: 'Portfolio criado em: 15/01/2026 14:32:07 UTC'</p>
<p>METRICAS DO PORTFOLIO (4 cards):</p>
<p>Total de Microcontratos | Capital Total | Capital em Uso | Capital Retornado</p>
<p>MAPA DE BLOCOS (componente central — inovador):</p>
<p>Grid de pequenos quadradinhos (tipo GitHub contribution graph mas em tempo real)</p>
<p>Cada quadradinho = 1 micro-contrato (hash unico)</p>
<p>Cor: azul=deployed | verde=em uso | dourado=repago | vermelho=inadimplente | cinza=ocioso</p>
<p>Hover em qualquer quadradinho: tooltip com sub-hash | vertical | valor | estado | dias restantes</p>
<p>Click em quadradinho: abre painel lateral com historico completo daquele bloco</p>
<p>Legenda de cores abaixo do grid | filtros por estado acima do grid</p>
<p>TABELA DE EVENTOS (abaixo do mapa):</p>
<p>Timeline de todos os eventos do portfolio: deposito | alocacao | uso | repagamento | default</p>
<p>Cada evento: timestamp | tipo | valor | hash do micro-contrato afetado | estado resultante</p>
<p>Filtros: por tipo de evento | por data | por vertical</p>
<p>PAINEL LATERAL DE BLOCO (abre ao clicar no quadradinho):</p>
<p>Sub-hash do bloco | Usuario ID anonimo | Vertical | Estado atual</p>
<p>Historico de uso: grafico de barras mensais (usou quanto cada mes)</p>
<p>Projecao de retorno deste bloco especifico</p>
<p>Botao 'Listar no Mercado Secundario' (se SEP)</p></td>
</tr>
</tbody>
</table>

**TELA A-05 — Mercado Secundario de Contratos**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA A-05: MERCADO SECUNDARIO (SEP)</strong></p>
<p>Crie uma tela de marketplace interno para compra e venda de contratos P2P entre Aplicantes.</p>
<p>Visual inspirado em marketplaces de NFT (OpenSea) mas com linguagem financeira. Dark mode.</p>
<p>TOPO: Headline 'Mercado de Contratos NEXUS' | Metricas: [Volume 24h: R$ X] [Contratos Listados: N]</p>
<p>[Preco Medio: X% do face value] | Barra de busca global</p>
<p>FILTROS (linha horizontal abaixo do header):</p>
<p>Vertical (multiselect) | Estado (Ativo/Renegociado) | Faixa de Valor | % do Face Value</p>
<p>Score de Saude do Usuario (A+/A/B+/B/C) | Dias ate vencimento</p>
<p>GRID DE CONTRATOS (3 colunas no desktop, 2 tablet, 1 mobile):</p>
<p>Cada card de contrato:</p>
<p>- Topo colorido com a cor da vertical (ex: verde para saude)</p>
<p>- Icone da vertical + nome da vertical</p>
<p>- Hash truncado do contrato (NexusHash)</p>
<p>- 'Face Value: R$ XXX' | 'Preco Pedido: R$ YYY (ZZ% do face)'</p>
<p>- Barra de saude: score de adimplencia do usuario (anonimizado)</p>
<p>- Historico: grafico micro de barras (pagamentos em dia nos ultimos 6 meses)</p>
<p>- Badge: [Vendendo] ou [Leilao] ou [Oferta Relampago]</p>
<p>- Botao 'Comprar Agora' ou 'Fazer Oferta'</p>
<p>PAINEL DE VENDA (para o Aplicante que quer vender):</p>
<p>Botao flutuante 'Listar Contrato' — abre modal:</p>
<p>Selector do contrato a listar | tipo: venda imediata ou leilao</p>
<p>Preco pedido (sugestao automatica da plataforma baseada em score)</p>
<p>Aviso de taxa da plataforma (1%) | confirmacao e listagem</p>
<p>PAGINA DE DETALHE DO CONTRATO (ao clicar em um card):</p>
<p>Hash completo | Vertical | Score de saude do devedor (anonimizado)</p>
<p>Historico completo de pagamentos (grafico de barras mensais)</p>
<p>Comparativo: este contrato vs media da vertical</p>
<p>Box de compra: preco | quantidade (1 unidade) | taxa | total | botao 'Confirmar Compra'</p></td>
</tr>
</tbody>
</table>

**PARTE 3 — MODULO DO USUARIO (TOMADOR DE CREDITO)**

O Usuario e o tomador de credito. Suas telas devem ser SIMPLES, ENCORAJADORAS e UTEIS. Nao deve haver jargao financeiro excessivo. Design mais claro, acessivel e mobile-first. Inspiracoes: Nubank app, C6 Bank, Wise — clean, colorido com acentos verdes.

**TELA U-01 — Onboarding / Qualificacao do Usuario**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA U-01: ONBOARDING USUARIO</strong></p>
<p>Crie um fluxo de onboarding multi-etapas para o Usuario NEXUS. Mobile-first. Light mode predominante.</p>
<p>Progress bar no topo mostrando etapa atual (ex: '3 de 7'). Animacoes de transicao entre etapas.</p>
<p>ETAPA 1 — BEM-VINDO: Animacao lottie de cartao NEXUS aparecendo. Headline: 'Seu cartao de credito</p>
<p>inteligente'. Subheadline: 'Credito ate R$ 2.500 para o que voce precisa todo mes'.</p>
<p>Botao 'Comecar minha solicitacao' | Link 'Como funciona?' (bottom sheet com explicacao)</p>
<p>ETAPA 2 — DADOS PESSOAIS: Nome completo | CPF | Data de nascimento | Genero (opcional)</p>
<p>Todos como NexusInput mas em versao light | Validacao em tempo real | Teclado numerico para CPF/data</p>
<p>ETAPA 3 — CONTATO E ENDERECO: Celular (com validacao via SMS) | Email | CEP (auto-complete)</p>
<p>Endereco completo | Botao 'Usar localizacao atual' para preencher CEP</p>
<p>ETAPA 4 — DOCUMENTOS: Upload de foto do RG/CNH (frente e verso) + selfie segurando documento</p>
<p>Instrucoes visuais com ilustracao mostrando como tirar a foto corretamente</p>
<p>Opcao de usar camera do celular em tempo real (WebRTC) ou upload de arquivo</p>
<p>ETAPA 5 — RENDA: Pergunta simples: 'Qual sua renda mensal aproximada?'</p>
<p>Selector de faixas (nao input livre): R$ 1k-2k | R$ 2k-4k | R$ 4k-8k | Acima de R$ 8k</p>
<p>Upload opcional de comprovante (holerite, extrato) com texto 'Aumenta sua chance de aprovacao'</p>
<p>ETAPA 6 — AUTORIZACAO DE CONSULTA: Checkbox para consulta ao Serasa/SPC</p>
<p>Explicacao visual simples do que isso significa | Link para politica de privacidade</p>
<p>ETAPA 7 — AGUARDANDO ANALISE: Animacao de loading/analise | ETA: '2 a 24 horas'</p>
<p>Botao 'Ativar notificacoes' (push) | Link 'O que acontece agora?' (FAQ bottom sheet)</p>
<p>Mensagem: 'Seu Gerente de Contas entrara em contato pelo Whatsapp em breve'</p></td>
</tr>
</tbody>
</table>

**TELA U-02 — Home do Usuario (App do Cartao)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA U-02: HOME USUARIO</strong></p>
<p>Crie a tela principal do app do Usuario NEXUS apos aprovacao. Mobile-first (375px width).</p>
<p>Design clean com fundo branco/light grey e acentos em verde NEXUS (#27AE60).</p>
<p>TOP BAR: Logo NEXUS pequeno | Saudacao: 'Ola, [Nome]!' | Icone de notificacao | Avatar</p>
<p>HERO CARD (cartao virtual animado, estilo cartao de credito fisico):</p>
<p>Fundo: gradiente diagonal de #0D1B2A para #132135 (cartao dark premium)</p>
<p>Logo NEXUS + bandeira Visa/Mastercard no canto</p>
<p>Numero do cartao mascarado: **** **** **** 4782</p>
<p>Nome do titular | Validade | CVV (mostrar ao pressionar e segurar)</p>
<p>Valor disponivel em destaque: 'R$ 1.847,00 disponivel'</p>
<p>Tap para virar o cartao e ver codigo de segurança (animacao flip 3D)</p>
<p>METRICAS RAPIDAS (linha abaixo do cartao, 3 chips horizontais scroll):</p>
<p>[Limite Total: R$ 2.500] [Usado: R$ 653] [Vence em: 18 dias]</p>
<p>ACOES RAPIDAS (4 botoes em grid 2x2 com icones):</p>
<p>[Ver Fatura] [Pagar Agora (Pix)] [Extrato] [Falar com Assistente]</p>
<p>GASTOS RECENTES (lista vertical, estilo Nubank):</p>
<p>Cada item: icone do merchant (favicon ou icone da categoria) | nome do merchant</p>
<p>Data/hora | valor | categoria (chip colorido)</p>
<p>Botao 'Ver todos os gastos'</p>
<p>BARRA INFERIOR NAVEGACAO (fixed bottom): [Home] [Cartao] [Extrato] [Perfil] [Ajuda]</p>
<p>ALERTA DE USO (banner amber se usuario nao usou o cartao na semana):</p>
<p>'Voce tem R$ 1.847 disponiveis — lembre de usar antes do vencimento!'</p>
<p>Botao 'Ver merchants parceiros'</p></td>
</tr>
</tbody>
</table>

**TELA U-03 — Extrato e Historico de Gastos**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA U-03: EXTRATO USUARIO</strong></p>
<p>Crie a tela de extrato do Usuario NEXUS. Mobile-first. 5 anos de historico navegavel.</p>
<p>HEADER: 'Meu Extrato' | Seletor de periodo: [Mes atual] [Mes anterior] | date picker para periodos customizados</p>
<p>RESUMO DO PERIODO (card compacto no topo):</p>
<p>Total gasto | Total pago | Economia com merchants parceiros (cashback/desconto)</p>
<p>GRAFICO DE GASTOS POR CATEGORIA (donut chart compacto):</p>
<p>Ao tap em uma fatia: filtra a lista abaixo para aquela categoria</p>
<p>LISTA DE TRANSACOES (agrupadas por data):</p>
<p>Separador de data: 'Hoje', 'Ontem', 'Quinta-feira, 3 de Abril'</p>
<p>Cada transacao: icone categoria | nome do merchant | hora | valor | status (processado/pendente)</p>
<p>Swipe left em uma transacao: opcoes de contestar/detalhar</p>
<p>Tap em uma transacao: bottom sheet com detalhes completos</p>
<p>BOTTOM SHEET DE DETALHE DA TRANSACAO:</p>
<p>Icone grande do merchant | nome | data e hora exata | valor | categoria</p>
<p>Mapa com localizacao do merchant (se disponivel)</p>
<p>Botao 'Contestar esta cobrança' (abre fluxo de disputa)</p>
<p>Botao 'Repetir esta compra' (redireciona para merchant se app disponivel)</p>
<p>SECAO 'HISTORICO COMPLETO': timeline por ano (dropdown), navegar ate 5 anos atras</p>
<p>Botao 'Baixar extrato PDF' e 'Exportar CSV'</p></td>
</tr>
</tbody>
</table>

**TELA U-04 — Tela de Pagamento de Fatura (Pix)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA U-04: PAGAMENTO DE FATURA</strong></p>
<p>Crie a tela de pagamento de fatura do Usuario NEXUS. Mobile-first. Deve ser SIMPLES e TRANQUILIZADORA.</p>
<p>HEADER: 'Pagar Fatura' com botao voltar</p>
<p>CARD DA FATURA ATUAL:</p>
<p>Valor a pagar em destaque grande (verde se em dia, vermelho se vencida)</p>
<p>Detalhamento: 'Valor utilizado: R$ X' + 'Taxa de utilizacao (6%): R$ Y' = 'Total: R$ Z'</p>
<p>Data de vencimento | Dias restantes (ou 'VENCIDA ha X dias' em vermelho)</p>
<p>Link 'Ver detalhes da fatura' (expande com lista de transacoes)</p>
<p>OPCOES DE PAGAMENTO:</p>
<p>[Pix — Copia e Cola] (recomendado, verde) — gera chave Pix instantaneamente</p>
<p>[Pix — QR Code] — exibe QR Code com timer de validade</p>
<p>[Codigo de Barras] — exibe codigo e botao copiar</p>
<p>FLUXO PIX:</p>
<p>Ao selecionar Pix: modal com QR Code grande + chave Pix + valor + botao 'Copiar codigo'</p>
<p>Timer de 30 minutos para validade do QR Code</p>
<p>Animacao de sucesso ao detectar pagamento: confetti + 'Fatura paga! Seu credito foi renovado'</p>
<p>SLIDER 'QUANTO PAGAR' (para pagamento parcial se permitido pela politica):</p>
<p>Slider de 0% a 100% do valor total</p>
<p>Aviso: 'Pagar menos do que o total gera juros sobre o saldo restante'</p>
<p>APOS PAGAMENTO CONFIRMADO:</p>
<p>Tela de sucesso: animacao check verde | 'Fatura paga com sucesso!'</p>
<p>'Seu limite de R$ 2.500 esta disponivel novamente'</p>
<p>Botao 'Ver limite disponivel' | Botao 'Voltar para Home'</p></td>
</tr>
</tbody>
</table>

**PARTE 4 — MODULO DO EXECUTIVO DE CONTAS**

O Executivo de Contas gerencia sua base de Usuarios e Merchants em campo. Suas telas devem ser FUNCIONAIS e RAPIDAS, como um CRM mobile. Design: dark mode opcional, primario em azul escuro + roxo NEXUS.

**TELA E-01 — CRM Dashboard do Executivo**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA E-01: DASHBOARD EXECUTIVO</strong></p>
<p>Crie o dashboard CRM do Executivo de Contas NEXUS. Desktop com opcao mobile.</p>
<p>Layout com sidebar esquerda + conteudo principal + mini-painel direito.</p>
<p>SIDEBAR (240px): Logo | Avatar + nome + cargo (Ex: Exec. Senior - Zona Sul SP)</p>
<p>Menu: [Minha Base] [Qualificacoes Pendentes] [Merchants] [Desempenho] [Comunicacao] [Configuracoes]</p>
<p>HERO METRICS (4 cards no topo do conteudo):</p>
<p>[Usuarios Ativos na Base] [Adimplencia da Base (%)] [MDR Gerado no Mes (R$)] [Novos Usuarios no Mes]</p>
<p>MAPA TERRITORIAL (60% do conteudo, esquerda):</p>
<p>Mapa do Brasil com zoom na area do Executivo</p>
<p>Pins coloridos: verde=usuario ativo | amarelo=usuario pendente | vermelho=inadimplente | azul=merchant</p>
<p>Filtros por tipo acima do mapa | Click em pin: popup com info resumida + botao 'Ver detalhes'</p>
<p>LISTA DE ALERTAS (40% direita):</p>
<p>Usuarios em risco (pagamento vencendo em 3 dias) | Novos qualificacoes aguardando revisao</p>
<p>Merchants com baixo volume no mes | Metas do mes (progress bars)</p>
<p>TABELA DA BASE (full width abaixo): NexusTable de todos os usuarios da base</p>
<p>[ID anonimo] [Vertical] [Limite] [Usado%] [Status] [Ultimo Pagamento] [Score] [Acoes]</p>
<p>Acoes: [Ver perfil] [Ligar/Whatsapp] [Adicionar nota] [Escalar]</p>
<p>Filtros: por status | por vertical | por nivel de risco | busca por ID</p>
<p>PAINEL DE COMISSOES (mini-painel direito fixo):</p>
<p>MDR acumulado no mes | Projecao de comissao ao final do mes</p>
<p>Comparativo com meta | Ranking da equipe (posicao anonimizada)</p></td>
</tr>
</tbody>
</table>

**TELA E-02 — Perfil e Qualificacao de Usuario**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA E-02: QUALIFICACAO DE USUARIO</strong></p>
<p>Crie a tela de revisao e qualificacao de novo Usuario pelo Executivo de Contas.</p>
<p>LAYOUT: 2 colunas. Esquerda: dados do candidato. Direita: decisao e notas.</p>
<p>COLUNA ESQUERDA — FICHA DO CANDIDATO:</p>
<p>Foto do documento (mascara automatica do nome) | Score do Bureau (gauge chart, Serasa style)</p>
<p>Informacoes pessoais basicas (com mascaramento de CPF) | Renda declarada vs. comprovada</p>
<p>DTI (Debt-to-Income ratio) calculado automaticamente | Historico em outras plataformas (se Open Finance)</p>
<p>Score NEXUS (calculado pelo motor interno) — gauge chart colorido A+/A/B+/B/C</p>
<p>Documentos anexados: miniaturas com botao de ampliar</p>
<p>COLUNA DIREITA — PAINEL DE DECISAO:</p>
<p>Headline: 'Sua Avaliacao'</p>
<p>Limite Sugerido pelo Sistema: R$ X (baseado no score)</p>
<p>Slider para o Executivo ajustar: de R$ 500 a R$ 2.500 (com justificativa obrigatoria se alterar)</p>
<p>Dropdown 'Vertical de Enquadramento': lista das 12 verticais</p>
<p>Dropdown 'Vertical Secundaria' (opcional)</p>
<p>Textarea 'Notas do Executivo' (campo obrigatorio, min 100 caracteres)</p>
<p>Toggle 'Exige documentacao adicional' — habilita campo para especificar o que falta</p>
<p>Botoes de decisao:</p>
<p>[Aprovar e Emitir Cartao] (verde) | [Solicitar mais documentos] (amber) | [Reprovar] (vermelho)</p>
<p>Ao aprovar: modal de confirmacao com preview do cartao que sera emitido</p></td>
</tr>
</tbody>
</table>

**PARTE 5 — MODULO 360 BOARD (VISAO EXECUTIVA)**

O 360 Board e o sistema nervoso central da empresa. Deve ser poderoso como um Bloomberg Terminal, mas intuitivo como um painel da Datadog. Dark mode absoluto. Inspiracoes: Palantir Gotham, Grafana, Retool dashboards, Looker Studio premium.

**TELA B-01 — Visao Geral da Plataforma (CEO/Board)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA B-01: 360 BOARD VISAO GERAL</strong></p>
<p>Crie o dashboard executivo 360 do NEXUS para CEO e Board. Dark mode absoluto.</p>
<p>Layout full-screen sem sidebar — navegacao por top tabs.</p>
<p>TOP BAR: Logo NEXUS | 'NEXUS 360 BOARD — VISAO EXECUTIVA' | Data/hora em tempo real</p>
<p>Status da plataforma: [dot verde] 'Todos os sistemas operacionais'</p>
<p>Tabs: [Visao Geral] [Carteira] [Executivos] [Merchants] [Financeiro] [Risco] [IA Insights]</p>
<p>TAB: VISAO GERAL</p>
<p>ROW 1 — KPIs EM TEMPO REAL (6 cards em linha, numeros grandes animados):</p>
<p>Capital sob Gestao (R$) | Cartoes Ativos | Adimplencia (%) | MDR do Dia (R$)</p>
<p>Novos Usuarios Hoje | Aplicantes Ativos</p>
<p>ROW 2 — MAPA DO BRASIL (60% esq) + GRAFICO TEMPORAL (40% dir):</p>
<p>Mapa: calor de atividade por estado/regiao | Hover: metricas do estado</p>
<p>Grafico: volume de transacoes nas ultimas 24h (area chart com hora no eixo X)</p>
<p>ROW 3 — METRICAS DE NEGOCIO (4 cards medios):</p>
<p>Top 5 Verticais por Volume | Taxa de Conversao Qualificacao-&gt;Aprovacao</p>
<p>Custo de Aquisicao de Usuario (CAC) | LTV medio do Usuario</p>
<p>ROW 4 — ALERTAS E ANOMALIAS (full width):</p>
<p>Lista de alertas em tempo real: [critico/warning/info] | timestamp | descricao | acao recomendada</p>
<p>Botao 'Ver todos os alertas' | Filtro por severidade</p>
<p>TAB: FINANCEIRO</p>
<p>P&amp;L em tempo real: receitas vs custos vs EBITDA no mes (waterfall chart)</p>
<p>Projecao de fechamento do mes | Comparativo com mes anterior e meta</p>
<p>Breakdown de receitas: MDR | Taxa de intermediacao | Spread de cambio | Outros</p>
<p>Custos por centro de custo | Fluxo de caixa projetado 90 dias</p>
<p>Botao 'Exportar para ODOO' (integra com ERP contabil)</p>
<p>TAB: RISCO</p>
<p>Mapa de calor de risco por vertical e por regiao</p>
<p>Curva de inadimplencia vs historico | VaR (Value at Risk) da carteira</p>
<p>Stress test: simulador de cenarios de inadimplencia com impacto no P&amp;L</p>
<p>Alertas de concentracao: verticais ou regioes com exposicao acima do limite</p>
<p>TAB: IA INSIGHTS</p>
<p>Chat com IA do Board: pergunta em linguagem natural, responde com graficos gerados on-the-fly</p>
<p>Ex: 'Qual vertical tem maior risco de inadimplencia em SP nos proximos 30 dias?'</p>
<p>Insights automaticos diarios: 3-5 observacoes geradas pela IA sobre a operacao</p>
<p>Botao 'Gerar Relatorio Executivo PDF' (exporta um one-pager com os principais KPIs)</p></td>
</tr>
</tbody>
</table>

**TELA B-02 — Visao do Executivo de Contas no 360 (com trava de hash)**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA B-02: 360 VISAO EXECUTIVO (ISOLADA)</strong></p>
<p>Crie a versao do 360 Board restrita ao Executivo de Contas — ele ve SOMENTE sua base.</p>
<p>Mesma estetica do Board, mas com banner superior indicando o escopo restrito.</p>
<p>BANNER TOPO (azul escuro, full width): 'Voce esta visualizando os dados da sua base — Zona Sul SP'</p>
<p>Hash do Executivo (NexusHash): 'EXE-A4F2...B91C' | Tooltip: 'Este hash identifica sua base de dados'</p>
<p>CONTEUDO — MESMO LAYOUT DO B-01, MAS RESTRITO A BASE DO EXECUTIVO:</p>
<p>Todos os numeros referentes apenas aos seus Usuarios e Merchants</p>
<p>Mapa mostrando apenas sua area de atuacao</p>
<p>Nenhum dado de outros Executivos visivel (mesmo que o usuario tente manipular a URL)</p>
<p>ADICIONAL — SECAO 'MINHA PERFORMANCE':</p>
<p>Ranking anonimizado: 'Voce esta em [X] lugar entre [N] Executivos da sua regiao'</p>
<p>Metas do mes: progress bars para: novos usuarios | MDR gerado | adimplencia da base</p>
<p>Projecao de comissao: 'Com o ritmo atual, sua comissao sera de R$ X este mes'</p>
<p>TRAVA TECNOLOGICA (comentario no codigo — nao visivel ao usuario):</p>
<p>O backend filtra todos os dados pelo HASH do Executivo logado</p>
<p>Frontend nunca recebe dados fora do escopo — nao ha possibilidade de inspecao</p>
<p>Qualquer tentativa de acesso fora do escopo: log de auditoria + alerta ao CCROO</p></td>
</tr>
</tbody>
</table>

**PARTE 6 — TELAS ADMINISTRATIVAS E DE SUPORTE**

**TELA AD-01 — Painel de AML/KYC Compliance**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA AD-01: PAINEL AML/KYC</strong></p>
<p>Crie o painel de compliance AML/KYC para o time CCROO (Compliance Officer).</p>
<p>Dark mode. Layout de dois paineis: lista de casos + detalhe do caso selecionado.</p>
<p>PAINEL ESQUERDO (380px) — FILA DE CASOS:</p>
<p>Tabs: [Pendentes] [Em Analise] [Aprovados] [Negados] [Escalados ao COAF]</p>
<p>Cada item na lista: tipo (Aplicante/Usuario/Merchant) | ID | Risco (A/B/C/D) | Tempo na fila</p>
<p>Ordenacao por: risco | tempo na fila | tipo | data</p>
<p>Barra de busca | Filtros rapidos</p>
<p>PAINEL DIREITO (flex) — DETALHE DO CASO:</p>
<p>Header: tipo do caso + ID + status atual + tempo em analise</p>
<p>Score de risco AML (gauge 0-100) gerado pelo motor de IA</p>
<p>Alertas disparados: lista de red flags identificados automaticamente</p>
<p>Timeline de eventos: todas as acoes do usuario na plataforma</p>
<p>Documentos enviados: visualizador inline (sem download obrigatorio)</p>
<p>PEP check | Sanction list check | Adversarial media search (resultado automatico)</p>
<p>Campo de notas do compliance officer</p>
<p>Botoes: [Aprovar] [Solicitar documentos] [Negar] [Escalar ao COAF]</p>
<p>Ao escalar ao COAF: formulario de preenchimento do RIF (Relatorio de Inteligencia Financeira)</p></td>
</tr>
</tbody>
</table>

**TELA AD-02 — Canal de Comunicacao Usuario-Assistente**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT PARA IA — TELA AD-02: CHAT USUARIO-ASSISTENTE</strong></p>
<p>Crie a interface de chat entre Usuario e Assistente Executivo NEXUS. Mobile-first.</p>
<p>Estilo: WhatsApp Business / Intercom — familiar e acolhedor.</p>
<p>VISAO DO USUARIO (app mobile):</p>
<p>Header: foto do Assistente + nome + 'Online' ou ultima vez online</p>
<p>Area de chat: bolhas de mensagem (usuario = direita, azul; assistente = esquerda, branco)</p>
<p>Tipos de mensagem suportados: texto | imagem | PDF | link de pagamento (Pix deeplink)</p>
<p>Input area: campo de texto | icone de anexo | icone de microfone | botao enviar</p>
<p>Quick replies: chips pre-configurados: ['Quero pagar minha fatura'] ['Estou com dificuldades']</p>
<p>['Quero aumentar meu limite'] ['Contestar uma cobrança']</p>
<p>VISAO DO ASSISTENTE EXECUTIVO (desktop ou mobile):</p>
<p>Multi-inbox: lista de conversas na esquerda (ordenada por urgencia/tempo)</p>
<p>Cada item: avatar usuario (anonimizado) | ultima mensagem | tempo | status | badge de urgencia</p>
<p>No detalhe: mesma interface de chat + painel lateral com dados do usuario:</p>
<p>Score atual | Limite | Valor em uso | Status da fatura | Historico de pagamentos</p>
<p>Botoes rapidos: [Gerar link de pagamento] [Solicitar documentos] [Escalar para Executivo]</p>
<p>Templates de resposta rapida (snippets pre-aprovados pelo compliance)</p>
<p>Aviso: 'Todas as conversas sao gravadas e monitoradas conforme a LGPD'</p></td>
</tr>
</tbody>
</table>

**PARTE 7 — FLUXO DE NAVEGACAO E MAPA DE TELAS**

| **Codigo** | **Tela**                         | **Modulo** | **Acesso**     | **Status no Prompt**       |
| ---------- | -------------------------------- | ---------- | -------------- | -------------------------- |
| A-01       | Login / Onboarding Aplicante     | Aplicante  | Publico        | Completo acima             |
| A-02       | Dashboard Principal Aplicante    | Aplicante  | Aplicante auth | Completo acima             |
| A-03       | Composer de Portfolio            | Aplicante  | Aplicante auth | Completo acima             |
| A-04       | Macro Hash Ledger View           | Aplicante  | Aplicante auth | Completo acima             |
| A-05       | Mercado Secundario de Contratos  | Aplicante  | Aplicante auth | Completo acima             |
| A-06       | Relatorios e Extratos            | Aplicante  | Aplicante auth | Detalhar na proxima versao |
| A-07       | Perfil e Configuracoes           | Aplicante  | Aplicante auth | Detalhar na proxima versao |
| U-01       | Onboarding / Qualificacao        | Usuario    | Publico        | Completo acima             |
| U-02       | Home do Usuario (App Cartao)     | Usuario    | Usuario auth   | Completo acima             |
| U-03       | Extrato e Historico              | Usuario    | Usuario auth   | Completo acima             |
| U-04       | Pagamento de Fatura (Pix)        | Usuario    | Usuario auth   | Completo acima             |
| U-05       | Solicitar Aumento de Limite      | Usuario    | Usuario auth   | Detalhar na proxima versao |
| U-06       | Merchants Parceiros (mapa)       | Usuario    | Usuario auth   | Detalhar na proxima versao |
| U-07       | Negociacao de Debito             | Usuario    | Usuario auth   | Detalhar na proxima versao |
| E-01       | Dashboard CRM do Executivo       | Executivo  | Exec auth      | Completo acima             |
| E-02       | Qualificacao de Usuario          | Executivo  | Exec auth      | Completo acima             |
| E-03       | Gestao de Merchants              | Executivo  | Exec auth      | Detalhar na proxima versao |
| E-04       | Meu Desempenho e Comissoes       | Executivo  | Exec auth      | Detalhar na proxima versao |
| B-01       | 360 Board — Visao Geral          | Board      | CEO/Board auth | Completo acima             |
| B-02       | 360 — Visao Executivo (restrita) | Board      | Exec auth      | Completo acima             |
| B-03       | 360 — Visao Gerente de Area      | Board      | Gerente auth   | Detalhar na proxima versao |
| B-04       | 360 — Financeiro / P\&L          | Board      | CFO auth       | Incluido no B-01           |
| AD-01      | Painel AML/KYC Compliance        | Admin      | CCROO auth     | Completo acima             |
| AD-02      | Chat Usuario-Assistente          | Admin/User | Ambos          | Completo acima             |
| AD-03      | Gestao de Contratos              | Admin      | Backofc auth   | Detalhar na proxima versao |
| AD-04      | ODOO Integration Console         | Admin      | CFO/CTO auth   | Detalhar na proxima versao |

**PARTE 8 — PROMPT MESTRE CONSOLIDADO PARA IA GENERATIVA**

INSTRUCOES: Copie e cole o bloco abaixo diretamente em v0.dev, Lovable, Bolt.new, ou no prompt de qualquer LLM com capacidade de geracao de UI (GPT-4o, Claude 3.5+). Para melhores resultados, gere tela por tela usando o codigo de referencia (A-01, U-02, etc.).

<table>
<tbody>
<tr class="odd">
<td><p><strong>PROMPT MESTRE — COPIE ESTE BLOCO PARA GERAR AS TELAS</strong></p>
<p>=== NEXUS FINANCIAL PLATFORM — UI GENERATION PROMPT ===</p>
<p>Voce e um designer e engenheiro frontend senior. Vou te pedir para criar telas de uma</p>
<p>plataforma financeira P2P chamada NEXUS. Siga RIGOROSAMENTE estas especificacoes:</p>
<p>STACK TECNICA:</p>
<p>- Framework: React 18 + TypeScript</p>
<p>- Styling: Tailwind CSS (dark mode por padrao com classe 'dark')</p>
<p>- Componentes: shadcn/ui como base, customizados para o Design System NEXUS</p>
<p>- Graficos: Recharts para todos os charts (area, bar, donut, line, sparkline)</p>
<p>- Animacoes: Framer Motion para transicoes e microinteracoes</p>
<p>- Icones: Lucide React</p>
<p>- Mapas: Leaflet.js com tiles dark do CartoDB</p>
<p>- Fontes: Inter (principal) + JetBrains Mono (hashes/codigos) via Google Fonts</p>
<p>DESIGN TOKENS — USE EXATAMENTE ESTAS CORES:</p>
<p>--nexus-dark: #0D1B2A (background)</p>
<p>--nexus-surface: #132135 (cards)</p>
<p>--nexus-surface-2: #1C2E45 (hover/alternado)</p>
<p>--nexus-accent: #00B4D8 (CTAs, links)</p>
<p>--nexus-gold: #F5A623 (retornos, alertas positivos)</p>
<p>--nexus-green: #27AE60 (ativo, adimplente)</p>
<p>--nexus-red: #D62228 (inadimplente, erro)</p>
<p>--nexus-amber: #F39C12 (risco medio, pendente)</p>
<p>--nexus-purple: #6C3ABD (blockchain, hash, premium)</p>
<p>REGRAS DE DESIGN OBRIGATORIAS:</p>
<p>1. Dark mode em TODAS as telas de Aplicante, Executivo e Board</p>
<p>2. Light mode para telas do Usuario (app do cartao) — mais acessivel</p>
<p>3. Nunca use texto branco puro (#FFF) sobre fundo escuro — use rgba(255,255,255,0.87)</p>
<p>4. Cards sempre com border-radius: 16px e border: 1px solid rgba(255,255,255,0.08)</p>
<p>5. Hashes e codigos: fonte JetBrains Mono + background rgba(108,58,189,0.15) + padding</p>
<p>6. Valores monetarios grandes: font-size minimo 32px, color gold (#F5A623)</p>
<p>7. Status badges: sempre com icone circular (dot) antes do texto</p>
<p>8. Tabelas: sempre com virtualizacao se &gt;50 linhas (react-virtual)</p>
<p>9. Todos os numeros financeiros: animar ao mudar (react-spring counter animation)</p>
<p>10. Mobile-first para telas de Usuario; desktop-first para telas de Board/Executivo</p>
<p>PARA GERAR UMA TELA ESPECIFICA, USE O COMANDO:</p>
<p>'Gere a tela [CODIGO] — [NOME DA TELA] do NEXUS conforme especificacao acima'</p>
<p>Exemplo: 'Gere a tela A-02 — Dashboard Principal do Aplicante do NEXUS'</p>
<p>PARA GERAR O DESIGN SYSTEM COMPLETO:</p>
<p>'Gere o arquivo nexus-design-system.tsx com todos os componentes NexusCard,</p>
<p>NexusButton, NexusBadge, NexusHash, NexusTable, NexusInput, NexusProgress,</p>
<p>NexusSidebar, NexusStatusDot conforme especificacao acima'</p>
<p>=== FIM DO PROMPT MESTRE ===</p></td>
</tr>
</tbody>
</table>

**DICA DE USO: Para plataformas como v0.dev, use o prompt mestre acima seguido de:**

  - 'Create a complete React component for \[TELA CODE\] - \[NOME\]' — v0.dev gera com preview ao vivo

  - No Lovable.dev: 'Build the full \[MODULO\] module for NEXUS platform' — gera multiplas telas conectadas

  - No Bolt.new: 'Full-stack NEXUS \[MODULO\] with mock data and routing' — inclui backend mock

  - No Cursor: abra um repo React existente e use '@codebase Implement NEXUS tela A-02 following the design spec'

*NEXUS UI Specification v1.0 | Abril 2026 | Documento Confidencial | Todos os direitos reservados*
