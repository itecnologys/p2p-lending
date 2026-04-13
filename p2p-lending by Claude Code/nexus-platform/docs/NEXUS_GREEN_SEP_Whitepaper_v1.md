---
title: "NEXUS — NEXUS_GREEN_SEP_Whitepaper_v1"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>[ WHITEPAPER CONFIDENCIAL — DOCUMENTO GREEN-SEP v1.0 — ABRIL 2026 ]</strong></p>
<p><strong>PROJECTO NEXUS GREEN-SEP</strong></p>
<p><strong>Plataforma P2P via Sociedade de Emprestimo entre Pessoas</strong></p>
<p><em>Modelo P2P Regulado · Banco Central do Brasil · CMN 5050/2022 · Captacao P2P Direta</em></p></td>
</tr>
</tbody>
</table>

*Este documento apresenta a estrutura do Projeto NEXUS operando sob o modelo de Sociedade de Emprestimo entre Pessoas (SEP), modalidade regulada pelo Banco Central do Brasil. Destinado a investidores, Conselho de Administracao, assessores juridicos e reguladores.*

**SUMARIO EXECUTIVO**

O Documento GREEN-SEP apresenta a arquitetura do Projeto NEXUS operando como Sociedade de Emprestimo entre Pessoas (SEP). Esta e a modalidade que mais se aproxima do modelo original do LendingClub e do Prosper — a SEP atua como intermediaria eletronica que CONECTA diretamente Aplicantes (investidores/credores) a Usuarios (tomadores), sem usar capital proprio para realizar os emprestimos. O Aplicante e o credor efetivo do contrato; a SEP e a plataforma de matching, scoring e gestao do relacionamento. Este modelo e o que melhor replica a essencia P2P global dentro do arcabouco regulatorio brasileiro.

<table>
<tbody>
<tr class="odd">
<td><p><strong>DIFERENCIAIS ESTRATEGICOS DO MODELO SEP vs SCD</strong></p>
<p>✔ P2P Autentico: Aplicante e o credor legal — total alinhamento com benchmarks globais (LendingClub, Mintos, Prosper)</p>
<p>✔ Sem uso de capital proprio para credito: menor exigencia de capital inicial na SCD</p>
<p>✔ Base de Aplicantes como ativo: comunidade de investidores e o moat principal do negocio</p>
<p>✔ Diversificacao natural de risco: cada contrato e atomizado entre multiplos Aplicantes</p>
<p>✔ Transparencia para o Aplicante: ele ve sua carteira de contratos, nao uma cota de fundo</p>
<p>✔ Modelo escalavel via crescimento da base de Aplicantes (sem limite de balanco proprio)</p>
<p>✔ Alinhamento com Open Finance: Aplicante pode ser PF qualificado ou nao-qualificado</p>
<p>✔ Retorno mais alto ao Aplicante vs FIDC da SCD (6% a.m. no cartao do Usuario)</p></td>
</tr>
</tbody>
</table>

**1. REGULACAO — SOCIEDADE DE EMPRESTIMO ENTRE PESSOAS (SEP)**

A SEP foi criada pela Resolucao CMN 4.656/2018 e consolidada na CMN 5.050/2022, constituindo a primeira regulacao especifica de P2P lending no Brasil. E a modalidade que permite a captacao de recursos diretamente de pessoas fisicas e juridicas (Aplicantes) para emprestimo a outras pessoas fisicas e juridicas (Usuarios), tudo intermediado pela plataforma eletronica da SEP.

**1.1 Caracteristicas Fundamentais da SEP**

| **Caracteristica**    | **Regra SEP**                                             | **Impacto no NEXUS**                                                  |
| --------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| Capital Minimo        | R$ 1.000.000 (PL permanente)                              | Aporte inicial de R$ 1M pelos Shareholders (menor que SCD em pratica) |
| Fonte de Recursos     | CAPTACAO de terceiros (Aplicantes) para emprestimo        | Aplicantes investem diretamente na plataforma — modelo P2P autentico  |
| Modelo de Credito     | Contrato entre Aplicante e Usuario; SEP e intermediaria   | SEP nao e parte do contrato de credito — apenas gestora               |
| Operacoes Permitidas  | Emprestimos entre PF e PJ exclusivamente via plataforma   | Todos os produtos NEXUS (cartao rotativo) sao compatíveis             |
| Limite por Credor PF  | Sem limite expresso na norma atual                        | Aplicante PF pode investir qualquer valor na plataforma               |
| Limite por Devedor PF | Sem limite expresso (plataforma define politica interna)  | Limite NEXUS: R$ 500 a R$ 2.500 por cartao de Usuario                 |
| Emissao de Cartao     | Permitida via parceria com emissor credenciado            | Parceria com BIN Sponsor (Dock, Conductor, Matera, BS2)               |
| Cessao de Credito     | Permitida entre SEPs e para IFs                           | Possibilidade de securitizacao futura dos contratos                   |
| Supervisao            | Banco Central do Brasil                                   | Conformidade com CMN 5.050/2022 e atualizacoes                        |
| Reporte               | SCR mensal ao Bacen                                       | Toda a carteira de contratos reportada mensalmente                    |
| Diversificacao        | SEP deve implementar politica de diversificacao do credor | Regra NEXUS: max 25% por vertical, fracionamento por 1.800 Usuarios   |

**1.2 Diferenca Fundamental: SEP vs SCD na Pratica**

<table>
<tbody>
<tr class="odd">
<td><p><strong>SEP: O APLICANTE E O CREDOR LEGAL</strong></p>
<p>Na SEP: Aplicante → [assina contrato de emprestimo] → Usuario</p>
<p>SEP atua como: gestora, cobradora, intermediaria eletronica</p>
<p>SEP nao e parte do contrato de credito</p>
<p>Aplicante assume o risco de credito (nao a SEP)</p>
<p>Na SCD: SCD → [assina contrato de emprestimo] → Usuario</p>
<p>SCD e a credora; Aplicante investe na SCD (nao no contrato direto)</p>
<p>SCD assume o risco de credito</p>
<p>Aplicante tem exposicao ao risco da SCD como instituicao</p></td>
</tr>
</tbody>
</table>

**IMPLICACAO PARA O PITCH: A SEP e o modelo mais transparente e mais proximo do que investidores sofisticados esperam de uma plataforma P2P autentica. O Aplicante ve exatamente quais contratos possui, qual e o hash de cada microemprestimo e qual e o retorno de cada real investido — sem a camada de um fundo no meio.**

**2. MODELO DE NEGOCIO NEXUS-SEP**

**2.1 Fluxo Operacional SEP**

<table>
<tbody>
<tr class="odd">
<td><p><strong>FLUXO COMPLETO — NEXUS SEP (100% BRL)</strong></p>
<p>PASSO 1: Aplicante realiza KYC/AML na plataforma e deposita capital (Pix/TED para conta SEP)</p>
<p>PASSO 2: Aplicante escolhe perfil de portfólio (mix de verticais) no dashboard de investimentos</p>
<p>PASSO 3: Motor de matching atribui o capital do Aplicante a contratos de Usuario elegíveis</p>
<p>PASSO 4: SEP formaliza N contratos de emprestimo (cada micro-contrato: Aplicante ← → Usuario)</p>
<p>PASSO 5: Capital e transferido para o cartao pre-pago do Usuario (via BIN Sponsor parceiro)</p>
<p>PASSO 6: Usuario usa o cartao nos merchants credenciados — SEP recebe MDR de 3%</p>
<p>PASSO 7: No vencimento, Usuario paga fatura + 6% de taxa — pagamento via Pix</p>
<p>PASSO 8: SEP distribui o capital repago + rendimento ao Aplicante (proporcional a cada contrato)</p>
<p>PASSO 9: Aplicante opta por reinvestimento automatico ou resgate para conta bancaria</p></td>
</tr>
</tbody>
</table>

**2.2 Contrato de Emprestimo entre Aplicante e Usuario**

Cada microcontrato na plataforma NEXUS-SEP e um contrato de emprestimo pessoal formalmente constituido, com os seguintes elementos essenciais:

| **Elemento Contratual** | **Especificacao NEXUS-SEP**                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| Credor                  | Aplicante (identificado por CPF/CNPJ, representado pela SEP via procuracao)               |
| Devedor                 | Usuario (identificado por CPF, validado pelo Executivo de Contas)                         |
| Valor                   | Microparcela do Aplicante no limite do cartao do Usuario (ex: R$ 40 de R$ 10k investidos) |
| Taxa de Juros           | 6% ao mes sobre o saldo utilizado do cartao (equivalente a \~101% a.a.)                   |
| Prazo                   | Contrato de credito rotativo — renovavel mensalmente enquanto Usuario pagar em dia        |
| Garantias               | Carta de fianca digital (vouching) + seguro prestamista + fundo de reserva da SEP         |
| Forma de Pagamento      | Fatura mensal via Pix, TED ou debito em conta cadastrada                                  |
| Mecanismo de Execucao   | Em caso de default: cessao do contrato para empresa de cobranca parceira                  |
| Registro                | Registro eletronico na plataforma SEP + arquivo digital MACRO HASH                        |
| Representacao do Credor | SEP age como mandataria do Aplicante via procuracao irrevogavel no contrato               |

**2.3 Verticals e Score — Identico ao Modelo GREY**

A estrutura de verticais de consumo, scores de risco e retornos ao Aplicante e identica ao descrito no Documento GREY (Secao 2.2), com uma diferenca operacional: no modelo SEP, o Aplicante ESCOLHE as verticais e ve os contratos individuais. Nao ha camada de FIDC ou fundo entre ele e os contratos.

**3. ANALISE COMPARATIVA — VANTAGENS E DESVANTAGENS DA SEP**

**3.1 Vantagens e Desvantagens SEP vs SCD vs GREY**

| **Dimensao**               | **SEP**                        | **SCD**                      | **GREY (Stablecoin)**         |
| -------------------------- | ------------------------------ | ---------------------------- | ----------------------------- |
| Modelo P2P Autentico       | ✔ Sim (Aplicante = credor)     | ✘ Nao (SCD = credora)        | ✔ Sim (smart contract)        |
| Regulacao Bacen            | ✔ Licenca plena IF             | ✔ Licenca plena IF           | ✘ Fora do BC Brasil           |
| Credibilidade Inst.        | ★★★★★ Maxima                   | ★★★★★ Maxima                 | ★★★☆☆ Media (offshore)        |
| Transparencia ao Aplicante | ★★★★★ Total (vê contratos)     | ★★★☆☆ Parcial (cotas FIDC)   | ★★★★☆ Hash/ledger             |
| Capital Inicial Necessario | R$ 1M (apenas PL minimo)       | R$ 1M + funding carteira     | USD 500k (DIFC) + operacional |
| Risco de Credito           | Aplicante assume               | SCD assume                   | Aplicante assume              |
| Escalabilidade             | Alta (base de Aplicantes)      | Alta (via FIDC)              | Alta (crypto pool)            |
| Tributacao Aplicante PF    | IR 15% a 22,5% (rend. capital) | IR sobre rendimentos do FIDC | Carnê-leão (rendimentos ext.) |
| Tributacao da Empresa      | IR 25% + CSLL 20% (IF)         | IR 25% + CSLL 20% (IF)       | 0% (Dubai)                    |
| Acesso a Bancarios         | Total                          | Total                        | Via parceiro local            |
| Pitch para PF Brasileiro   | Excelente (produto intuitivo)  | Bom (FIDC e mais complexo)   | Bom (crypto nao e universal)  |
| Reporte ao Bacen           | Sim (SCR mensal)               | Sim (SCR mensal)             | Nao                           |

**3.2 Riscos Especificos da SEP**

  - RISCO DE LIQUIDEZ DO APLICANTE: Diferente de um fundo com mercado secundario, o Aplicante na SEP pode ter dificuldade de 'sair' antes do vencimento dos contratos. Mitigacao: SEP cria mercado secundario interno onde contratos podem ser cedidos a outros Aplicantes.

  - RISCO DE CONCENTRACAO: Se poucos Aplicantes respondem por grande parcela do capital, a saida de um pode desestabilizar a operacao. Mitigacao: limite de 20% do total da carteira por Aplicante individual.

  - RISCO REPUTACIONAL: Default de Usuarios visivel para Aplicantes (que sao os credores diretos) pode gerar reacao negativa intensa. Mitigacao: Fundo de Reserva de Liquidez (FRL) que absorve defaults antes de impactar o Aplicante.

  - RISCO DE COMPLIANCE: Com N contratos entre pessoas fisicas, o Bacen pode questionar se cada micro-contrato respeita as normas de credito ao consumidor (CDC). Mitigacao: assessoria juridica especializada e padronizacao contratual aprovada pelo Bacen.

  - RISCO OPERACIONAL: Gestao de milhares de microcontratos exige plataforma tecnologica robusta. Mitigacao: MACRO HASH e sistema AGENTIC AI automatizam inteiramente o ciclo de vida dos contratos.

**4. TRIBUTACAO E PLANEJAMENTO FISCAL — SEP**

A tributacao da SEP tem duas dimensoes: a da empresa (SEP como instituicao financeira) e a do Aplicante (pessoa fisica ou juridica investindo na plataforma).

**4.1 Tributacao da SEP (Empresa)**

| **Tributo** | **Base de Calculo**         | **Aliquota** | **Observacao**                            |
| ----------- | --------------------------- | ------------ | ----------------------------------------- |
| IRPJ        | Lucro Real                  | 25%          | Mesma aliquota da SCD — SEP e IF          |
| CSLL        | Lucro ajustado              | 20%          | Aliquota de IF (vs 9% empresas comuns)    |
| PIS         | Receitas operacionais       | 0,65%        | Regime cumulativo para IFs                |
| COFINS      | Receitas operacionais       | 4,00%        | Regime cumulativo para IFs                |
| ISS         | Receita de intermediacao    | 2%–5%        | Sobre taxa de servico cobrada da operacao |
| IOF/Credito | Saldo devedor dos contratos | 0,0082%/dia  | Incide sobre os contratos dos Usuarios    |
| IOF/Cambio  | N/A                         | N/A          | SEP opera em BRL — sem IOF cambio         |

**4.2 Tributacao do Aplicante (Investidor na SEP)**

Este e o ponto de maior diferencial do modelo SEP frente ao FIDC da SCD: o Aplicante recebe RENDIMENTOS DE EMPRESTIMO, tributados como renda de capital:

| **Perfil do Aplicante**      | **Natureza do Rendimento**        | **Tributacao**                                     | **Retencao na Fonte**                              |
| ---------------------------- | --------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| Pessoa Fisica                | Rendimentos de emprestimo pessoal | IR tabela progressiva (7,5% a 27,5%) OU carnê-leão | SEP retém 1,5% na fonte + Aplicante completa no IR |
| Pessoa Juridica              | Receita financeira                | IRPJ + CSLL sobre lucro (regime da PJ)             | Conforme regime tributario da PJ                   |
| Fundo de Investimento        | Conforme regulamento do fundo     | IR semestral + IOF (come-cotas se aplicavel)       | Administrador do fundo                             |
| Investidor Estrangeiro       | Rendimento de fonte brasileira    | 15% IR (residente em pais sem paraiso fiscal)      | SEP retém 15% na fonte                             |
| Investidor de Paraiso Fiscal | Rendimento de fonte brasileira    | 25% IR (pais com tributacao favorecida)            | SEP retém 25% na fonte                             |

**4.3 Estrategias de Otimizacao Tributaria — SEP**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PLANEJAMENTO TRIBUTARIO — SEP NEXUS</strong></p>
<p>EMPRESA (SEP):</p>
<p>▸ JCP: Distribuicao de Juros sobre Capital Proprio reduz base do IRPJ/CSLL em ate 30%</p>
<p>▸ Provisao para Devedores Duvidosos (PDD): dedutivel integralmente do IR</p>
<p>▸ Holding: SEP como subsidiaria de holding — dividendos da SEP para a holding sao isentos de IR</p>
<p>▸ Lei do Bem: Despesas com P&amp;D (MACRO HASH, IA, Open Finance) dedutivel em 160% do valor real</p>
<p>APLICANTE (Otimizacao sugerida pela plataforma como valor agregado):</p>
<p>▸ PF: Declarar no Simplificado pode ser mais vantajoso ate R$ 40k/ano de rendimento</p>
<p>▸ PF sofisticada: Estruturar via holding PJ (LTDA ou S.A. fechada) — tributacao pelo Lucro Presumido</p>
<p>▸ PGBL/VGBL: Rendimentos da SEP podem ser declarados no IR para compensar com previdencia</p>
<p>▸ Prejuizos compensaveis: defaults na SEP sao dedutiveis do imposto sobre rendimentos positivos</p></td>
</tr>
</tbody>
</table>

**4.4 Simulacao de Carga Tributaria — SEP para Pitch**

Simulacao para Aplicante Pessoa Fisica com R$ 100k investidos e retorno de 4% a.m.:

| **Item**                               | **Cenario Basico** | **Cenario com Holding PJ**         |
| -------------------------------------- | ------------------ | ---------------------------------- |
| Capital investido                      | R$ 100.000         | R$ 100.000                         |
| Retorno bruto mensal (4%)              | R$ 4.000           | R$ 4.000                           |
| Retorno bruto anual                    | R$ 48.000          | R$ 48.000                          |
| IR sobre rendimentos (27,5% tabela PF) | – R$ 13.200        | —                                  |
| IRPJ/CSLL Lucro Presumido (holding)    | —                  | – R$ 5.760 (32% margem × 25% + 9%) |
| PIS/COFINS (holding)                   | —                  | – R$ 912 (1,65% + 3%)              |
| Total de Tributos                      | R$ 13.200          | R$ 6.672                           |
| Rendimento Liquido Anual               | R$ 34.800          | R$ 41.328                          |
| Rentabilidade Liquida                  | 34,8% a.a.         | 41,3% a.a.                         |
| Reducao de Carga Tributaria            | Referencia         | 49,5% menos impostos               |

*NOTA IMPORTANTE: Esta simulacao e de carater ilustrativo para fins de pitch. O Aplicante deve consultar seu contador/advogado tributarista para validar a melhor estrutura para sua situacao especifica.*

**5. MODELO FINANCEIRO — SEP NEXUS**

**5.1 Fontes de Receita da SEP**

| **Fonte**                       | **Mecanismo**                                                | **Taxa**        | **Estimativa (Ano 2 — 80k cartoes)**  |
| ------------------------------- | ------------------------------------------------------------ | --------------- | ------------------------------------- |
| Taxa de Intermediacao (TI)      | Cobrada do Aplicante sobre rendimentos distribuidos          | 1,5% a.m.       | R$ 1,8M/mes (R$ 120M carteira × 1,5%) |
| MDR Merchant                    | 3% sobre transacoes dos Usuarios nos merchants               | 3,0%            | R$ 2,4M/mes (R$ 80M em compras)       |
| Taxa de Setup Aplicante         | Onboarding e estruturacao de portfólio                       | 0,5% do cap.    | R$ 500k (media anual)                 |
| Taxa de Gestao de Cobranca      | Sobre valores recuperados em default                         | 15% recup.      | R$ 150k/mes                           |
| Mercado Secundario de Contratos | Taxa sobre cessao de contratos entre Aplicantes              | 1% da cessao    | R$ 100k/mes                           |
| Seguro Prestamista (corretagem) | Comissao sobre premios de seguro embutidos nos cartoes       | 0,5% a.m.       | R$ 600k/mes                           |
| ODOO/Relatorios Premium         | Modulo avancado de relatorios para Aplicantes institucionais | Fixo R$ 500/mes | R$ 250k/mes                           |

**5.2 Projecao Financeira Comparada — SEP vs SCD (3 Anos)**

| **Indicador**                 | **SEP — Ano 1**             | **SCD — Ano 1** | **SEP — Ano 3** | **SCD — Ano 3** |
| ----------------------------- | --------------------------- | --------------- | --------------- | --------------- |
| Cartoes Ativos                | 25.000                      | 25.000          | 200.000         | 200.000         |
| Carteira de Credito           | R$ 37M                      | R$ 37M          | R$ 300M         | R$ 300M         |
| Receita de Intermediacao (TI) | R$ 6,7M                     | —               | R$ 54M          | —               |
| MDR Merchant                  | R$ 9M                       | R$ 9M           | R$ 72M          | R$ 72M          |
| Juros (capital proprio SCD)   | —                           | R$ 22M          | —               | R$ 180M         |
| Receita Total                 | R$ 17M                      | R$ 31M          | R$ 135M         | R$ 252M         |
| Custo Financeiro              | R$ 0 (nao usa cap. proprio) | – R$ 8M         | R$ 0            | – R$ 40M        |
| Inadimplencia                 | Risco Aplicante             | – R$ 2,6M       | Risco Aplicante | – R$ 21M        |
| Despesas Operacionais         | – R$ 16M                    | – R$ 20M        | – R$ 70M        | – R$ 85M        |
| EBITDA                        | R$ 1M                       | R$ 0,4M         | R$ 65M          | R$ 106M         |
| Lucro Liquido (apos tributos) | R$ 0,5M                     | R$ 0,2M         | R$ 35M          | R$ 58M          |
| Margem Liquida                | 2,9%                        | 0,6%            | 25,9%           | 23,0%           |

*OBSERVACAO: A SEP tem MENOR receita total que a SCD porque nao captura os juros dos contratos (que vao ao Aplicante). Porem, tem MENOR custo financeiro (sem FIDC/Debêntures). O modelo SEP e mais eficiente em capital mas menos lucrativo em receita bruta.*

**6. INOVACOES ESPECIFICAS DO MODELO SEP**

**6.1 Mercado Secundario de Contratos (Liquidity Layer)**

A SEP NEXUS introduz um mercado secundario interno onde Aplicantes podem VENDER seus contratos de emprestimo a outros Aplicantes antes do vencimento. O preco do contrato e determinado pelo estado de saude do devedor (score atual, historico de pagamentos, tempo restante de contrato). Isso resolve o principal problema de liquidez do P2P tradicional e diferencia o NEXUS de todos os players brasileiros.

  - Contratos inadimplentes sao vendidos com desconto (ex: 70% do valor de face) para Aplicantes com apetite de risco elevado

  - Contratos performando sao vendidos pelo valor de face + accrual de juros

  - Hash do contrato e transferido no ledger — rastreabilidade total da cadeia de custodia

  - Taxa da SEP no mercado secundario: 1% do valor de cessao

**6.2 Aplicante Score — Qualificacao de Investidores**

Assim como os Usuarios passam por scoring, os Aplicantes sao qualificados. A plataforma implementa o 'Aplicante Score' para evitar concentracao de risco e enquadramento AML (o Aplicante tambem pode ser um 'laranja'):

| **Tier do Aplicante** | **Capital Minimo** | **Limite de Exposicao** | **Produtos Disponiveis**                 |
| --------------------- | ------------------ | ----------------------- | ---------------------------------------- |
| Varejo (Starter)      | R$ 1.000           | R$ 50.000 total         | Autopiloto; max 3 verticais              |
| Varejo Plus           | R$ 10.000          | R$ 500.000 total        | Escolha de verticais; mercado secundario |
| Qualificado           | R$ 100.000         | Sem limite              | Todos os produtos + API acesso           |
| Institucional         | R$ 1.000.000       | Sem limite              | Portfolio customizado + relatorio FATCA  |

**6.3 API para Aplicantes Institucionais (Open Credit API)**

Aplicantes institucionais (family offices, fintechs, gestoras) podem acessar a plataforma via API para: (i) automatizar alocacao de capital; (ii) integrar o portfólio NEXUS com seus sistemas de gestao; (iii) receber dados de performance em tempo real via webhook. Esta feature posiciona o NEXUS como infraestrutura de credito para outras fintechs, nao apenas como produto para investidor final.

**6.4 NEXUS Guarantee Fund (Fundo de Reserva de Liquidez)**

Para proteger o Aplicante contra defaults nao-antecipados, a SEP NEXUS mantem um Fundo de Reserva de Liquidez (FRL) capitalizade com:

  - 5% do capital aportado por cada novo Aplicante (deduzido nos primeiros 6 meses)

  - 10% da taxa de intermediacao mensal retida pela SEP

  - Aportado diretamente pelos Shareholders como garantia institucional minima de R$ 2M

  - FRL absorve defaults de ate 7% da carteira antes de impactar rendimentos dos Aplicantes

  - Saldo do FRL e auditado externamente e publicado no dashboard do Aplicante em tempo real

**7. COMPLIANCE, AML/KYC E ESTRUTURA OPERACIONAL**

**7.1 Obrigacoes de Compliance da SEP**

| **Obrigacao**                           | **Frequencia**      | **Responsavel**    |
| --------------------------------------- | ------------------- | ------------------ |
| SCR — Central de Risco de Credito       | Mensal              | CFO + Compliance   |
| COAF — Comunicacoes suspeitas PLD/FT    | Ate 24h             | CCROO              |
| LGPD — Relatorio de Impacto (RIPD)      | Anual ou por evento | DPO                |
| Politica de Diversificacao (CMN 5050)   | Revisao semestral   | CRO                |
| Auditoria Externa Independente          | Anual               | Board              |
| Relatorio de Controles Internos (RCI)   | Anual               | Auditoria Interna  |
| Teste de Estresse de Carteira           | Trimestral          | CRO + Data Science |
| Relatorio de Transparencia ao Aplicante | Mensal              | CFO + Produto      |

**7.2 Estrutura Organizacional — SEP NEXUS**

| **Setor**              | **Funcao Principal**                                          | **Headcount Ano 1** |
| ---------------------- | ------------------------------------------------------------- | ------------------- |
| CEO / Presidencia      | Representante legal perante o Bacen + Shareholders            | 1                   |
| CRO — Risco            | OBRIGATORIO para IFs: gestao de risco, Basileia, capital reg. | 1 + eq.3            |
| CCROO — Compliance/PLD | OBRIGATORIO: AML, COAF, Bacen                                 | 1 + eq.4            |
| CFO — Financeiro       | SCR, ODOO, relatorios, gestao do FRL                          | 1 + eq.4            |
| CTO — Tecnologia       | MACRO HASH, AGENTIC AI, API, segurança Bacen (Res.4893)       | 1 + eq.10           |
| Produto & UX           | Dashboards Aplicante, Usuario, 360 Board                      | Eq.5                |
| Crédito & Politica     | Scoring, politica de credito, provisoes                       | Eq.6                |
| Operacoes de Campo     | Executivos Sênior/Júnior e Assistentes Executivos             | 200+ (escala)       |
| Juridico               | Contratos P2P, compliance regulatorio, litígios               | Eq.3                |
| Data Science & BI      | Motor de scoring, 360 Board, analytics                        | Eq.5                |
| Marketing & Growth     | Aquisicao de Aplicantes e Usuarios, comunidade                | Eq.5                |
| SAC                    | Suporte a todas as partes                                     | Eq.15               |
| Merchant Success       | Credenciamento e gestao de merchants                          | Eq.6                |
| Cobranca & Recuperacao | Negociacao de defaults, juridico de cobranca                  | Eq.8                |
| Auditoria Interna      | OBRIGATORIO para IFs                                          | Eq.3                |

**8. ROADMAP DE IMPLEMENTACAO — SEP NEXUS**

| **Fase**              | **Periodo** | **Entregas Principais**                                                                                                      | **Marco Regulatorio**                                                 |
| --------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Fase 0 — Constituicao | Meses 1–3   | S.A. constituida | R$ 1M integralizado | Contratacao CTO/CCROO/CFO | Parceria BIN Sponsor | Contratacao auditoria juridica   | Protocolo pedido autorizacao Bacen OU abertura processo aquisicao SEP |
| Fase 1 — Autorizacao  | Meses 4–18  | MVP plataforma (Aplicante + Usuario) | MACRO HASH v1 | Mercado Secundario v1 | Parceria Executivos piloto (10) | FRL fundado | Obtencao autorizacao Bacen                                            |
| Fase 2 — Beta         | Meses 19–22 | 50 Aplicantes seed | 5.000 Usuarios beta | 50 Executivos | Merchants piloto (100 locais) | Dashboard 360 v1                  | Primeiro SCR ao Bacen                                                 |
| Fase 3 — Go-Live      | Meses 23–30 | Lancamento publico | 500 Aplicantes | 30.000 cartoes | Rede nacional Executivos | Mercado Secundario ao vivo                 | Auditoria externa Ano 1                                               |
| Fase 4 — Escala       | Meses 31–42 | Open Credit API lancada | 2.000 Aplicantes inst. | 120.000 cartoes | Internacionalizacao (Colombia, Mexico)                  | Relatorio CVM se oferta publica                                       |

**9. RECOMENDACAO ESTRATEGICA — QUAL MODELO ADOTAR?**

Após analise completa dos tres documentos (GREY, GREEN-SCD e GREEN-SEP), a recomendacao estratégica depende do perfil do investidor e do horizonte de tempo:

<table>
<tbody>
<tr class="odd">
<td><p><strong>CENARIO 1 — VELOCIDADE MAXIMA + INVESTIDORES GLOBAIS: GREY</strong></p>
<p>Use o Documento GREY se: voce tem acesso a investidores globais (cripto-nativos, family offices internacionais)</p>
<p>e quer lancar em 6 meses sem esperar autorizacao do Bacen.</p>
<p>Risco: area cinzenta regulatoria no Brasil. Mitigacao: assessoria juridica especializada + estrutura Dubai.</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>CENARIO 2 — CREDIBILIDADE MAXIMA + INVESTIDORES INSTITUCIONAIS BR: GREEN-SCD</strong></p>
<p>Use o Documento SCD se: voce quer se posicionar como 'Nubank do credito rotativo' para investidores institucionais</p>
<p>brasileiros (fundos, family offices, bancas). O FIDC e o instrumento perfeito para grandes volumes.</p>
<p>Risco: tributacao IF onerosa. Mitigacao: planejamento tributario via JCP e holding.</p></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><p><strong>CENARIO 3 — P2P AUTENTICO + PITCH MAIS PODEROSO: GREEN-SEP</strong></p>
<p>Use o Documento SEP se: voce quer o modelo mais proximo do LendingClub/Prosper, com Aplicantes PF/PJ</p>
<p>sendo os credores diretos. Mercado Secundario de Contratos e o diferencial que nenhum player BR tem.</p>
<p>Risco: menor receita bruta para a empresa vs SCD. Compensado por menor custo de capital.</p></td>
</tr>
</tbody>
</table>

**RECOMENDACAO FINAL DO CONSULTOR: Comece com GREEN-SEP para o mercado brasileiro (credibilidade + modelo autentico + menor capital inicial), e implemente simultaneamente a estrutura GREY para captacao de Aplicantes internacionais via Dubai/Cayman. A SCD pode ser incorporada no Ano 2 como subsidiaria que securitiza a carteira via FIDC para captacao institucional em larga escala. Este modelo 'tri-estrutura' e o mais robusto e defensavel em termos de pitch para Series A.**

**10. REFERENCIAS**

\[1\] Banco Central do Brasil. Resolucao CMN 5.050/2022 — Consolida as normas SCD e SEP.

\[2\] Banco Central do Brasil. Resolucao CMN 5.177/2024 — Atualizacao regulatoria (vigência 01/01/2025).

\[3\] Lei 4.595/1964 — Lei da Reforma Bancaria.

\[4\] Lei 10.406/2002 — Codigo Civil Brasileiro (contratos de emprestimo entre pessoas).

\[5\] CVM. Instrucao 476/2009 — Oferta pública com esforcos restritos.

\[6\] Iyer, R. et al. (2009). Screening in new credit markets (NBER W15242).

\[7\] Lin, M., Prabhala, N. R., Viswanathan, S. (2012). Judging borrowers by the company they keep.

\[8\] Herzenstein, M. et al. (2008). Tell me a good story and I may lend you money.

\[9\] Pope, D. G., Sydnor, J. R. (2011). Discrimination evidence from Prosper.com. J. Human Resources.

\[10\] Berger, S. C., Gleisner, F. (2009). Emergence of financial intermediaries. BuR Springer.

\[11\] Frerichs, A., Schumann, M. (2008). Peer-to-Peer Lending: Opportunities and Risks.

\[12\] Ashta, A., Assadi, D. (2009). Do Social Cause and Social Technology Meet? ULB Working Paper.

\[13\] Herrero-Lopez, S. (2009). Social Interactions in P2P Lending. Baruch College Working Paper.

\[14\] Mintos (2024). Annual Investor Report 2024. Mintos Marketplace.

\[15\] Bondora (2024). Go & Grow — Product Documentation. Bondora Group.

\[16\] Nexoos (2024). Relatorio Anual — Plataforma SEP Brasil.

\[17\] Bacen (2023). Relatorio de Estabilidade Financeira — Fintechs de Credito.

*NEXUS GREEN-SEP v1.0 | Abril 2026 | Documento Confidencial | Todos os direitos reservados*
