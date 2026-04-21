---
title: "NEXUS — NEXUS_DEF_v1.0"
date: "Abril 2026"
---

**NEXUS**

**Plataforma P2P de Crédito Inteligente**

**DOCUMENTO DE ESPECIFICAÇÃO FUNCIONAL — DEF v1.0**

| **Versão**            | 1.0 — Abril 2026                                |
| --------------------- | ----------------------------------------------- |
| **Confidencialidade** | Estritamente Confidencial                       |
| **Regulação**         | CMN 5050/2022 · BACEN SCD                       |
| **Tecnologia**        | MACRO HASH SHA-256 · IA Agentic · Visa Pré-Pago |
| **Documento**         | Camada 0 — Fundação Documental                  |

# 1\. Visão Geral do Projeto NEXUS

## 1.1 Conceito e Propósito

O NEXUS é uma plataforma P2P (Peer-to-Peer) de crédito direto, operando sob a regulamentação CMN 5050/2022 do Banco Central do Brasil como Sociedade de Crédito Direto (SCD). A plataforma conecta dois tipos de usuários com interesses complementares:

  - > **Aplicantes (Investidores):** Aplicantes (Investidores): pessoas físicas ou jurídicas que aportam capital em portfólios de crédito com retorno mensal de 3% a 5% a.m., superior ao CDI e à poupança.

  - > **Usuários (Tomadores):** Usuários (Tomadores): pessoas físicas elegíveis (NEXUS Score ≥ 550) que recebem crédito pré-aprovado em blocos de R$40 diretamente em cartão Visa pré-pago, utilizável em 141 verticais de consumo.

**A plataforma é sustentada por três pilares tecnológicos únicos:**

  - > **MACRO HASH:** MACRO HASH Ledger: cadeia SHA-256 auditável de 5 camadas (L1→L5), imutável e verificável publicamente.

  - > **IA Agentic:** IA Agentic Engine: workers Celery/Redis que avaliam score, enfileiram solicitações (FIFO) e distribuem crédito autonomamente.

  - > **NEXUS Score:** NEXUS Score Proprietário: modelo de pontuação 0–1000 baseado em comportamento, dados alternativos e histórico de relacionamento — independente de bureaus externos.

## 1.2 Proposta de Valor por Público

| **Dimensão**        | **Aplicante (Investidor)**      | **Usuário (Tomador)**                  |
| ------------------- | ------------------------------- | -------------------------------------- |
| Benefício principal | Retorno 3–5% a.m. — até 5× CDI  | Crédito pré-aprovado sem burocracia    |
| Produto             | Portfólios A/B/C diversificados | Cartão Visa pré-pago com saldo         |
| Acesso              | App/Web · Aporte mínimo R$500   | Score ≥ 550 · Cartão emitido pela Dock |
| Liquidez            | Retorno PIX D+1 mensalmente     | Crédito liberado em até 2 horas        |

## 1.3 Diferenciais Competitivos vs. Mercado

Análise baseada em estudo das plataformas Mintos (EU) e LenderMarket (IE), líderes mundiais em P2P lending:

| **Funcionalidade**         | **Mintos**         | **LenderMarket**   | **NEXUS**          |
| -------------------------- | ------------------ | ------------------ | ------------------ |
| Auditoria pública SHA-256  | Não                | Não                | ✓ MACRO HASH L1-L5 |
| Cartão pré-pago ao tomador | Não                | Não                | ✓ Visa/Dock        |
| 141 verticais de consumo   | Não                | Não                | ✓ Rastreadas       |
| PIX nativo D+1             | Não (EUR)          | Não (EUR)          | ✓ BACEN DICT       |
| Score proprietário         | Não (bureaus EU)   | Não (bureaus EU)   | ✓ NEXUS Score      |
| IA Agentic FIFO            | Auto-invest básico | Auto-invest básico | ✓ Celery/Redis     |
| Regulação brasileira SCD   | MiFID II (EU)      | CSP (IE)           | ✓ CMN 5050/2022    |

# 2\. Arquitetura de Informação

## 2.1 Módulos da Plataforma

| **Módulo** | **Nome**       | **Responsabilidade**                                  |
| ---------- | -------------- | ----------------------------------------------------- |
| MOD-01     | Auth & KYC     | Cadastro, login, verificação de identidade (3 níveis) |
| MOD-02     | NEXUS Score    | Motor de pontuação proprietário 0–1000                |
| MOD-03     | Portfólios     | Gestão de portfólios A/B/C para Aplicantes            |
| MOD-04     | Investimentos  | Aportes, retornos, relatório IR, extrato              |
| MOD-05     | Crédito FIFO   | Fila Celery/Redis, aprovação, disbursamento           |
| MOD-06     | Cartão Visa    | Emissão Dock/BS2, saldo, transações por vertical      |
| MOD-07     | MACRO HASH     | Ledger SHA-256 L1→L5, verificação pública             |
| MOD-08     | Pagamentos PIX | Aportes, retornos D+1, amortizações                   |
| MOD-09     | Notificações   | Push, email, SMS, webhook                             |
| MOD-10     | Admin Panel    | Gestão interna, compliance, relatórios BACEN          |
| MOD-11     | Analytics      | BI para Aplicante e gestão interna                    |
| MOD-12     | Open Finance   | Integração com dados bancários (futuro)               |

## 2.2 Jornada do Aplicante — Navegação Completa

| **Rota**                     | **Descrição Funcional**                                                 |
| ---------------------------- | ----------------------------------------------------------------------- |
| / (Home pública)             | Apresentação do produto, CTA cadastro/login                             |
| /cadastro                    | Formulário registro: nome, CPF, email, telefone, senha — role=applicant |
| /kyc                         | Upload documentos (RG/CNH + selfie), status KYC                         |
| /dashboard                   | Hub central: saldo total, retorno mês, portfólios ativos, notificações  |
| /dashboard/aportar           | Escolha de portfólio, valor, prazo; geração PIX; confirmação            |
| /dashboard/investimentos     | Lista todos os aportes: status, retorno acumulado, vencimento           |
| /dashboard/investimentos/:id | Detalhe do aporte: cronograma mensal de retornos, MACRO HASH L2         |
| /dashboard/retornos          | Histórico de créditos PIX recebidos, filtros por mês/portfólio          |
| /dashboard/saque             | Solicitar saque via PIX — chave cadastrada, valor, confirmação          |
| /portafolios                 | Marketplace de portfólios: filtros risco/taxa/prazo, simulador          |
| /portafolios/:id             | Detalhe do portfólio: histórico, composição, taxa real, default rate    |
| /score-aplicante             | NEXUS Score do Aplicante: componentes, histórico, como melhorar         |
| /relatorios                  | Extrato IR anual (IRPF), informe de rendimentos, CSV                    |
| /notificacoes                | Centro de notificações: push, email, webhook settings                   |
| /perfil                      | Dados pessoais, chave PIX, senha, autenticação 2FA                      |
| /suporte                     | Chat, FAQ, abertura de ticket                                           |

## 2.3 Jornada do Usuário — Navegação Completa

| **Rota**                     | **Descrição Funcional**                                                |
| ---------------------------- | ---------------------------------------------------------------------- |
| / (Home pública)             | Apresentação do produto, CTA cadastro/login                            |
| /cadastro                    | Formulário registro: nome, CPF, email, telefone, senha — role=user     |
| /kyc                         | Upload documentos, status KYC, aguardar score inicial                  |
| /dashboard                   | Hub: saldo cartão, limite disponível, próxima parcela, NEXUS Score     |
| /dashboard/solicitar-credito | Escolha blocos (1–10 × R$40), vertical, parcelas; envio para fila FIFO |
| /dashboard/meu-credito       | Solicitações: status fila, posição, aprovadas, rejeitadas              |
| /dashboard/meu-credito/:id   | Detalhe: cronograma amortização, MACRO HASH L4, parcelas pagas/abertas |
| /cartao                      | Visualização do cartão Visa virtual: PAN mascarado, saldo, vencimento  |
| /cartao/extrato              | Extrato: transações por vertical, filtros data/categoria, total gasto  |
| /cartao/bloquear             | Bloquear/desbloquear cartão temporariamente                            |
| /score                       | NEXUS Score detalhado: componentes A/B/C/D/E, histórico, dicas         |
| /verticais                   | Mapa das 141 verticais: onde usar o cartão, estabelecimentos aceitos   |
| /parcelas                    | Calendário de parcelas vencidas/próximas, pagamento via PIX/boleto     |
| /notificacoes                | Centro de alertas: limite próximo, parcela vencendo, crédito aprovado  |
| /perfil                      | Dados pessoais, chave PIX para amortização, senha, 2FA                 |
| /suporte                     | Chat, FAQ, contestação de transação                                    |

# 3\. NEXUS Score — Modelo Proprietário 0–1000

O NEXUS Score é um sistema proprietário de pontuação de crédito desenvolvido internamente, independente de bureaus externos. Inspirado metodologicamente no Serasa Score e no FICO, o modelo incorpora dados comportamentais da própria plataforma, dados alternativos e, opcionalmente, enriquecimento de bureaus externos. A pontuação varia de 0 a 1000 pontos, calculada em tempo real e atualizada a cada evento relevante.

## 3.1 Blocos de Variáveis e Pesos

| **Bloco** | **Nome**                       | **Peso** | **Variáveis Principais**                                                                           |
| --------- | ------------------------------ | -------- | -------------------------------------------------------------------------------------------------- |
| A         | Histórico de Pagamentos        | 35%      | Pagamentos em dia, atrasos, inadimplências, renegociações na plataforma NEXUS                      |
| B         | Comportamento de Consumo       | 25%      | Padrão de uso do cartão Visa: regularidade, verticais essenciais vs. discricionárias, ticket médio |
| C         | Dados Financeiros Alternativos | 20%      | Pagamento de contas (via Open Finance), renda estimada, histórico de PIX recebidos                 |
| D         | Cadastro e Relacionamento      | 12%      | Tempo de conta, completude do KYC, documentos válidos, atividade na plataforma                     |
| E         | Bureau Externo (Opcional)      | 8%       | Consulta Serasa como sinal de enriquecimento — não é gate obrigatório                              |

## 3.2 Faixas de Score e Limites de Crédito (Usuário)

| **Faixa**  | **Risco**   | **Status** | **Limite Máx/Solicit.** | **Condições**                        |
| ---------- | ----------- | ---------- | ----------------------- | ------------------------------------ |
| 0 – 399    | Muito Alto  | Bloqueado  | R$ 0                    | Nenhum acesso ao crédito             |
| 400 – 549  | Alto        | Restrito   | R$ 40                   | 1 bloco. Prazo máx 3 meses           |
| 550 – 699  | Médio       | Monitorado | R$ 120                  | 3 blocos. Prazo máx 6 meses          |
| 700 – 849  | Baixo       | Aprovado   | R$ 280                  | 7 blocos. Prazo até 12 meses         |
| 850 – 1000 | Muito Baixo | Premium    | R$ 400                  | 10 blocos. Acesso portfólios premium |

## 3.3 Score do Aplicante (Funding Operator Score)

O Aplicante também possui um NEXUS Funding Score (0–1000), que determina acesso a portfólios premium, limites de aporte e benefícios. Os blocos de avaliação são:

  - > **Consistência de aportes:** 35% — Frequência e regularidade dos depósitos

  - > **Volume e crescimento:** 25% — Crescimento do capital aportado ao longo do tempo

  - > **Comportamento de saque:** 20% — Reinveste vs. saca total — perfil de longo prazo valorizado

  - > **Diversificação de portfólio:** 12% — Distribuição entre portfólios A, B e C

  - > **Tempo de relacionamento:** 8% — Meses ativos na plataforma

# 4\. As 141 Verticais de Consumo

O cartão Visa NEXUS é aceito em 141 verticais de consumo mapeadas, todas recorrentes ou semi-recorrentes, com tickets entre R$30 e R$2.500/mês. As verticais são categorizadas em 15 super-categorias para fins de rastreamento, análise de comportamento de consumo e composição do NEXUS Score Bloco B.

**🍽️ ALIMENTAÇÃO**

  - > V001 Supermercado

  - > V002 Feira livre / hortifrutigranjeiros

  - > V003 Açougue / peixaria

  - > V004 Padaria / confeitaria

  - > V005 Restaurante almoço

  - > V006 Restaurante jantar

  - > V007 Delivery (iFood / Rappi / 99Food)

  - > V008 Lanchonete / fast food

  - > V009 Rotisseria / comida pronta

  - > V010 Empório / produtos orgânicos

  - > V011 Bebidas (adega / loja de bebidas)

  - > V012 Café / cafeteria

  - > V013 Marmita / quentinha

  - > V014 Clube de assinatura de alimentos

  - > V015 Cesta básica

  - > V016 Bebidas alcoólicas (bar)

  - > V017 Mercearia de bairro

  - > V018 Importados / gourmet

**🏠 MORADIA E CASA**

  - > V019 Aluguel (via plataforma parceira)

  - > V020 Condomínio

  - > V021 Energia elétrica

  - > V022 Água e esgoto

  - > V023 Gás encanado / botijão

  - > V024 Internet banda larga

  - > V025 TV por assinatura (pacote)

  - > V026 Telefone fixo

  - > V027 Faxineira / diarista

  - > V028 Segurança / portaria

  - > V029 Manutenção e pequenos reparos

  - > V030 Jardinagem

  - > V031 Decoração / mobiliário parcelado

  - > V032 Materiais de limpeza doméstica

**🚗 TRANSPORTE**

  - > V033 Combustível (posto)

  - > V034 Estacionamento

  - > V035 Seguro veicular

  - > V036 IPVA parcelado

  - > V037 Manutenção / mecânica

  - > V038 Transporte público (cartão VT / bilhete)

  - > V039 App de corrida (Uber / 99)

  - > V040 Motofrete / motoboy

  - > V041 Pedágio / tag

  - > V042 Financiamento de veículo (parcela)

  - > V043 Lavagem e detalhamento

  - > V044 Pneus e acessórios automotivos

**❤️ SAÚDE E BEM-ESTAR**

  - > V045 Plano de saúde (mensalidade)

  - > V046 Consulta médica particular

  - > V047 Dentista / ortodontia

  - > V048 Farmácia / medicamentos

  - > V049 Academia / crossfit / musculação

  - > V050 Fisioterapia / quiropraxia

  - > V051 Psicólogo / psiquiatra

  - > V052 Nutricionista

  - > V053 Exames laboratoriais / imagem

  - > V054 Plano odontológico

  - > V055 Óptica / óculos

  - > V056 Suplementos alimentares

  - > V057 Spa / massagem terapêutica

  - > V058 Home care / enfermagem

**📚 EDUCAÇÃO**

  - > V059 Escola particular (mensalidade)

  - > V060 Faculdade / pós-graduação

  - > V061 Curso de idiomas

  - > V062 Curso profissionalizante / técnico

  - > V063 Plataforma EAD (Alura / Udemy / Coursera)

  - > V064 Material escolar e livros

  - > V065 Aulas particulares / tutoria

  - > V066 Creche / berçário

  - > V067 Intercâmbio parcelado

  - > V068 Curso preparatório (concurso / vestibular)

**👗 VESTUÁRIO E MODA**

  - > V069 Roupas do dia a dia

  - > V070 Calçados

  - > V071 Roupa social / trabalho

  - > V072 Roupa infantil

  - > V073 Roupas íntimas e meias

  - > V074 Acessórios (bolsas / cintos / relógios)

  - > V075 Roupa fitness / esportiva

  - > V076 Reparos e costura

**💆 BELEZA E CUIDADOS PESSOAIS**

  - > V077 Salão de beleza / cabeleireiro

  - > V078 Barbearia

  - > V079 Manicure / pedicure

  - > V080 Produtos de higiene pessoal

  - > V081 Perfumaria / cosméticos

  - > V082 Depilação (laser / cera)

  - > V083 Skincare / estética facial

  - > V084 Maquiagem

  - > V085 Sobrancelha / cílios

**🎮 LAZER E ENTRETENIMENTO**

  - > V086 Streaming vídeo (Netflix / Disney+ / Max / Globoplay)

  - > V087 Streaming música (Spotify / Deezer)

  - > V088 Jogos / games (Steam / PS Store / Xbox)

  - > V089 Cinema / teatro / shows

  - > V090 Eventos e ingressos (Sympla / Ticket Master)

  - > V091 Viagem (parcela hotel / passagem)

  - > V092 Clube / associação esportiva

  - > V093 Hobby (fotografia / artesanato / colecionismo)

  - > V094 Leitura (Kindle / revistas / assinaturas)

  - > V095 Parque de diversões / eventos infantis

  - > V096 Esportes (tênis / futebol / natação)

  - > V097 Karaokê / bowling / lazer noturno

**📱 TECNOLOGIA E DIGITAL**

  - > V098 Celular (prestação / upgrade)

  - > V099 Computador / notebook (prestação)

  - > V100 Software / apps por assinatura

  - > V101 Cloud storage (Google / iCloud / Dropbox)

  - > V102 Antivírus / segurança digital

  - > V103 TV / eletrodoméstico parcelado

  - > V104 Smartwatch / wearable

  - > V105 Carregadores e acessórios tech

**🐾 PET**

  - > V106 Ração e petiscos

  - > V107 Veterinário / consultas

  - > V108 Pet shop / banho e tosa

  - > V109 Remédios e vacinas pet

  - > V110 Plano de saúde pet

  - > V111 Brinquedos e acessórios pet

**🏋️ ESPORTE E FITNESS**

  - > V112 Mensalidade academia

  - > V113 Equipamentos esportivos

  - > V114 Roupa esportiva especializada

  - > V115 Suplemento esportivo

  - > V116 Personal trainer / professor

  - > V117 Apps fitness premium (Strava / Nike Training)

**🔧 SERVIÇOS DO LAR**

  - > V118 Dedetização / controle de pragas

  - > V119 Conserto de eletrodomésticos

  - > V120 Pintura / pequena reforma

  - > V121 Chaveiro / serralhearia

  - > V122 Instalações elétricas e hidráulicas

  - > V123 Frete / mudança

  - > V124 Conserto de eletrônicos

  - > V125 Arquitetura / design de interiores

**💼 SERVIÇOS FINANCEIROS E PROTEÇÃO**

  - > V126 Seguro de vida (parcela)

  - > V127 Seguro residencial

  - > V128 Previdência privada (aporte mensal)

  - > V129 Consórcio (parcela)

  - > V130 Cartório / registro / reconhecimento firma

  - > V131 Serviços contábeis / contador

  - > V132 Consultoria jurídica

**🎁 PRESENTES E SOCIAL**

  - > V133 Presente de aniversário / datas comemorativas

  - > V134 Churrasco / confraternização

  - > V135 Casamento / festa (parcelamento)

  - > V136 Festa infantil / buffet

  - > V137 Doação / dízimo / contribuição social

**🌱 SUSTENTABILIDADE E NICHO**

  - > V138 Energia solar (parcela do sistema)

  - > V139 Horta e jardim urbano

  - > V140 Produtos sustentáveis / zero waste

  - > V141 Assinatura de caixas temáticas (nicho)

# 5\. Especificação Funcional por Módulo

## MOD-01 · Auth & KYC

O módulo de autenticação e KYC gerencia o ciclo completo de onboarding do usuário, desde o cadastro até a aprovação regulatória. Existem 3 níveis de KYC progressivos:

| **Nível**   | **Requisitos**                      | **Permissões**                                  | **Prazo de Aprovação** |
| ----------- | ----------------------------------- | ----------------------------------------------- | ---------------------- |
| KYC Nível 1 | Email + CPF validados               | Explorar plataforma, ver portfólios, simulações | Automático (\< 1 min)  |
| KYC Nível 2 | Doc de identidade (RG/CNH) + selfie | Investir, solicitar crédito, receber cartão     | 1–2 dias úteis         |
| KYC Nível 3 | Comprovante de renda + endereço     | Limites aumentados, portfólios premium          | 2–5 dias úteis         |

**Campos obrigatórios no cadastro:**

  - > Nome completo (conforme documento)

  - > CPF (11 dígitos, validação de algoritmo)

  - > E-mail (verificação por link)

  - > Telefone celular (verificação por SMS/WhatsApp)

  - > Senha (mínimo 8 caracteres, 1 maiúscula, 1 número, 1 especial)

  - > Role: applicant ou user (seleção no cadastro)

  - > Data de nascimento

Estados do KYC: pending → in\_review → approved | rejected. Em caso de rejeição, o sistema informa o motivo e permite reenvio em até 3 tentativas antes de bloqueio temporário de 30 dias.

## MOD-02 · NEXUS Score Engine

O Score Engine é um serviço assíncrono que recalcula o NEXUS Score de cada usuário mediante eventos-gatilho. O cálculo nunca ocorre em tempo real de requisição — é processado em background e o resultado é cacheado.

**Eventos que disparam recálculo:**

  - > Pagamento de parcela (pontual ou atrasado)

  - > Nova transação no cartão Visa

  - > Aprovação ou rejeição de KYC

  - > Consulta de bureau externo (Bloco E)

  - > Inatividade de 30+ dias na plataforma

  - > Novo aporte do Aplicante (Funding Score)

<table>
<tbody>
<tr class="odd">
<td><p><strong>Fórmula NEXUS Score</strong></p>
<p>Score = (PagamentosNDia × 0.35) + (ComportamentoCartão × 0.25) +</p>
<p>(DadosAlternativos × 0.20) + (Relacionamento × 0.12) + (BureauExterno × 0.08)</p>
<p>Onde cada componente é normalizado para a escala 0–1000 antes da ponderação.</p></td>
</tr>
</tbody>
</table>

## MOD-03 · Portfólios de Investimento

Os portfólios são veículos de investimento coletivo onde múltiplos Aplicantes aportam capital que é distribuído entre contratos de crédito com Usuários. Existem 3 classes de risco:

| **Classe**  | **Risco** | **Taxa Mensal**  | **Aporte Mín.** | **Aporte Máx.** | **Prazo** | **Default Máx.** | **Critério Usuário** |
| ----------- | --------- | ---------------- | --------------- | --------------- | --------- | ---------------- | -------------------- |
| Portfólio A | Baixo     | 3,0% – 3,8% a.m. | R$ 500          | R$ 50.000       | 3–12m     | \< 2%            | Score Usuário ≥ 850  |
| Portfólio B | Médio     | 3,9% – 4,5% a.m. | R$ 500          | R$ 100.000      | 3–12m     | 2%–5%            | Score Usuário ≥ 700  |
| Portfólio C | Alto      | 4,6% – 5,0% a.m. | R$ 500          | R$ 100.000      | 3–12m     | 5%–8%            | Score Usuário ≥ 550  |

**Campos exibidos na listagem de portfólios:**

  - > Nome e classificação (A/B/C) com badge de risco colorido

  - > Taxa mensal mínima e máxima (ex: 3,9% – 4,5% a.m.)

  - > Aporte mínimo e capacidade disponível (barra de progresso)

  - > Número de contratos ativos e taxa de inadimplência atual

  - > Prazo disponível: 3 / 6 / 9 / 12 meses (seletor interativo)

  - > Botão 'Simular' (abre calculadora inline) e botão 'Investir'

## MOD-04 · Aportes e Retornos (Aplicante)

**Fluxo de aporte:**

  - > 1\. Aplicante seleciona portfólio e define: valor (≥ R$500), prazo (3/6/9/12m)

  - > 2\. Plataforma exibe projeção: retorno bruto, IR retido, retorno líquido, comparativo CDI

  - > 3\. Aplicante confirma → sistema gera cobrança PIX (copia-e-cola + QR code)

  - > 4\. PIX pago → confirmação via webhook Dock → aporte ativado

  - > 5\. MACRO HASH L2 (Investor Block) gerado e registrado

  - > 6\. Retorno creditado mensalmente em D+1 via PIX na chave cadastrada

**Cálculo de retorno (fórmula de juros compostos):**

<table>
<tbody>
<tr class="odd">
<td><p><strong>Fórmulas de Retorno</strong></p>
<p>Retorno Bruto = Principal × (1 + taxa_mensal)^n - Principal</p>
<p>IR Retido = Retorno_Bruto × alíquota_IR(n) [tabela regressiva IRPF]</p>
<p>Retorno Líquido = Retorno_Bruto - IR_Retido</p>
<p>Tabela IR (prazo do investimento):</p>
<p>Até 180 dias → 22,5%</p>
<p>181 a 360 dias → 20,0%</p>
<p>361 a 720 dias → 17,5%</p>
<p>Acima de 720 dias → 15,0%</p>
<p>Comparativo CDI: CDI_Retorno = Principal × (1 + CDI_mensal)^n - Principal</p>
<p>Multiplicador NEXUS vs CDI = Retorno_Liquido_NEXUS / CDI_Retorno</p></td>
</tr>
</tbody>
</table>

## MOD-05 · Módulo de Crédito — Fila FIFO Agentic

O módulo de crédito é o coração operacional do NEXUS. Utiliza workers Celery com broker Redis para processar solicitações de forma assíncrona, justa (FIFO) e auditável.

**Fluxo completo de uma solicitação de crédito:**

| **Etapa**             | **Descrição**                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1\. Solicitação       | Usuário define: blocos (1–10), vertical de uso, número de parcelas (1–12). Sistema valida score ≥ 550 e KYC nível 2.              |
| 2\. Enfileiramento    | Solicitação inserida na fila Redis com timestamp. Status: queued. Posição na fila exibida ao usuário em tempo real via websocket. |
| 3\. Worker Celery     | Worker consome a fila FIFO. Verifica disponibilidade de capital nos portfólios elegíveis (match por taxa de risco do score).      |
| 4\. Score Check       | Revalidação do score em tempo real (pode ter mudado desde a solicitação). Score abaixo do mínimo → rejeição com motivo.           |
| 5\. Matching          | Sistema faz match com portfólio(s) de maior compatibilidade. Reserva o capital necessário no portfólio selecionado.               |
| 6\. MACRO HASH L4     | Contract Block gerado: H(contract\_id || user\_id || amount || terms || L3\_hash). Assinado e registrado no ledger.               |
| 7\. Emissão do cartão | Se Usuário não tem cartão: solicita emissão à Dock/BS2 via API. Cartão virtual disponível em minutos.                             |
| 8\. Crédito no cartão | Blocos R$40 × n creditados no saldo do cartão Visa via API Dock. MACRO HASH L5 (Block State) gerado por bloco.                    |
| 9\. Notificação       | Push + email: 'Seu crédito de R$X foi aprovado e está disponível no seu cartão\\\!'                                               |
| 10\. Monitoramento    | Parcelas monitoradas diariamente. Atraso \> 3 dias → notificação. Atraso \> 15 dias → impacto no Score Bloco A.                   |

**Fórmula de amortização (Sistema Price — parcelas fixas):**

<table>
<tbody>
<tr class="odd">
<td><p><strong>Amortização Price (Parcelas Fixas)</strong></p>
<p>PMT = PV × [i × (1+i)^n] / [(1+i)^n - 1]</p>
<p>Onde:</p>
<p>PMT = valor da parcela mensal (fixo)</p>
<p>PV = valor presente (total crédito concedido em R$)</p>
<p>i = taxa mensal de juros (definida pelo portfólio matched)</p>
<p>n = número de parcelas escolhidas pelo Usuário</p>
<p>Cada parcela é composta por amortização + juros decrescentes ao longo do tempo.</p>
<p>O retorno ao Aplicante é calculado proporcional à sua participação no portfólio.</p></td>
</tr>
</tbody>
</table>

## MOD-06 · Cartão Visa Pré-Pago (Dock/BS2)

O cartão Visa pré-pago é o veículo de entrega do crédito ao Usuário. Emitido pela Dock como BIN Sponsor Visa/Mastercard, com BS2 como banco parceiro. O saldo é carregado por blocos de R$40 conforme crédito aprovado.

**Tela do cartão (campos exibidos):**

  - > PAN mascarado: \*\*\*\* \*\*\*\* \*\*\*\* 4521

  - > Nome do titular

  - > Validade (mês/ano)

  - > Bandeira: Visa ou Mastercard

  - > Saldo disponível (destaque em verde)

  - > Limite total contratado

  - > Próxima parcela (data + valor)

  - > Status: Ativo / Bloqueado / Cancelado

  - > Botão 'Bloquear temporariamente'

  - > Botão 'Ver número completo' (autenticação 2FA exigida)

**Extrato do cartão — campos por transação:**

  - > Data e hora da transação

  - > Nome do estabelecimento

  - > Vertical de consumo (ex: V007 · Delivery)

  - > Valor em R$

  - > Tipo: purchase / credit\_block / refund / fee

  - > Status: authorized / settled / reversed / failed

  - > MACRO HASH L5 (para transações de credit\_block)

## MOD-07 · MACRO HASH Ledger

O MACRO HASH é o sistema de auditoria criptográfica do NEXUS. Uma cadeia de 5 camadas de hashes SHA-256, append-only (imutável), onde cada bloco encadeia o hash do bloco pai — tornando qualquer adulteração detectável imediatamente.

| **Nível** | **Nome**        | **Entidade**                | **Composição do Hash**                                 | **Quando é Criado**                 |
| --------- | --------------- | --------------------------- | ------------------------------------------------------ | ----------------------------------- |
| L1        | Platform State  | Estado global da plataforma | H(platform\_id || timestamp || config\_hash)           | Criado uma vez por período (diário) |
| L2        | Investor Block  | Aporte do Aplicante         | H(investor\_id || portfolio\_id || amount || L1\_hash) | Criado a cada novo aporte           |
| L3        | Portfolio Block | Parâmetros do portfólio     | H(portfolio\_params || allocation || L2\_hash)         | Criado/atualizado a cada alocação   |
| L4        | Contract Block  | Contrato com o Usuário      | H(contract\_id || user\_id || terms || L3\_hash)       | Criado a cada crédito aprovado      |
| L5        | Block State     | Bloco R$40 no cartão        | H(block\_id || amount\_40 || card\_token || L4\_hash)  | Criado a cada bloco creditado       |

<table>
<tbody>
<tr class="odd">
<td><p><strong>Verificação Pública</strong></p>
<p>O NEXUS publica o hash raiz L1 de cada período em /ledger/root (endpoint público, sem autenticação).</p>
<p>Qualquer auditor externo pode verificar a integridade completa do ledger via GET /ledger/verify/{hash}</p>
<p>sem precisar de acesso a dados sensíveis — apenas comparando hashes SHA-256.</p></td>
</tr>
</tbody>
</table>

# 6\. Regras de Negócio

## 6.1 Regras do Lado Aplicante

  - > **RN-A01** Aporte mínimo: R$ 500 por portfólio por operação.

  - > **RN-A02** Aporte máximo por operação: R$ 100.000 (pode variar por portfólio).

  - > **RN-A03** KYC Nível 2 obrigatório para realizar qualquer aporte.

  - > **RN-A04** Retornos creditados via PIX D+1 no primeiro dia útil após fechamento mensal.

  - > **RN-A05** IR retido na fonte conforme tabela regressiva IRPF (22,5% a 15%).

  - > **RN-A06** Prazo mínimo de investimento: 3 meses. Máximo: 12 meses por operação.

  - > **RN-A07** Resgate antecipado: não permitido nos primeiros 60 dias. Após: sujeito a taxa de saída de 1%.

  - > **RN-A08** Informe de rendimentos anual gerado automaticamente até 28 de fevereiro do ano seguinte.

  - > **RN-A09** Diversificação máxima: um Aplicante pode deter no máximo 20% do capital total de um portfólio.

  - > **RN-A10** Relatório mensal enviado por email com: retorno bruto, IR, retorno líquido, default rate do portfólio.

## 6.2 Regras do Lado Usuário (Tomador)

  - > **RN-U01** NEXUS Score mínimo para solicitar crédito: 550 pontos.

  - > **RN-U02** Bloco unitário de crédito: R$ 40 (indivisível).

  - > **RN-U03** Máximo de 10 blocos por solicitação (R$ 400 por operação).

  - > **RN-U04** Máximo de 1 solicitação ativa por usuário (nova solicitação bloqueada enquanto há crédito em aberto).

  - > **RN-U05** Parcelas: de 1 a 12 meses. Prazo máximo varia por faixa de score.

  - > **RN-U06** Taxa de juros determinada pelo portfólio matched (não pelo Usuário).

  - > **RN-U07** Atraso ≥ 3 dias corridos: notificação automática por push + email.

  - > **RN-U08** Atraso ≥ 15 dias: impacto negativo no NEXUS Score Bloco A.

  - > **RN-U09** Atraso ≥ 30 dias: suspensão do cartão (transações bloqueadas).

  - > **RN-U10** Atraso ≥ 60 dias: cobrança por empresa especializada + impacto crítico no score.

  - > **RN-U11** Amortizações aceitas: PIX, boleto bancário (D+2), débito automático (quando disponível).

  - > **RN-U12** Amortização antecipada total: permitida sem multa, com recálculo de juros.

  - > **RN-U13** KYC Nível 2 obrigatório para emissão do cartão.

  - > **RN-U14** Cartão Visa virtual: disponível em até 2 horas após aprovação do crédito.

  - > **RN-U15** Cartão físico (opcional): enviado pelos Correios em até 10 dias úteis.

## 6.3 Regras do MACRO HASH

  - > **RN-H01** Todo aporte, contrato e bloco de crédito DEVE ter um hash SHA-256 correspondente registrado.

  - > **RN-H02** O ledger é append-only: nenhum bloco pode ser editado ou excluído após registro.

  - > **RN-H03** Qualquer inconsistência de hash detectada pelo sistema gera alerta crítico para o time de compliance.

  - > **RN-H04** O hash raiz L1 é publicado publicamente em /ledger/root uma vez por dia (00:00 BRT).

  - > **RN-H05** Usuários podem verificar qualquer hash de suas transações via /ledger/verify/{hash} sem autenticação.

# 7\. Especificação de Telas — Campos e Componentes

## 7.1 Dashboard Aplicante — Componentes

| **Componente**           | **Conteúdo / Campos**                                                             |
| ------------------------ | --------------------------------------------------------------------------------- |
| Card Saldo Total         | Valor total investido (R$), variação vs. mês anterior (%), ícone tendência        |
| Card Retorno Mês         | Retorno líquido do mês corrente (R$), taxa efetiva (% a.m.), badge 'acima do CDI' |
| Card Próximo PIX         | Data e valor do próximo crédito PIX, botão 'Ver extrato'                          |
| Card NEXUS Score         | Score atual do Aplicante, barra de progresso, categoria (Bronze/Prata/Ouro)       |
| Gráfico Crescimento      | Linha temporal: capital total vs. retorno acumulado (últimos 12 meses)            |
| Tabela Portfólios Ativos | Portfólio, valor, taxa, prazo restante, retorno acumulado, ação (detalhe)         |
| Alertas/Notificações     | Últimas 5 notificações: PIX creditado, novo portfólio disponível, etc.            |
| Botão rápido: Investir   | CTA primário — abre modal de seleção de portfólio                                 |
| Botão rápido: Sacar      | CTA secundário — abre modal de saque PIX                                          |

## 7.2 Dashboard Usuário — Componentes

| **Componente**              | **Conteúdo / Campos**                                                   |
| --------------------------- | ----------------------------------------------------------------------- |
| Card Cartão Visa            | PAN mascarado, saldo disponível, limite total, status ativo/bloqueado   |
| Card NEXUS Score            | Score atual, faixa de cor (vermelho→verde), próxima faixa e o que falta |
| Card Próxima Parcela        | Valor, data de vencimento, conta bancária para PIX, botão 'Pagar'       |
| Card Crédito Disponível     | Limite adicional disponível (em blocos × R$40), botão 'Solicitar'       |
| Histórico de Solicitações   | Lista: data, valor, status (fila/aprovado/rejeitado), vertical de uso   |
| Extrato Resumido            | Últimas 5 transações do cartão: estabelecimento, valor, vertical, data  |
| Barra de Progresso Parcelas | Visual de parcelas pagas vs. abertas para cada crédito ativo            |
| Alerta Vencimento           | Banner amarelo/vermelho se parcela vence em ≤ 5 dias ou está em atraso  |

# 8\. Estados e Transições das Entidades

**Solicitação de Crédito**

| **Estado** | **Descrição**                                                          |
| ---------- | ---------------------------------------------------------------------- |
| queued     | Enfileirada aguardando worker                                          |
| processing | Worker processando: score check + matching                             |
| approved   | Crédito aprovado, aguardando emissão no cartão                         |
| rejected   | Reprovado: score insuficiente, capital indisponível ou limite atingido |
| disbursed  | Crédito creditado no cartão Visa — MACRO HASH L5 registrado            |

**Aporte (Investment)**

| **Estado**       | **Descrição**                                             |
| ---------------- | --------------------------------------------------------- |
| pending\_payment | PIX gerado, aguardando pagamento (expira em 30 min)       |
| active           | PIX confirmado, capital alocado no portfólio              |
| matured          | Prazo encerrado, capital + retorno liquidado ao Aplicante |
| withdrawn        | Resgate antecipado após 60 dias (taxa de saída aplicada)  |

**Parcela (Installment)**

| **Estado**   | **Descrição**                                |
| ------------ | -------------------------------------------- |
| upcoming     | Vencimento futuro — nenhuma ação necessária  |
| due\_today   | Vence hoje — notificação push enviada        |
| overdue\_3d  | 3 dias de atraso — notificação urgente       |
| overdue\_15d | 15 dias — impacto no score                   |
| overdue\_30d | 30 dias — cartão suspenso                    |
| paid         | Pago via PIX/boleto — amortização registrada |

**Cartão Visa**

| **Estado**  | **Descrição**                                               |
| ----------- | ----------------------------------------------------------- |
| not\_issued | Crédito aprovado mas cartão ainda não emitido               |
| active      | Cartão emitido e operacional                                |
| blocked     | Bloqueado temporariamente pelo usuário ou por inadimplência |
| cancelled   | Cancelado definitivamente (após 60+ dias inadimplência)     |

**KYC**

| **Estado** | **Descrição**                                            |
| ---------- | -------------------------------------------------------- |
| pending    | Cadastro criado, documentos não enviados                 |
| in\_review | Documentos enviados, análise em andamento                |
| approved   | KYC aprovado — nível correspondente liberado             |
| rejected   | Reprovado — motivo informado, reenvio permitido (máx 3×) |

# 9\. Integrações Externas

| **Parceiro**         | **Categoria**             | **Funcionalidade**                                                                                              | **Protocolo**           | **Criticidade** |
| -------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------- |
| Dock / BS2           | BIN Sponsor               | Emissão de cartão Visa/MC pré-pago, crédito de saldo (blocos R$40), bloqueio/desbloqueio, extrato de transações | REST API + Webhooks     | Alta            |
| PIX / BACEN DICT     | Infraestrutura Pagamentos | Recebimento de aportes dos Aplicantes, liquidação D+1 de retornos, amortizações dos Usuários                    | PSP parceiro + DICT API | Crítica         |
| Serasa Experian      | Bureau de Crédito         | Enriquecimento opcional do NEXUS Score (Bloco E). NÃO é gate — apenas sinal adicional.                          | REST API                | Média           |
| Open Finance BCB     | Dados Financeiros         | Consulta histórico bancário, pagamento de contas (Bloco C do score). Mediante consentimento do usuário.         | OAuth2 + REST           | Futura          |
| AWS S3 / GCS         | Armazenamento KYC         | Documentos de identidade e selfies criptografados em repouso (AES-256)                                          | SDK cloud               | Alta            |
| Twilio / SendGrid    | Comunicação               | SMS de verificação, emails transacionais (KYC, PIX, alertas de parcela)                                         | REST API                | Alta            |
| Firebase / OneSignal | Push Notifications        | Notificações push iOS/Android: crédito aprovado, PIX recebido, parcela vencendo                                 | SDK mobile              | Média           |

# 10\. Sistema de Notificações

O NEXUS opera um sistema de notificações multicanal (push, email, SMS, webhook) disparadas por eventos de negócio. Cada usuário pode configurar seus canais preferidos nas configurações de perfil.

| **Evento**              | **Destinatário**    | **Canal**          | **Mensagem Template**                                  |
| ----------------------- | ------------------- | ------------------ | ------------------------------------------------------ |
| kyc.approved            | Aplicante / Usuário | Push + Email       | KYC aprovado — sua conta está liberada                 |
| kyc.rejected            | Aplicante / Usuário | Push + Email       | KYC não aprovado — veja o motivo e reenvie             |
| investment.active       | Aplicante           | Push + Email       | Aporte de R$X confirmado no Portfólio Y                |
| investment.return\_paid | Aplicante           | Push + Email + SMS | R$X creditado via PIX — retorno de \[mês\]             |
| investment.matured      | Aplicante           | Push + Email       | Seu aporte venceu. Capital + retorno liquidados        |
| credit.queued           | Usuário             | Push               | Solicitação recebida. Posição na fila: \#N             |
| credit.approved         | Usuário             | Push + Email + SMS | Crédito R$X aprovado\\\! Disponível no seu cartão      |
| credit.rejected         | Usuário             | Push + Email       | Solicitação não aprovada. Motivo: \[razão\]            |
| card.transaction        | Usuário             | Push               | Compra R$X em \[estabelecimento\] · \[vertical\]       |
| installment.due\_soon   | Usuário             | Push + Email       | Parcela de R$X vence em 5 dias — \[data\]              |
| installment.overdue     | Usuário             | Push + Email + SMS | Parcela em atraso há \[N\] dias. Regularize já         |
| score.upgraded          | Ambos               | Push               | Seu NEXUS Score subiu para \[X\] pontos\\\! 🎉          |
| score.downgraded        | Ambos               | Push + Email       | Atenção: seu score caiu para \[X\]. Veja como melhorar |
| pix.received            | Aplicante           | Push               | PIX de R$X recebido na sua conta NEXUS                 |

# 11\. Painel Administrativo (Admin Panel)

O Admin Panel é um sistema interno de gestão, acessível apenas por colaboradores com roles autorizadas. Opera sobre a mesma API da plataforma com permissões elevadas.

  - > **Admin · Dashboard:** KPIs em tempo real: Aplicantes ativos, Usuários ativos, capital total, retorno médio, default rate geral, volume PIX do dia

  - > **Admin · Usuários:** Busca por CPF/email, ver perfil completo, histórico de score, forçar recálculo de score, suspender conta, ver todos os créditos

  - > **Admin · KYC Queue:** Fila de documentos aguardando revisão, aprovação/rejeição manual com motivo, histórico de decisões

  - > **Admin · Portfólios:** Criar/editar/pausar portfólios, definir taxas e limites, ver composição de contratos, ajustar parâmetros de risco

  - > **Admin · Créditos:** Ver todas as solicitações (qualquer status), forçar processamento manual, ver logs do worker Celery

  - > **Admin · MACRO HASH:** Explorador do ledger: busca por hash, ver árvore de blocos, exportar para auditoria, verificar integridade da cadeia

  - > **Admin · Compliance:** Relatórios BACEN, geração de arquivos para SCR (Sistema de Informações de Crédito), registros de auditoria

  - > **Admin · Financeiro:** Conciliação financeira, PIX pendentes, posições por portfólio, cálculo de provisão para inadimplência

  - > **Admin · Comunicações:** Envio de notificações manuais, templates de email, histórico de disparos

  - > **Admin · Configurações:** Parâmetros do sistema: taxas de saída, limites de crédito por faixa de score, thresholds do worker Celery

# 12\. Fluxo de Dados End-to-End

## 12.1 Fluxo: Aplicante investe → Usuário recebe crédito → Aplicante recebe retorno

| **\#** | **Ator**      | **Ação / Evento**                                                        | **Sistema/Serviço**   |
| ------ | ------------- | ------------------------------------------------------------------------ | --------------------- |
| 1      | Aplicante     | Realiza aporte de R$5.000 no Portfólio B (4,2% a.m., 6 meses)            | POST /investments     |
| 2      | Sistema       | Gera cobrança PIX; aguarda confirmação via webhook Dock                  | PIX QR Code           |
| 3      | PIX           | Pagamento confirmado → aporte ativado; MACRO HASH L2 registrado          | Webhook → MACRO HASH  |
| 4      | Worker Celery | Usuário A solicita 5 blocos (R$200). Score=720. Entra na fila FIFO.      | POST /credit/request  |
| 5      | Worker Celery | Worker consome fila. Score revalidado. Capital do Portfólio B reservado. | Celery task           |
| 6      | Sistema       | MACRO HASH L3 (Portfolio) + L4 (Contract) registrados sequencialmente.   | MACRO HASH L3+L4      |
| 7      | Dock API      | 5 × R$40 creditados no cartão Visa do Usuário A.                         | API Dock BIN          |
| 8      | Sistema       | MACRO HASH L5 registrado para cada bloco (5 registros distintos).        | MACRO HASH L5 ×5      |
| 9      | Usuário A     | Usa cartão: R$120 em supermercado (V001), R$80 em farmácia (V048).       | Transações rastreadas |
| 10     | Usuário A     | Paga parcela via PIX no vencimento. Score Bloco A melhora +2 pts.        | POST /payments/pix    |
| 11     | Sistema       | Amortização registrada. Retorno calculado e creditado ao Portfólio B.    | D+1 via PIX           |
| 12     | Aplicante     | Recebe R$210 via PIX (retorno bruto R$252 - IR R$42 = R$210 líquido).    | PIX D+1               |

# 13\. Roadmap de Implementação — 7 Camadas

| **Camada** | **Nome**                | **Entregáveis**                                                                                       | **Status**  |
| ---------- | ----------------------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| Camada 0   | Fundação Documental     | DEF (este documento), OpenAPI .yaml, modelo de score detalhado, arquitetura de informação completa    | ✅ Concluída |
| Camada 1   | Captação e Validação    | Pitch deck para investidores, modelo financeiro 36 meses (.xlsx), one-pager executivo                 | 🔄 Próxima   |
| Camada 2   | Especificação Técnica   | Schema PostgreSQL, ADR de arquitetura, fluxo de dados, contratos de integração (Dock, PIX, Serasa)    | 📋 Planejada |
| Camada 3   | Protótipo Navegável     | Todas as telas interativas com mock data — dashboard Aplicante/Usuário, fluxos de crédito e portfólio | 📋 Planejada |
| Camada 4   | Backend                 | FastAPI + Celery + Redis, MACRO HASH engine, score engine, integração PIX e Dock                      | 📋 Planejada |
| Camada 5   | Frontend                | Dashboard web (React), app mobile (React Native), notificações, relatório IR                          | 📋 Planejada |
| Camada 6   | QA, Compliance e Deploy | Testes automatizados, checklist regulatório BACEN, K8s, monitoramento, pentest                        | 📋 Planejada |

NEXUS P2P Credit Platform · DEF v1.0 · Confidencial · Abril 2026
