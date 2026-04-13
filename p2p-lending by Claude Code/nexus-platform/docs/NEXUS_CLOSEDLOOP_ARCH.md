# 🏗️ NEXUS: Arquitetura de Rede Proprietária (Closed-Loop)

Este documento detalha o modelo de **Circuito Fechado** da NEXUS, onde a plataforma atua como emissora, adquirente e processadora final, eliminando intermediários como Visa/Mastercard e adquirentes tradicionais.

---

## 1. Visão Geral do Fluxo Closed-Loop

Diferente do modelo tradicional (Open-Loop), onde o cartão pode ser passado em qualquer maquininha, no modelo **NEXUS Closed-Loop**, a transação ocorre exclusivamente entre o App do Usuário e o App/Terminal do Lojista Credenciado.

### Pilares da Operação:
1. **NEXUS Merchant App:** O celular do lojista atua como o terminal de captura.
2. **NEXUS User App:** O celular do tomador atua como o instrumento de pagamento (via QR ou NFC).
3. **Smart Contracts (USDC/Alchemy):** A liquidação da transação ocorre on-chain, transferindo frações de stablecoin do cofre do investidor para a sub-conta do lojista.

---

## 2. Métodos de Captura (O "Caminhão" Proprietário)

### A) QR Code Estático/Dinâmico
1. O lojista gera uma cobrança no App.
2. O usuário escaneia o código.
3. O Backend valida o saldo de crédito (Lending Pool) e autoriza o "Push" de USDC.

### B) Tap-on-Phone (NFC)
1. O lojista digita o valor.
2. O usuário aproxima seu celular (ou cartão Private Label NFC).
3. A comunicação NFC dispara o Webhook de autorização para o Ledger L5.

---

## 3. Comprovantes e Recibos Digitais (Smart Receipts)

Para eliminar o custo de bobinas de papel e hardware de impressão:
* **Fluxo Automatizado:** Assim que a transação é confirmada on-chain, o backend aciona a API de mensageria (WhatsApp/Email).
* **Conteúdo:** O recibo contém o ID da transação no **MACRO HASH (L5)**, garantindo imutabilidade e prova de pagamento para ambas as partes.

---

## 4. Ciclo de Liquidação para o Lojista (Cashout)

O lojista acumula saldo em USDC (indexado a BRL) dentro da plataforma.
1. **Solicitação de Saque:** O lojista clica em "Resgatar Vendas".
2. **Conversão (Off-Ramp):** A NEXUS aciona o parceiro de liquidez (ex: Liqi) para converter o saldo do FIDC em Reais.
3. **Distribuição:** A conta liquidante da NEXUS (FitBank/BS2) efetua um PIX para a chave do lojista.
4. **Prazos:** Suporte a D+0 (conforme saldo de reserva) ou D+1 padrão.

---

## 5. Comparativo de Margem (Unit Economics)

| Elemento | Modelo VISA (Antigo) | Modelo Proprietário (Novo) |
| :--- | :--- | :--- |
| **TIC (Intercâmbio)** | 0.70% (Teto Bacen) | 0.00% |
| **MDR (Taxa Lojista)** | ~2.00% | **2.50% (Definido pela NEXUS)** |
| **Repasse Terceiros** | Visa/Dock/Cielo | Apenas Parceiro de PIX/Cashout |
| **Margem NEXUS** | **~0.49%** | **~2.00% a 2.30%** |

---

## 6. Blindagem Jurídica e Regulatória

* **Arranjo Fechado:** Enquadrado na Resolução BCB nº 150 como não integrante do SPB (dispensa de autorização prévia por volume e propósito limitado).
* **FIDC Próprio:** Toda a carteira de crédito e recebíveis de lojistas circulam dentro do fundo, garantindo a separação patrimonial e a legalidade dos juros cobrados.

---
*Documento de Trabalho Alternativo - Versão 1.0*
