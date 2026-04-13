---
title: "NEXUS — NEXUS_GREY_Whitepaper_v1"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>[ WHITEPAPER CONFIDENCIAL — DOCUMENTO GREY v1.0 — ABRIL 2026 ]</strong></p>
<p><strong>PROJECTO NEXUS GREY</strong></p>
<p><strong>Plataforma P2P de Crédito via Stablecoins</strong></p>
<p><em>SPE Exchange Proprietária · Cartão Pré-Pago · Investidores Globais · Arquitetura Descentralizada</em></p></td>
</tr>
</tbody>
</table>

*Este documento é de natureza estritamente confidencial e destinado exclusivamente a investidores, parceiros estratégicos e assessores jurídicos qualificados. Não constitui oferta pública de valores mobiliários nem instrumento de captação de recursos junto ao público em geral.*

**SUMÁRIO EXECUTIVO**

O Projeto NEXUS GREY apresenta uma arquitetura inovadora de crédito peer-to-peer que opera inteiramente sobre infraestrutura de stablecoins (USDT/USDC), liquidando os empréstimos em reais através de cartões pré-pagos emitidos via subadquirência internacional (Visa/Mastercard). A plataforma conecta Aplicantes (investidores) globais a Usuários (tomadores) brasileiros, com retornos de 3% a 5% ao mês, risco fracionado em até 1.800 microparticipações por carteira e rastreabilidade completa via MACRO HASH em ledger imutável.

A estrutura jurídica ancora-se em uma SPE Exchange (Special Purpose Entity) registrada em jurisdição favorável (preferencialmente Dubai DIFC, Ilhas Cayman ou BVI), operando como exchange de propósito específico para conversão stablecoin ↔ BRL e como compliance layer de toda a operação. Esta arquitetura posiciona a plataforma fora do perímetro regulatório direto do Banco Central do Brasil, enquanto mantém conformidade com normas internacionais de AML/KYC (FATF) e requisitos de licenciamento local de meios de pagamento.

<table>
<tbody>
<tr class="odd">
<td><p><strong>MÉTRICAS-ALVO — ANO 1 A 3</strong></p>
<p>▸ Aplicantes-alvo (Ano 1): 500 investidores | Capital sob gestão: R$ 50M–R$ 150M</p>
<p>▸ Usuários-alvo (Ano 1): 90.000 cartões ativos | Ticket médio: R$ 1.500</p>
<p>▸ Retorno ao Aplicante: 3,5% a 5,0% a.m. (42% a 60% a.a.)</p>
<p>▸ Taxa de inadimplência projetada: ≤ 7% (mitigada pelo fracionamento)</p>
<p>▸ Receita da plataforma via MDR Merchant: 3% sobre cada transação no cartão</p>
<p>▸ Break-even operacional projetado: mês 18 após go-live</p></td>
</tr>
</tbody>
</table>

**1. CONTEXTO GLOBAL — BENCHMARKS INTERNACIONAIS P2P LENDING**

O mercado global de P2P lending alcançou USD 134 bilhões em volume originado em 2024, com projeção de atingir USD 558 bilhões até 2030 (CAGR de 27,4%). A tabela abaixo apresenta os principais players por continente, seus modelos de negócio e métricas relevantes para orientar o posicionamento estratégico do Projeto NEXUS.

| **Plataforma** | **País/Região** | **Modelo**                   | **Volume Total** | **Retorno Inv.** | **Diferencial**                                     |
| -------------- | --------------- | ---------------------------- | ---------------- | ---------------- | --------------------------------------------------- |
| LendingClub    | EUA             | Originador direto (pós-2020) | USD 70B+         | N/A (inst.)      | Maior histórico P2P; migrou para banco digital      |
| Prosper        | EUA             | P2P Marketplace puro         | USD 22B+         | 5–8% a.a.        | Último grande P2P EUA; USD 2,2B originados 2024     |
| Mintos         | Letônia/UE      | Marketplace de crédito       | EUR 7B+          | 8–12% a.a.       | 340k investidores; mercado secundário robusto       |
| Bondora        | Estônia/UE      | Go\&Grow produto fixo        | EUR 805M+        | 6% a.a.          | Liquidez diária; produto simplificado               |
| Twino          | Letônia/UE      | P2P com buyback guarantee    | EUR 1B+          | 8–10% a.a.       | Regulado FKTK; €1 mínimo; 15+ países                |
| Funding Circle | UK/EUA/Ger      | SME lending                  | GBP 15B+         | 5–7% a.a.        | Foco PME; parcialmente institucionalizado           |
| Lufax          | China           | Wealth mgmt + P2P            | CNY 100B+        | 6–8% a.a.        | Maior P2P chinesa; listada NYSE                     |
| Faircent       | Índia           | P2P consumer/business        | INR 5B+          | 12–18% a.a.      | Regulado RBI; 2M+ usuários                          |
| Modalku        | Indonésia/SE    | SME P2P                      | USD 4B+          | 10–14% a.a.      | Funding Societies; 6 países ASEAN                   |
| Beehive        | Dubai/MENA      | SME P2P, Sharia-compliant    | AED 2B+          | 9–14% a.a.       | Primeiro P2P regulado DIFC; adquirido e& enterprise |
| Nexoos         | Brasil          | PME P2P (SEP)                | R$ 500M+         | 15–25% a.a.      | Licença SEP Bacen; foco PME                         |
| Biva           | Brasil          | SMB community lending        | R$ 200M+         | 18–22% a.a.      | Comunidade investidores pessoa física               |
| SocietyOne     | Austrália       | Consumer P2P                 | AUD 1B+          | 7–10% a.a.       | 1º P2P Austrália (2012); trust units                |
| Squirrel NZ    | Nova Zelândia   | P2P com secondary market     | NZD 500M+        | 6–9% a.a.        | 1º com mercado secundário na NZ                     |
| Goldfinch      | Global/DeFi     | DeFi P2P stablecoin          | USD 150M+        | 10–15% a.a.      | USDC para mercados emergentes; defaults em 2024     |
| Maple Finance  | Global/DeFi     | Institutional DeFi lending   | USD 4B+          | 8–12% a.a.       | 500%+ crescimento 2024; foco institucional          |

**1.1 Lições Críticas dos Benchmarks para o NEXUS GREY**

A análise comparativa dos principais players globais revela seis lições estruturantes que fundamentam as escolhas de design do Projeto NEXUS:

  - Fracionamento de risco (Mintos, Twino): distribuição por múltiplos originadores reduz correlação de default. O NEXUS leva isso ao extremo com microparcelas de até 1.800 usuários por portfólio.

  - Buyback guarantee como âncora de confiança (Twino, Mintos): garantias de recompra aumentam conversão de novos investidores. O NEXUS implementa Fundo de Reserva de Liquidez (FRL) como equivalente.

  - Stablecoin como camada de liquidação (Goldfinch, Maple): elimina risco cambial intraoperação. NEXUS usa USDT/USDC com conversão BRL apenas no on-ramp do cartão.

  - Dashboard de investidor rico e transparente (Prosper, Maple): investidores exigem visibilidade granular. O MACRO HASH do NEXUS entrega rastreabilidade de centavo a centavo.

  - Regulação como produto (Bondora, Beehive): regulação clara vira vantagem competitiva no pitch para investidores institucionais. Estratégia de jurisdição Dubai DIFC/Cayman é deliberada.

  - Cautela com DeFi puro (Goldfinch): defaults de USD 14M+ em 2024 mostram que o modelo DeFi puro sem curadoria humana é frágil. NEXUS combina smart contracts com Executivos de Contas presenciais.

**2. ARQUITETURA DO MODELO DE NEGÓCIO**

**2.1 Fluxo Operacional Macro**

O modelo opera em quatro camadas sequenciais, cada uma separada por controles de compliance e tecnologia de ledger distribuído:

<table>
<tbody>
<tr class="odd">
<td><p><strong>CAMADA 1 — CAPTAÇÃO (Aplicante → SPE Exchange)</strong></p>
<p>Aplicante (global) converte capital fiat/crypto em USDT/USDC via SPE Exchange proprietária</p>
<p>Capital entra em Smart Contract de Pool segregado por portfólio (hash único por Aplicante)</p>
<p>KYC/AML do Aplicante realizado pela SPE Exchange (padrão FATF Recommendation 16)</p>
<p>Contrato mínimo de 18 meses | Reinvestimento automático de juros recebidos na cota</p>
<p>Retorno prometido: 3,5% a.m. (portfólios baixo risco) até 5,0% a.m. (portfólios alto risco)</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>CAMADA 2 — DISTRIBUIÇÃO (SPE Exchange → Cartão Usuário)</strong></p>
<p>Motor de matching atribui microcréditos do pool a Usuários qualificados por vertical</p>
<p>Cada Usuário recebe microparcelas de N Aplicantes diferentes (máx. R$ 40/Aplicante por cartão)</p>
<p>Conversão USDT → BRL executada via parceiro de câmbio licenciado (ex: Transfero, Hashdex, BS2)</p>
<p>Valor creditado no cartão pré-pago emitido via BIN Sponsor (Visa/Mastercard via Rain, Reap ou Gnosis Pay)</p>
<p>Limite do cartão: R$ 500 a R$ 2.500 | Uso compulsório mensal do crédito disponível</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>CAMADA 3 — REPAGAMENTO (Usuário → Motor de Distribuição)</strong></p>
<p>Usuário paga fatura do cartão + 6% de ágio sobre o valor total utilizado</p>
<p>Sistema AGENTIC AI identifica o bloco de crédito de cada Aplicante no repagamento</p>
<p>Capital repago convertido de BRL → USDT e retorna ao pool do Aplicante (+ rendimento)</p>
<p>Ciclo se reinicia: crédito disponibilizado novamente no cartão do Usuário (recorrência)</p>
<p>Inadimplência &gt;30 dias: bloqueio do cartão + acionamento do Executivo de Contas</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>CAMADA 4 — LEDGER &amp; TRANSPARÊNCIA (MACRO HASH)</strong></p>
<p>Cada portfólio gera um hash único imutável no ledger da SPE Exchange</p>
<p>Cada microcrédito dentro do portfólio tem um sub-hash rastreável</p>
<p>Estados possíveis de cada bloco: DEPLOYED | ACTIVE_USE | IDLE | REPAID | DEFAULT</p>
<p>Aplicante visualiza em tempo real % do capital em cada estado (sem dados pessoais do Usuário)</p>
<p>Relatórios contábeis exportados automaticamente para ODOO (módulo contabilidade)</p></td>
</tr>
</tbody>
</table>

**2.2 Estrutura de Verticais de Consumo**

Os Usuários são classificados em Verticais de Consumo durante o processo de qualificação, definindo onde os créditos do cartão poderão ser utilizados (MCCs habilitados). Cada vertical tem um perfil de risco, retorno ao Aplicante e score de adimplência associados:

| **Vertical**  | **Descrição dos MCCs habilitados**                     | **Score Risco** | **Ret. Aplicante/mês** | **Adimplência Projetada** |
| ------------- | ------------------------------------------------------ | --------------- | ---------------------- | ------------------------- |
| SAÚDE         | Planos de saúde, farmácias, medicamentos, clínicas     | BAIXO           | 3,5%                   | 96%                       |
| SEGUROS       | Seguros auto, vida, residencial, prestamista           | BAIXO           | 3,5%                   | 95%                       |
| EDUCAÇÃO      | Mensalidades escolares, cursos, universidades privadas | BAIXO-MED       | 3,8%                   | 94%                       |
| CONTAS FIXED  | Energia, água, gás, internet, telefonia (débito auto)  | BAIXO           | 3,5%                   | 96%                       |
| SUPERMERCADO  | Supermercados, hipermercados, atacarejo                | MÉDIO           | 4,0%                   | 93%                       |
| TRANSPORTE    | Combustível, pedágio, transporte de carga, frete       | MÉDIO           | 4,0%                   | 92%                       |
| ALIMENTAÇÃO   | Restaurantes, delivery, refeições                      | MÉDIO           | 4,2%                   | 91%                       |
| VEÍCULOS      | Financiamento de veículos, manutenção, seguros auto    | MÉDIO-ALT       | 4,5%                   | 90%                       |
| VIAGEM        | Passagens aéreas, hotéis, pacotes de viagem, Airbnb    | MÉDIO-ALT       | 4,5%                   | 89%                       |
| AGRO MICRO    | Implementos agrícolas, insumos, equipamentos micro     | MÉDIO-ALT       | 4,8%                   | 88%                       |
| REFORMA/CONS  | Material de construção, reformas, home improvement     | ALTO            | 5,0%                   | 87%                       |
| CONSUMO GERAL | Eletrodomésticos, eletrônicos, bens duráveis           | ALTO            | 5,0%                   | 86%                       |

**REGRA DE DIVERSIFICAÇÃO OBRIGATÓRIA: Nenhum Aplicante pode ter mais de 25% do portfólio em uma única vertical. A plataforma impõe automaticamente essa restrição no momento da composição da carteira, garantindo exposição mínima a verticais de maior risco para balancear retorno e estabilidade.**

**3. SPE EXCHANGE — ARQUITETURA JURÍDICA E OPERACIONAL**

A SPE Exchange (Special Purpose Entity Exchange) é o coração jurídico e operacional do Documento GREY. Ela opera como exchange de propósito específico, sendo responsável por: (i) custódia de stablecoins dos Aplicantes; (ii) compliance AML/KYC; (iii) liquidação das operações de câmbio stablecoin ↔ BRL; e (iv) emissão e gestão dos contratos de participação nos portfólios.

**3.1 Jurisdições Candidatas e Análise Comparativa**

| **Jurisdição** | **Regime Regulatório**                     | **Licença Necessária**         | **Capital Mínimo** | **Tributação**            | **Score** |
| -------------- | ------------------------------------------ | ------------------------------ | ------------------ | ------------------------- | --------- |
| Dubai (DIFC)   | DFSA — Dubai Financial Services Authority  | Category 3C (Arranging Credit) | USD 500k           | 0% IR corporativo         | ★★★★★     |
| Dubai (ADGM)   | FSRA — Financial Services Regulatory Auth. | Lending / Arranging            | USD 250k           | 0% IR corporativo         | ★★★★★     |
| Ilhas Cayman   | CIMA — Cayman Islands Monetary Authority   | Virtual Asset Service Provider | USD 100k           | 0% qualquer tributo       | ★★★★☆     |
| BVI            | FSC — Financial Services Commission        | Money Services Business        | USD 50k            | 0% IR corporativo         | ★★★★☆     |
| Malta          | MiCA (UE) + MFSA                           | VASP + E-Money Institution     | EUR 730k           | 35% (créditos possíveis)  | ★★★☆☆     |
| Singapura      | MAS — Monetary Authority of Singapore      | Major Payment Institution      | SGD 250k           | 17% IR corp (territorial) | ★★★★☆     |
| El Salvador    | BCR — Banco Central de Reserva             | Digital Asset Service Provider | USD 50k            | 0% crypto gains           | ★★★☆☆     |

**RECOMENDAÇÃO: Dubai DIFC ou ADGM como jurisdição primária, com estrutura holding em Cayman para segregação patrimonial. Dubai oferece a combinação única de regulação reconhecida internacionalmente (padrão FATF), acesso a investidores do Golfo/Ásia, tributação zero e infraestrutura bancária de ponta para fintechs.**

**3.2 Infraestrutura de Cartão — Subadquirência Internacional**

Para a emissão do cartão pré-pago que materializa o crédito do Usuário, o NEXUS utiliza a infraestrutura de BIN Sponsorship e stablecoin-to-fiat já disponível no mercado global. Os principais parceiros avaliados são:

| **Parceiro**       | **Tipo**             | **Bandeiras**   | **Moedas Suportadas** | **Cobertura Brasil**     | **Modelo**                   |
| ------------------ | -------------------- | --------------- | --------------------- | ------------------------ | ---------------------------- |
| Rain (rain.xyz)    | Full-stack issuer    | Visa            | USDC, USDT, USDB      | Sim (via parceiro local) | BIN Sponsor + on-ramp fiat   |
| Gnosis Pay         | Self-custodial card  | Visa            | EURe, USDC            | Em expansão              | Smart contract wallet → Visa |
| Reap               | Card-as-a-Service    | Visa/Mastercard | Multi-stablecoin      | API disponível           | White-label B2B              |
| Baanx              | Card platform        | Visa/Mastercard | USDT, USDC, BTC       | Verificar                | Embeddable card SDK          |
| Transfero (Brazil) | BRL on/off ramp      | Mastercard      | USDT→BRL              | Sim (local)              | Licença BC + câmbio crypto   |
| BS2 Bank           | Banco parceiro local | Visa/Mastercard | BRL (fiat)            | Sim (completo)           | Subadquirente + BIN emissor  |

ESTRATÉGIA RECOMENDADA: Parceria primária com Rain ou Reap para infraestrutura de stablecoin-to-card no nível SPE Exchange + Transfero ou BS2 como parceiro local de câmbio e emissão BRL. Esta estrutura dual separa a camada crypto (offshore) da camada fiat (onshore), mantendo a SPE Exchange como ponto de controle.

**4. NÚCLEO TECNOLÓGICO — MACRO HASH & AGENTIC AI**

O MACRO HASH é o sistema nervoso central da plataforma. Cada operação — do crédito de um único centavo ao portfólio agregado — possui uma identidade rastreável no ledger da SPE Exchange. O motor AGENTIC AI distribui créditos, executa repagamentos e atualiza os estados dos blocos em tempo real.

**4.1 Hierarquia de Hashes**

<table>
<tbody>
<tr class="odd">
<td><p><strong>ESTRUTURA HIERÁRQUICA DO LEDGER</strong></p>
<p>PLATFORM HASH → Hash global de toda a operação da plataforma</p>
<p>└── INVESTOR HASH → Hash único por Aplicante (portfólio agregado)</p>
<p>└── PORTFOLIO HASH → Hash por carteira/composição escolhida</p>
<p>└── MICRO HASH → Hash de cada microcrédito em cada Usuário</p>
<p>└── BLOCK STATE → DEPLOYED | ACTIVE | IDLE | REPAID | DEFAULT | RENEGOTIATED</p></td>
</tr>
</tbody>
</table>

**4.2 Motor AGENTIC AI — Distribuição de Blocos**

No momento em que o Usuário realiza uma compra com o cartão, o Motor AGENTIC AI executa os seguintes passos em tempo real (latência alvo \< 200ms):

  - Identifica o bloco de microcrédito disponível de maior prioridade na carteira do Usuário (FIFO por data de alocação)

  - Debita o valor da transação do(s) bloco(s) correspondente(s)

  - Atualiza o estado do bloco para ACTIVE\_USE no hash do Aplicante correspondente

  - Gera notificação push ao Aplicante mostrando utilização percentual do portfólio

  - Registra o MCC da transação para análise de vertical e scoring de comportamento

  - Alimenta o dashboard 360° do BOARD com o evento em tempo real

**4.3 Dashboard do Aplicante — Métricas e Visualizações**

O painel do Aplicante é inspirado em dashboards de cripto-ativos e plataformas de investimento sofisticadas (Maple Finance, Nexo, Trading View). As métricas disponíveis são:

| **Módulo**        | **Métricas Exibidas**                                                                                           | **Granularidade** |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | ----------------- |
| Visão Geral       | Capital total aplicado | Capital em uso | Capital ocioso | Rendimento acumulado | Projeção de retorno 12/24/36m | Tempo real        |
| Por Portfólio     | Hash do portfólio | % por vertical | \# usuários ativos | Taxa de uso média | Inadimplência %                   | Diário            |
| Por Micro-Bloco   | Hash do bloco | Usuário (ID anônimo) | Estado atual | Histórico de uso | Dias até vencimento                    | Por transação     |
| Gerente de Contas | Nome e contato do Gerente responsável | Carteira sob gestão | NPS do gerente | Solicitação de reunião           | Ao vivo           |
| Forecast          | Simulador de reinvestimento | Curva de rendimento composto | Stress test de inadimplência                       | Sob demanda       |
| Relatórios        | Extrato PDF/Excel | Informe de rendimentos | DARF automático | Relatório FATCA (para estrangeiros)              | Mensal/Anual      |

**5. ESTRUTURA COMERCIAL E EQUIPE DE CAMPO**

A rede de Executivos de Contas é o diferencial humano da plataforma frente a modelos puramente digitais. Eles são responsáveis por qualificação de Usuários, credenciamento de merchants e expansão da base territorial.

**5.1 Hierarquia Comercial**

<table>
<tbody>
<tr class="odd">
<td><p><strong>ESTRUTURA ORGANIZACIONAL DE CAMPO</strong></p>
<p>CEO / Diretoria Executiva Nacional</p>
<p>└── Diretor de Área (responsável por 5–8 Gerentes de Área)</p>
<p>└── Gerente de Área (responsável por 10–15 Executivos Sênior)</p>
<p>└── Executivo Sênior (responsável por 500–800 Usuários + 1–2 Executivos Jr.)</p>
<p>└── Executivo Júnior (suporte ao Sênior, 200–300 Usuários)</p>
<p>└── Assistente Executivo (1 para cada 500 Usuários na base)</p></td>
</tr>
</tbody>
</table>

**5.2 Tabela de Remuneração — Executivos e Assistentes**

O modelo de remuneração combina salário-base competitivo com variável atrelado ao volume de crédito ativo na base de responsabilidade. Parâmetro: benchmarks bancários (Bradesco, Itaú, Nubank) + fintechs de crédito (Creditas, Biva, C6 Bank).

| **Posição**      | **Salário Base** | **Comissão MDR (3%)**           | **Bônus Adimpl. 95%+** | **Total Estimado/Mês** | **CLT/PJ** |
| ---------------- | ---------------- | ------------------------------- | ---------------------- | ---------------------- | ---------- |
| Assistente Exec. | R$ 2.200         | 0,05% do volume base (500 usr)  | R$ 300                 | R$ 2.800–R$ 3.500      | CLT        |
| Executivo Júnior | R$ 3.500         | 0,10% do volume base            | R$ 600                 | R$ 4.500–R$ 6.000      | CLT/PJ     |
| Executivo Sênior | R$ 5.500         | 0,15% do volume base            | R$ 1.200               | R$ 7.500–R$ 12.000     | PJ         |
| Gerente de Área  | R$ 9.000         | 0,05% do volume total equipe    | R$ 2.000               | R$ 12.000–R$ 18.000    | PJ         |
| Diretor de Área  | R$ 15.000        | 0,03% do volume total diretoria | R$ 4.000               | R$ 22.000–R$ 35.000    | PJ         |
| Diretor Nacional | R$ 25.000        | 0,01% volume nacional           | R$ 8.000               | R$ 38.000–R$ 55.000    | CLT        |

*NOTA: A comissão MDR é calculada sobre o volume de transações dos cartões da base do profissional no período (mensal). O bônus de adimplência é pago quando a taxa de inadimplência da base do profissional fica ≤ 5% no mês.*

**6. MODELO FINANCEIRO E TRIBUTAÇÃO**

**6.1 Receitas da Plataforma**

| **Fonte de Receita**  | **Mecanismo**                                    | **Taxa** | **Estimativa Mensal (Ano 2)**                   |
| --------------------- | ------------------------------------------------ | -------- | ----------------------------------------------- |
| MDR Merchant          | 3% sobre cada transação no cartão do Usuário     | 3,0%     | R$ 2,7M (base 90k cartões × R$ 1.000 uso médio) |
| Setup Fee Aplicante   | Taxa única de onboarding por portfólio criado    | 0,5%     | R$ 250k (500 Aplicantes × R$ 50k médio)         |
| Spread de Câmbio      | USDT→BRL: spread de 0,5% na conversão            | 0,5%     | R$ 450k (R$ 90M em conversões)                  |
| Taxa de Inadimplência | Cobrança sobre débitos recuperados (success fee) | 15%      | R$ 180k (sobre recuperação estimada)            |
| Fee Contábil ODOO     | Licença SaaS do módulo contábil por Aplicante    | Fixo     | R$ 150k (R$ 300/Aplicante/mês)                  |

**6.2 Estrutura de Custos Operacionais (Ano 2)**

| **Centro de Custo**    | **Descrição**                                       | **Estimativa Mensal** |
| ---------------------- | --------------------------------------------------- | --------------------- |
| Pessoal de Campo       | 500 Executivos/Assistentes (média R$ 5k/mês)        | R$ 2.500.000          |
| Pessoal HQ             | TI, Jurídico, Financeiro, RH, Compliance, Marketing | R$ 1.200.000          |
| Infraestrutura Tech    | Cloud (AWS/GCP), Blockchain nodes, APIs bancárias   | R$ 350.000            |
| Marketing & Aquisição  | CAC Usuários + CAC Aplicantes + merchant onboarding | R$ 600.000            |
| SPE Exchange Ops       | Custos operacionais Dubai + compliance FATF         | R$ 280.000            |
| Fundo de Reserva (FRL) | 5% do capital sob gestão aportado mensalmente       | R$ 750.000            |
| ODOO + Sistemas        | Licenças, customização, suporte, integrações        | R$ 120.000            |
| Jurídico & Regulatório | Assessoria legal Brasil + Dubai + auditoria         | R$ 200.000            |
| TOTAL CUSTOS           |                                                     | R$ 6.000.000          |

**6.3 P\&L Simplificado — Cenários de Escala**

| **Cenário**         | **Cartões Ativos** | **Capital sob Gestão** | **Receita Bruta/mês** | **Custos/mês** | **EBITDA/mês** | **Margem** |
| ------------------- | ------------------ | ---------------------- | --------------------- | -------------- | -------------- | ---------- |
| Conservador (Ano 1) | 30.000             | R$ 45M                 | R$ 1,3M               | R$ 3,5M        | – R$ 2,2M      | Negativo   |
| Base (Ano 2)        | 90.000             | R$ 135M                | R$ 3,7M               | R$ 6,0M        | – R$ 2,3M      | Negativo   |
| Otimista (Ano 2)    | 120.000            | R$ 180M                | R$ 5,1M               | R$ 6,8M        | – R$ 1,7M      | Negativo   |
| Break-even (Mês 18) | 200.000            | R$ 300M                | R$ 8,5M               | R$ 8,0M        | \+ R$ 0,5M     | 6%         |
| Escala (Ano 3)      | 500.000            | R$ 750M                | R$ 21,0M              | R$ 14M         | \+ R$ 7,0M     | 33%        |

**6.4 Tributação — Cenário para Pitch**

A estrutura tributária é um diferencial estratégico do Documento GREY. A operação é arquitetada para minimizar carga fiscal através da separação entre entidade offshore (SPE Exchange) e operação local (entidade operacional brasileira):

<table>
<tbody>
<tr class="odd">
<td><p><strong>ESTRUTURA TRIBUTÁRIA GREY — ENTIDADE OFFSHORE (SPE Exchange Dubai/Cayman)</strong></p>
<p>▸ IR Corporativo: 0% (Dubai Free Zone / Cayman Islands — sem IR)</p>
<p>▸ IOF sobre câmbio: estrutura de câmbio contratual minimiza IOF (0,38% em operações de curto prazo)</p>
<p>▸ Imposto sobre lucros remetidos: Cayman = 0% | Dubai DIFC = 0%</p>
<p>▸ Ganhos do Aplicante (estrangeiro): tributação no país de residência do Aplicante</p>
<p>▸ Ganhos do Aplicante (brasileiro): Carnê-leão mensal sobre rendimentos estrangeiros (IR tabela progressiva)</p>
<p>▸ Regime de transparência fiscal: relatórios FATCA/CRS para investidores americanos/europeus</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>ESTRUTURA TRIBUTÁRIA GREY — ENTIDADE OPERACIONAL BRASIL</strong></p>
<p>▸ Regime tributário recomendado: Lucro Real (permite dedução de todas as despesas operacionais)</p>
<p>▸ PIS/COFINS sobre receitas financeiras: 0,65% + 4% = 4,65% (Decreto 8.426/2015)</p>
<p>▸ ISS sobre serviços de gestão/consultoria: 2% a 5% (variável por município)</p>
<p>▸ CSLL: 15% sobre lucro líquido (instituição financeira: alíquota majorada)</p>
<p>▸ IR sobre JUROS sobre Capital Próprio: estratégia de JCP reduz base tributável em até 30%</p>
<p>▸ Contribuição Social: 9% sobre lucro ajustado</p>
<p>▸ CPMF/IOF interno: 0,0082% ao dia sobre saldo médio diário de operações financeiras</p>
<p>▸ Tese jurídica: receitas geradas no exterior pela SPE Exchange não configuram fato gerador no Brasil</p></td>
</tr>
</tbody>
</table>

**ALERTA REGULATÓRIO: Embora a estrutura GREY seja projetada para operar fora do perímetro direto do Banco Central, qualquer operação de captação de recursos junto ao público brasileiro — mesmo via stablecoins — pode ser enquadrada pelo BC como 'operação de câmbio não autorizada' ou 'atividade privativa de instituição financeira' (Lei 4.595/64, Art. 17). Recomenda-se fortemente a contratação de assessoria jurídica especializada em crypto-law brasileiro antes do go-live.**

**7. ESTRUTURA ORGANIZACIONAL INTERNA DA EMPRESA**

**7.1 Departamentos e Setores**

| **Setor/Departamento**      | **Função Principal**                                                   | **Headcount Est. (Ano 1)** |
| --------------------------- | ---------------------------------------------------------------------- | -------------------------- |
| Presidência Executiva / CEO | Visão estratégica, relação com Shareholders, Sponsors e reguladores    | 1                          |
| COO — Operações             | Gestão da operação diária, processos, qualidade, SLA                   | 1 + equipe 5               |
| CFO — Financeiro            | Tesouraria, contabilidade ODOO, câmbio, relatórios FATCA/CRS           | 1 + equipe 4               |
| CTO — Tecnologia            | Plataforma, MACRO HASH, APIs, segurança, AGENTIC AI                    | 1 + equipe 10              |
| CCROO — Compliance          | AML/KYC, FATF, regulação Dubai, risco legal Brasil                     | 1 + equipe 4               |
| CMO — Marketing             | Aquisição Aplicantes + Usuários, branding, growth hacking              | 1 + equipe 5               |
| Diretoria Comercial         | Diretores de Área, gestão da rede de executivos                        | 3 Diretores                |
| Crédito & Score             | Motor de scoring, análise de risco, política de crédito, verticais     | Equipe 6                   |
| Produto & UX                | Design das plataformas (Aplicante, Usuário, 360°), roadmap             | Equipe 5                   |
| Jurídico                    | Contratos, regulação, litígios, propriedade intelectual                | Equipe 3                   |
| RH & Cultura                | Recrutamento executivos de campo, treinamento, benefícios              | Equipe 4                   |
| Operações de Campo          | Rede de Executivos Sênior/Júnior e Assistentes                         | 200–500                    |
| Cobrança & Recuperação      | Negociação de débitos, renegociação de contratos, jurídico de cobrança | Equipe 8                   |
| Merchant Success            | Credenciamento e retenção de merchants, parcerias, descontos           | Equipe 6                   |
| Data Science & BI           | Análise de dados, relatórios 360°, forecast, modelos preditivos        | Equipe 5                   |
| SAC / Customer Experience   | Suporte a Usuários e Aplicantes, canal executivos-Usuários             | Equipe 15                  |
| SPE Exchange Ops (Dubai)    | Gestão operacional da exchange, custódia, liquidação                   | Equipe 4                   |
| Auditoria Interna           | Conformidade com ODOO, relatórios regulatórios, controles internos     | Equipe 3                   |

**8. INOVAÇÕES INCREMENTAIS — ELEMENTOS NÃO EXPLORADOS ANTERIORMENTE**

Com base na literatura acadêmica (Iyer et al., Herzenstein, Lin et al., Berger & Gleisner) e nos benchmarks globais analisados, identificamos os seguintes elementos de inovação que elevam o NEXUS acima dos modelos existentes:

**8.1 Sistema de Vouching Social (Lin et al., 2012)**

Usuários podem endossar outros Usuários da plataforma. Cada endosso de um Usuário com histórico de adimplência superior a 18 meses eleva em 8 pontos o score do endossado. Isso reaplica a descoberta acadêmica de que redes sociais verificáveis reduzem default em até 30%.

**8.2 NFT de Portfólio para Transferência de Cotas**

Cada portfólio do Aplicante pode ser 'tokenizado' como um NFT no ledger da SPE Exchange, permitindo transferência de cotas entre Aplicantes sem liquidação antecipada. Cria um mercado secundário interno de portfólios, aumentando a liquidez do produto para investidores.

**8.3 Score Comportamental Dinâmico (Além do Bureau)**

O motor de IA analisa padrões de uso do cartão em tempo real: consistência de uso mensal, diversidade de MCCs, sazonalidade de gastos e correlação com indicadores macroeconômicos regionais. O score é atualizado mensalmente, permitindo upgrades e downgrades dinâmicos de limite.

**8.4 Programa de Fidelidade do Merchant — NEXUS REWARDS**

Merchants credenciados podem oferecer descontos exclusivos (1% a 5%) para portadores do cartão NEXUS. O desconto é financiado pelo próprio MDR, sem custo adicional ao merchant. Cria lock-in do Usuário e aumenta o volume de transações por cartão.

**8.5 Modo 'Autopiloto' para o Aplicante (Inspirado em Bondora Go\&Grow)**

Aplicante pode escolher o modo Autopiloto, onde a plataforma compõe automaticamente o portfólio ótimo baseado no perfil de risco declarado e reinveste os juros automaticamente. Ideal para Aplicantes que querem exposição ao produto sem curadoria ativa.

**8.6 Integração Open Finance (Pix + Open Banking)**

Integração com o ecossistema de Open Finance do Banco Central (mesmo no modelo GREY, via entidade operacional local) permite leitura de extrato bancário do Usuário para scoring enriquecido, pagamento de fatura via Pix e consulta a histórico de contas em outras instituições.

**8.7 Seguro Prestamista Embutido**

Cada cartão NEXUS pode incluir um seguro prestamista (morte, invalidez, desemprego involuntário) com prêmio de 0,3% a 0,8% ao mês embutido na fatura. Além de proteger o Aplicante, cria receita adicional via corretagem de seguros e reduz o risco de default por eventos não intencionais.

**9. ROADMAP DE IMPLEMENTAÇÃO**

| **Fase**          | **Período** | **Entregas Principais**                                                                                                       | **KPI de Validação**                            |
| ----------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Fase 0 — Fundação | Meses 1–3   | Constituição SPE Exchange Dubai | Contratação CTO/CCROO/CFO | Definição parceiro BIN Sponsor | Contrato Transfero/BS2         | SPE Exchange licenciada | Time C-level completo |
| Fase 1 — MVP      | Meses 4–8   | Plataforma v1.0 (Aplicante + Usuário) | MACRO HASH v1 | 10 Executivos de Área piloto | 500 Usuários beta | 20 Aplicantes seed | 500 cartões ativos | R$ 1M capital sob gestão   |
| Fase 2 — Go-Live  | Meses 9–15  | Plataforma completa com 360° Board | Rede de 50 Executivos | Merchant network 200 locais | Campanha de aquisição              | 30.000 cartões | R$ 45M AUM | MDR positivo      |
| Fase 3 — Escala   | Meses 16–24 | Expansão nacional (todas as capitais) | 200 Executivos | NFT portfólios | Vouching Social | NEXUS Rewards                     | 90.000 cartões | Break-even atingido            |
| Fase 4 — Expansão | Meses 25–36 | Internacionalização (México, Colômbia) | Série B | 500.000 cartões | Parceria com exchange tier-1                             | R$ 750M AUM | EBITDA 30%+ | IPO/M\&A prep       |

**10. REFERÊNCIAS E BASE ACADÊMICA**

Este whitepaper baseia-se nas seguintes fontes acadêmicas e de mercado:

\[1\] Herzenstein, M., Sonenshein, S., & Dholakia, U. M. (2011). Tell me a good story and I may lend you money: The role of narratives in peer-to-peer lending decisions.

\[2\] Iyer, R., Khwaja, A. I., Luttmer, E. F., & Shue, K. (2009). Screening in new credit markets: Can individual lenders infer borrower creditworthiness in peer-to-peer lending? (NBER Working Paper 15242).

\[3\] Pope, D. G., & Sydnor, J. R. (2011). What's in a Picture? Evidence of Discrimination from Prosper.com. Journal of Human Resources.

\[4\] Ravina, E. (2007). Beauty, Personal Characteristics, and Trust in Credit Markets. Columbia Business School.

\[5\] Lin, M., Prabhala, N. R., & Viswanathan, S. (2012). Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending.

\[6\] Berger, S. C., & Gleisner, F. (2009). Emergence of financial intermediaries in electronic markets: The case of online P2P lending. BuR — Business Research.

\[7\] Frerichs, A., & Schumann, M. (2008). Peer-to-Peer Lending: Opportunities and Risks.

\[8\] Goldfinch Protocol (2024). Default Report: Lend East. Goldfinch Foundation.

\[9\] Maple Finance (2024). Annual Report 2024 — Institutional DeFi Lending.

\[10\] DFSA (2024). Regulatory Framework for Digital Assets — Dubai Financial Services Authority.

\[11\] CMN Resolution 5050/2022 — Revogação e consolidação das normas SCD/SEP (Banco Central do Brasil).

\[12\] FATF (2023). Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers.

\[13\] Visa (2024). Empowering the future of payments with stablecoins. Visa Corporate.

\[14\] Rain.xyz (2024). Stablecoin-Powered Cards & Payments Infrastructure — Technical Documentation.

*NEXUS GREY v1.0 | Abril 2026 | Documento Confidencial | Todos os direitos reservados*
