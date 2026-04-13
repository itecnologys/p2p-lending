---
title: "NEXUS — NEXUS_GREEN_SCD_Whitepaper_v1"
date: "Abril 2026"
---

<table>
<tbody>
<tr class="odd">
<td><p><strong>[ WHITEPAPER CONFIDENCIAL — DOCUMENTO GREEN-SCD v1.0 — ABRIL 2026 ]</strong></p>
<p><strong>PROJECTO NEXUS GREEN-SCD</strong></p>
<p><strong>Plataforma P2P via Sociedade de Crédito Direto</strong></p>
<p><em>Modelo Regulado · Banco Central do Brasil · Resolução CMN 5050/2022 · Capital Próprio</em></p></td>
</tr>
</tbody>
</table>

*Este documento apresenta a estrutura do Projeto NEXUS operando sob o modelo de Sociedade de Crédito Direto (SCD), modalidade regulada pelo Banco Central do Brasil. É destinado a investidores, Conselho de Administração, assessores jurídicos e reguladores.*

**SUMÁRIO EXECUTIVO**

O Documento GREEN-SCD apresenta a arquitetura regulada do Projeto NEXUS operando como Sociedade de Crédito Direto (SCD). Na modalidade SCD, a plataforma usa CAPITAL PRÓPRIO para realizar as operações de crédito — não capta recursos diretamente do público. Os Aplicantes investem via emissão de cotas/debêntures da SCD, o capital é alocado internamente e os empréstimos são formalizados em nome da pessoa jurídica. O modelo oferece maior simplicidade operacional, menor risco regulatório e acesso ao ecossistema bancário/fintech nacional, mas exige capital mínimo de R$ 1M e limita a captação de recursos ao mercado de capitais (CVM/B3).

<table>
<tbody>
<tr class="odd">
<td><p><strong>VANTAGENS ESTRATÉGICAS DO MODELO SCD</strong></p>
<p>✔ Capital próprio: sem dependência de múltiplos investidores P2P para funding</p>
<p>✔ Marca regulada: 'aprovado pelo Banco Central' como diferencial de credibilidade</p>
<p>✔ Acesso a serviços bancários: conta-corrente, TEDs, Pix, câmara de compensação</p>
<p>✔ Integração Open Finance: acesso a dados de clientes com consentimento (LGPD)</p>
<p>✔ Parceria com bandeiras: emissão de cartão Visa/Mastercard via BIN Sponsor nacional</p>
<p>✔ Potencial de securitização: FIDC para captar junto a investidores qualificados</p>
<p>✔ Menor risco de enquadramento criminal (Lei 7.492/86 — 'crimes contra o SFN')</p></td>
</tr>
</tbody>
</table>

**1. REGULAÇÃO — SOCIEDADE DE CRÉDITO DIRETO (SCD)**

A SCD foi criada pela Resolução CMN 4.656/2018 (revogada e incorporada pela Resolução CMN 5.050/2022, atualizada pela CMN 5.177/2024 com vigência a partir de 01/01/2025). É uma instituição financeira não-bancária autorizada a funcionar pelo Banco Central do Brasil.

**1.1 Características Fundamentais da SCD**

| **Característica**           | **Regra SCD**                                                  | **Impacto no NEXUS**                                            |
| ---------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| Capital Mínimo               | R$ 1.000.000 (patrimônio líquido permanente)                   | Aporte inicial de pelo menos R$ 1M pelos Shareholders           |
| Fonte de Recursos            | EXCLUSIVAMENTE capital próprio (sem captação do público)       | Funding via FIDC, debêntures, emissão de ações — não P2P direto |
| Operações Permitidas         | Empréstimos, financiamentos, aquisição de direitos creditórios | Todos os produtos NEXUS são compatíveis                         |
| Meio de Concessão            | OBRIGATORIAMENTE via plataforma eletrônica                     | Confirma o modelo digital-first do NEXUS                        |
| Participação em Outras Inst. | PROIBIDA participação no capital de IFs                        | SPE Exchange não pode ser IF; deve ser empresa de tecnologia    |
| Emissão de Cartão            | Permitida via parceria com instituição emissora                | Parceria com Mastercard/Visa via BIN Sponsor (BS2, Cora, etc.)  |
| Cessão de Crédito            | Permitida para Fundos (FIDC) e outras instituições             | Securitização para captação de novos recursos                   |
| FIDC                         | SCD pode originar e ceder para FIDC                            | Mecanismo principal de funding escalável                        |
| Supervisão                   | Banco Central do Brasil — inspeções periódicas                 | Compliance e auditoria interna obrigatórios                     |
| Reporte                      | SCR (Central de Risco de Crédito) — mensal                     | Toda a carteira reportada ao Bacen mensalmente                  |

**1.2 Processo de Autorização pelo Banco Central**

O processo de autorização de uma SCD junto ao Banco Central segue as etapas abaixo:

  - ETAPA 1 — Constituição: Constituir S.A. com capital mínimo de R$ 1M integralizado em dinheiro

  - ETAPA 2 — Documentação: Submeter ao Bacen estatuto social, atas, qualificação de controladores e administradores (fit & proper test)

  - ETAPA 3 — Plano de Negócios: Apresentar plano de negócios detalhado com projeções financeiras para 3 anos

  - ETAPA 4 — Análise Bacen: Prazo médio de 12 a 18 meses para análise e visita in loco

  - ETAPA 5 — Autorização: Publicação no Diário Oficial da autorização para funcionamento

  - ETAPA 6 — Início das Operações: Comunicação ao Bacen do início das operações

**ESTRATÉGIA ACELERADA: Aquisição de SCD já autorizada (shell company) reduz o prazo de autorização de 18 meses para 30–60 dias. Mercado atual: SCDs autorizadas e disponíveis para aquisição custam entre R$ 800k e R$ 3M dependendo do portfólio e histórico.**

**2. MODELO DE NEGÓCIO ADAPTADO PARA SCD**

Na modalidade SCD, o Aplicante não empresta dinheiro diretamente ao Usuário — ele investe no instrumento financeiro emitido pela SCD (debêntures, cotas de FIDC ou CRI/CRA via estrutura de securitização). A SCD, por sua vez, concede o crédito com seu próprio capital e repassa os rendimentos aos investidores conforme acordado.

**2.1 Fluxo de Funding na SCD**

<table>
<tbody>
<tr class="odd">
<td><p><strong>ESTRUTURA DE CAPTAÇÃO — SCD NEXUS</strong></p>
<p>FONTE 1 — Capital Social: R$ 1M a R$ 10M dos Shareholders fundadores</p>
<p>FONTE 2 — Debêntures Simples: Emissão via CVM (Instrução 476 — esforços restritos, ≤20 investidores qualificados)</p>
<p>FONTE 3 — FIDC (Fundo de Investimento em Direitos Creditórios): SCD origina créditos e cede ao FIDC; FIDC capta dos Aplicantes (cotistas)</p>
<p>FONTE 4 — CRA/CRI: Para verticais agro e imobiliário, emissão de CRA/CRI via securitizadora parceira</p>
<p>FONTE 5 — Parceria Bancária: Linha de crédito com banco parceiro (BaaS) para capital de giro da operação</p>
<p>FONTE 6 — Venture Debt: Capital de dívida de fundos de venture debt para fase de escala</p></td>
</tr>
</tbody>
</table>

**2.2 FIDC — Veículo Principal de Escala**

O FIDC (Fundo de Investimento em Direitos Creditórios) é o principal mecanismo de escala do modelo SCD, pois permite que a SCD 'recicle' o capital continuamente:

  - SCD origina carteira de crédito (contratos de empréstimo via cartão NEXUS)

  - SCD cede os direitos creditórios ao FIDC (venda da carteira)

  - FIDC emite cotas Sênior (menor risco, menor retorno: CDI + 5% a.a.) e cotas Júnior/Mezanino (maior risco, maior retorno: CDI + 15% a.a.)

  - Aplicantes do NEXUS compram as cotas Júnior/Sênior do FIDC (através da plataforma)

  - SCD recebe o capital da cessão e origina novos créditos — ciclo contínuo

  - Administrador e Custodiante do FIDC: instituição financeira licenciada (ex: BRL Trust, Oliveira Trust, BTG Pactual)

**2.3 Mecanismo do Cartão no Modelo SCD**

No modelo SCD, o cartão pré-pago NEXUS é emitido diretamente sob a licença da SCD em parceria com um BIN Sponsor nacional. O fluxo é inteiramente em reais:

<table>
<tbody>
<tr class="odd">
<td><p><strong>FLUXO DO CARTÃO — MODELO SCD (100% BRL)</strong></p>
<p>1. SCD aprova limite de crédito ao Usuário (R$ 500 a R$ 2.500) após scoring KYC/AML</p>
<p>2. Cartão pré-pago é emitido pelo BIN Sponsor (ex: Matera, Dock, Conductor, BS2)</p>
<p>3. SCD carrega o cartão com o valor aprovado (débito na conta da SCD)</p>
<p>4. Usuário usa o cartão nos merchants credenciados (MCCs habilitados por vertical)</p>
<p>5. SCD recebe o MDR de 3% do merchant via adquirente parceiro</p>
<p>6. No vencimento da fatura, Usuário paga o valor total + 6% de taxa de utilização</p>
<p>7. Capital repago retorna à SCD → novo crédito liberado no cartão (ciclo recorrente)</p>
<p>8. Rendimentos são distribuídos aos cotistas do FIDC mensalmente (CDI + spread)</p></td>
</tr>
</tbody>
</table>

**3. ANÁLISE COMPARATIVA — VANTAGENS E DESVANTAGENS DA SCD**

**3.1 Vantagens da SCD vs. SEP vs. GREY**

| **Dimensão**         | **SCD**                      | **SEP**                      | **GREY (Stablecoin)**   |
| -------------------- | ---------------------------- | ---------------------------- | ----------------------- |
| Regulação Bacen      | ✔ Licença plena IF           | ✔ Licença plena IF           | ✘ Fora do BC Brasil     |
| Credibilidade Inst.  | ★★★★★ Máxima                 | ★★★★☆ Alta                   | ★★★☆☆ Média (offshore)  |
| Velocidade de Setup  | 12–18m (ou 30d c/ aquisição) | 12–18m                       | 3–6m (Dubai DIFC)       |
| Fonte de Capital     | Próprio + FIDC + Debêntures  | P2P direto (pool público)    | Stablecoin pool global  |
| Risco Regulatório BR | Baixo                        | Baixo                        | ALTO (área cinzenta)    |
| Acesso a Bancários   | Total (conta, Pix, TED)      | Total                        | Via parceiro local      |
| Emissão de Cartão    | Via BIN Sponsor nacional     | Via BIN Sponsor nacional     | Via Rain/Reap + on-ramp |
| Tributação Efetiva   | IR 25% + CSLL 20% (IF)       | IR 25% + CSLL 20% (IF)       | 0% (Dubai) + câmbio     |
| Investor Base        | Qualificados (CVM)           | Pessoa Física e Qualificados | Global (sem restrição)  |
| Pitch para Inst.     | Excelente                    | Muito bom                    | Bom (jurisdição Dubai)  |
| IOF nas Operações    | Sim (tabela fixa)            | Sim                          | Minimizado              |
| Reporte ao Bacen     | Sim (SCR mensal)             | Sim (SCR mensal)             | Não (fora do perímetro) |
| Escalabilidade       | Alta (via FIDC)              | Alta (via pool público)      | Alta (via crypto pool)  |

**3.2 Riscos Específicos da SCD**

  - RISCO DE CAPITAL: A SCD opera com capital próprio — se a inadimplência superar o patrimônio líquido, a SCD pode se tornar insolvente. Mitigação: FIDC com subordinação e Fundo de Reserva.

  - RISCO REGULATÓRIO: Mudanças na regulação do Bacen podem afetar o modelo de negócio. Mitigação: diversificação entre SCD e outras estruturas.

  - RISCO DE LIQUIDEZ: Carteira ilíquida até cessão ao FIDC. Mitigação: originação diversificada e linha de crédito bancária como backstop.

  - RISCO TRIBUTÁRIO: SCDs têm tributação de instituição financeira (IR 25% + CSLL 20% = 45% sobre lucro). Mitigação: planejamento tributário via JCP e estrutura holding.

  - RISCO DE CONCENTRAÇÃO: Dependência de poucos investidores qualificados no FIDC. Mitigação: diversificação da base de cotistas e múltiplas séries.

**4. TRIBUTAÇÃO E PLANEJAMENTO FISCAL — SCD**

A SCD é classificada como instituição financeira pelo Banco Central, o que implica tributação diferenciada (mais onerosa) em comparação a empresas não-financeiras:

**4.1 Tributos Incidentes sobre a SCD**

| **Tributo**  | **Base de Cálculo**         | **Alíquota SCD** | **Alíquota Empresa Comum** | **Observação**                           |
| ------------ | --------------------------- | ---------------- | -------------------------- | ---------------------------------------- |
| IRPJ         | Lucro Real/Presumido        | 25%              | 15% + adic. 10%            | IFs: alíquota majorada de 25% flat       |
| CSLL         | Lucro ajustado              | 20%              | 9%                         | IFs: 20% (vs 9% para outras empresas)    |
| PIS          | Receita bruta               | 0,65%            | 0,65%                      | Receitas financeiras: Decreto 8.426/2015 |
| COFINS       | Receita bruta               | 4,00%            | 3% (não-cumulativo)        | IFs: regime cumulativo                   |
| ISS          | Receita de serviços         | 2%–5%            | 2%–5%                      | Depende do município                     |
| IOF/Crédito  | Saldo devedor do empréstimo | 0,0082%/dia      | N/A                        | \= 3% a.a. sobre saldo médio             |
| IOF/Câmbio   | Conversão de moedas         | 0,38%            | 0,38%                      | Aplicável em remessas ao exterior        |
| CPMF (prop.) | Movimentações financeiras   | Não vigente      | Não vigente                | Risco de reintrodução legislativa        |

**4.2 Estratégias de Otimização Tributária**

<table>
<tbody>
<tr class="odd">
<td><p><strong>PLANEJAMENTO TRIBUTÁRIO — SCD NEXUS</strong></p>
<p>▸ JCP (Juros sobre Capital Próprio): dedução de até 50% do lucro como JCP — reduz base do IR/CSLL</p>
<p>▸ Estrutura Holding: SCD como subsidiária de holding PJ — holding captura dividendos isentos de IR</p>
<p>▸ Lucro Real obrigatório: permite dedução integral de despesas operacionais, inadimplência e provisões</p>
<p>▸ Provisão para Devedores Duvidosos (PDD): dedutível do IR na proporção do risco calculado pelo BACEN</p>
<p>▸ Incentivos Regionais: instalação em ZPE (Zona de Processamento de Exportações) ou SUFRAMA pode gerar créditos tributários</p>
<p>▸ FIDC como hedge fiscal: cessão de carteira ao FIDC transfere tributação para cotistas (que podem ser isentos — ex: FII/FIP)</p>
<p>▸ Benefícios da Lei do Bem (inovação tecnológica): despesas com P&amp;D (MACRO HASH, IA) podem ser deduzidas em 160% do valor real</p></td>
</tr>
</tbody>
</table>

**4.3 Carga Tributária Efetiva — Simulação para Pitch**

Simulação baseada em R$ 10M de lucro antes dos impostos no Ano 3, com planejamento tributário otimizado:

| **Item**                   | **Sem Planejamento** | **Com Planejamento Tributário** |
| -------------------------- | -------------------- | ------------------------------- |
| Lucro Antes do IR          | R$ 10.000.000        | R$ 10.000.000                   |
| (-) JCP Dedutível          | —                    | R$ 3.000.000 (30% do PL)        |
| Base de Cálculo IR         | R$ 10.000.000        | R$ 7.000.000                    |
| IRPJ (25%)                 | R$ 2.500.000         | R$ 1.750.000                    |
| CSLL (20%)                 | R$ 2.000.000         | R$ 1.400.000                    |
| PIS/COFINS (4,65% receita) | R$ 1.395.000         | R$ 1.395.000                    |
| Total Tributos             | R$ 5.895.000         | R$ 4.545.000                    |
| Carga Tributária Efetiva   | 58,9%                | 45,4%                           |
| Lucro Líquido              | R$ 4.105.000         | R$ 5.455.000                    |

**5. MODELO FINANCEIRO — SCD NEXUS**

**5.1 Estrutura de Capital e Funding**

| **Instrumento**       | **Montante (Ano 1)** | **Custo do Capital**         | **Prazo** | **Investidores Alvo**          |
| --------------------- | -------------------- | ---------------------------- | --------- | ------------------------------ |
| Capital Social (SCD)  | R$ 5.000.000         | Equity (retorno variável)    | Perpétuo  | Founders + Seed                |
| Debêntures Série 1    | R$ 20.000.000        | CDI + 8% a.a.                | 36 meses  | Investidores qualificados      |
| FIDC Sênior           | R$ 50.000.000        | CDI + 4% a.a.                | 24 meses  | Fundos, FPCPs, Family Offices  |
| FIDC Júnior/Mezanino  | R$ 15.000.000        | CDI + 18% a.a.               | 24 meses  | Aplicantes NEXUS (plataforma)  |
| Linha Bancária (BaaS) | R$ 10.000.000        | CDI + 6% a.a.                | 12 meses  | Banco parceiro (BS2, BV, etc.) |
| TOTAL ANO 1           | R$ 100.000.000       | CDI + \~7% (média ponderada) | —         | —                              |

**5.2 Projeção Financeira — 3 Anos**

| **Indicador**                      | **Ano 1** | **Ano 2**  | **Ano 3** |
| ---------------------------------- | --------- | ---------- | --------- |
| Cartões Ativos                     | 25.000    | 80.000     | 200.000   |
| Carteira de Crédito Ativa          | R$ 37M    | R$ 120M    | R$ 300M   |
| Receita MDR (3%)                   | R$ 9M     | R$ 28M     | R$ 72M    |
| Receita de Juros (6% a.m.)         | R$ 22M    | R$ 72M     | R$ 180M   |
| Receita Total Bruta                | R$ 31M    | R$ 100M    | R$ 252M   |
| Custo Financeiro (FIDC/Debêntures) | – R$ 8M   | – R$ 20M   | – R$ 40M  |
| Custo de Inadimplência (7%)        | – R$ 2,6M | – R$ 8,4M  | – R$ 21M  |
| Despesas Operacionais              | – R$ 20M  | – R$ 45M   | – R$ 85M  |
| EBITDA                             | R$ 0,4M   | R$ 26,6M   | R$ 106M   |
| Tributos (45,4% otimizado)         | – R$ 0,2M | – R$ 12,1M | – R$ 48M  |
| Lucro Líquido                      | R$ 0,2M   | R$ 14,5M   | R$ 58M    |
| Margem Líquida                     | 0,6%      | 14,5%      | 23%       |

**6. COMPLIANCE, AML/KYC E GESTÃO DE RISCOS**

**6.1 Obrigações de Compliance da SCD**

| **Obrigação**                            | **Frequência**   | **Responsável**   | **Sistema**        |
| ---------------------------------------- | ---------------- | ----------------- | ------------------ |
| SCR — Sistema de Central de Risco        | Mensal           | CFO + Compliance  | Bacen API          |
| CadastRO — Cadastro de Pessoas           | Contínuo         | Compliance        | Bacen CadPF/CadPJ  |
| COAF — Comunicação de Operações          | ≤24h (suspeitas) | CCROO             | COAF Web           |
| LGPD — Proteção de Dados                 | Contínuo         | DPO               | Plataforma interna |
| Relatório de Estabilidade Financeira     | Semestral        | CFO               | Bacen Portal       |
| Auditoria Externa                        | Anual            | Board             | Big 4 recomendado  |
| Relatório de Controles Internos (RCI)    | Anual            | Auditoria Interna | Bacen Portal       |
| PLD/FT — Prevenção LD/Financ. Terrorismo | Contínuo         | CCROO             | Software PLD       |

**6.2 Processo KYC/AML do Usuário**

O processo de qualificação do Usuário na SCD NEXUS combina validação automatizada com revisão humana pelo Executivo de Contas responsável pela área:

  - FASE 1 — IDENTIFICAÇÃO: CPF, RG/CNH, selfie com documento, comprovante de residência

  - FASE 2 — VALIDAÇÃO DE RENDA: Holerite, extrato bancário 3 meses, declaração IR (quando aplicável)

  - FASE 3 — BUREAU CHECK: Serasa Experian, SPC, Quod, Boa Vista + SCR Bacen

  - FASE 4 — SCORING NEXUS: Motor proprietário com 40+ variáveis comportamentais + bureau

  - FASE 5 — REVISÃO HUMANA: Executivo de Contas valida e aprova (ou solicita documentação adicional)

  - FASE 6 — ENQUADRAMENTO DE VERTICAL: Sistema define vertical(is) do Usuário e limite inicial do cartão

  - FASE 7 — ASSINATURA DIGITAL: Contrato de crédito rotativo assinado via DocuSign ou plataforma parceira

**7. ESTRUTURA ORGANIZACIONAL NEXUS-SCD**

A estrutura organizacional da SCD NEXUS é idêntica ao Documento GREY nos elementos de campo (Executivos, Gerentes, Diretores), mas inclui departamentos adicionais exigidos pelo Bacen para instituições financeiras:

| **Setor**                     | **Função / Obrigação Bacen**                                          | **Headcount Ano 1**    |
| ----------------------------- | --------------------------------------------------------------------- | ---------------------- |
| CEO / Presidência             | Representante legal perante o Bacen                                   | 1                      |
| CRO — Chief Risk Officer      | OBRIGATÓRIO para IFs: gestão de risco, capital regulatório (Basileia) | 1 + eq. 3              |
| CCROO / Diretor de Compliance | OBRIGATÓRIO: PLD/FT, COAF, Bacen                                      | 1 + eq. 4              |
| CFO — Financeiro              | SCR, relatórios Bacen, ODOO, FIDC/Debêntures                          | 1 + eq. 5              |
| CTO — Tecnologia              | Segurança da informação (Res. 4893 Bacen), MACRO HASH                 | 1 + eq. 10             |
| Auditoria Interna             | OBRIGATÓRIO para IFs com PL \> R$ 1M: auditoria independente          | Eq. 3 + auditoria ext. |
| Crédito & Políticas           | Definição de políticas de crédito, provisão (PCLD), scoring           | Eq. 6                  |
| Operações de Campo            | Executivos Sênior/Júnior e Assistentes (comercial)                    | 200+ (escala)          |
| Jurídico                      | Contratos, compliance regulatório, litígios                           | Eq. 3                  |
| Data Science & BI             | Motor de scoring, análise de carteira, 360° Board                     | Eq. 5                  |
| Produto & UX                  | Plataformas Aplicante, Usuário e 360° BOARD                           | Eq. 5                  |
| Marketing & Growth            | Aquisição de Aplicantes (cotistas FIDC) e Usuários                    | Eq. 5                  |
| SAC                           | Suporte a Usuários, Aplicantes e Executivos                           | Eq. 15                 |
| Merchant Success              | Credenciamento e gestão da rede de merchants                          | Eq. 6                  |
| Cobrança & Recuperação        | Negociação, renegociação, jurídico de cobrança                        | Eq. 8                  |

**8. ROADMAP DE IMPLEMENTAÇÃO — SCD NEXUS**

| **Fase**             | **Período** | **Entregas Principais**                                                                                                         | **Marco Regulatório**                               |
| -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Fase 0 — Fundação    | Meses 1–3   | Constituição S.A. | Integralização capital | Contratação time jurídico/compliance | Due diligence SCD disponível para aquisição | Protocolo pedido autorização Bacen ou aquisição SCD |
| Fase 1 — Autorização | Meses 4–18  | Desenvolvimento plataforma MVP | Estruturação FIDC | Parceria BIN Sponsor (Dock/Conductor/BS2) | Implantação ODOO               | Obtenção autorização Bacen (ou closing aquisição)   |
| Fase 2 — Go-Live     | Meses 19–24 | Lançamento plataforma | 100 Executivos de Campo | 10.000 cartões beta | Emissão Debêntures Série 1                              | Primeiro reporte SCR ao Bacen                       |
| Fase 3 — Escala      | Meses 25–36 | Emissão FIDC Série 1 (R$ 50M) | 80.000 cartões | Rede nacional de Executivos | 360° Board completo                              | Auditoria externa Ano 1                             |
| Fase 4 — Expansão    | Meses 37–48 | FIDC Série 2 (R$ 150M) | 200.000 cartões | Internacionalização via parceria com IF estrangeira                                  | ICVM aprovação para oferta pública (CVM)            |

**9. REFERÊNCIAS**

\[1\] Banco Central do Brasil. Resolução CMN 5.050/2022 — Consolida as normas sobre SCD e SEP.

\[2\] Banco Central do Brasil. Resolução CMN 5.177/2024 — Atualização regulatória, vigência 01/01/2025.

\[3\] Banco Central do Brasil. Resolução 4.893/2021 — Política de segurança cibernética para IFs.

\[4\] CVM. Instrução 476/2009 — Oferta pública de esforços restritos (debêntures para qualificados).

\[5\] Lei 4.595/1964 — Lei da Reforma Bancária (define instituição financeira no Brasil).

\[6\] Lei 7.492/1986 — Crimes contra o Sistema Financeiro Nacional.

\[7\] Lei 13.709/2018 — Lei Geral de Proteção de Dados (LGPD).

\[8\] Iyer, R. et al. (2009). Screening in new credit markets (NBER W15242).

\[9\] Berger, S. C., & Gleisner, F. (2009). Emergence of financial intermediaries in electronic markets. BuR.

\[10\] Herzenstein, M. et al. (2008). Tell me a good story and I may lend you money. Working Paper.

\[11\] Lin, M., Prabhala, N. R., & Viswanathan, S. (2012). Judging borrowers by the company they keep.

\[12\] Nexoos (2024). Relatório Anual — Plataforma SEP Brasil.

\[13\] Biva (2024). Relatório de Portfólio — P2P Lending PME Brasil.

\[14\] PricewaterhouseCoopers (2024). Guia Tributário para Instituições Financeiras — Brasil.

*NEXUS GREEN-SCD v1.0 | Abril 2026 | Documento Confidencial | Todos os direitos reservados*
