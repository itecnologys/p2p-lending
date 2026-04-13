# PROMPT MESTRE PARA IA GERADORA DE UI — P2P LENDING (STABLECOINS)

**Contexto da Aplicação:**
Plataforma de crédito P2P baseada em **Stablecoins** (descentralizada e alheia ao risco Bacen).
- **Aplicante (Investidor):** Fundo pulverizado (1 aplicação rateada para 250 Usuários). Rentabilidade de 3% a 5% ao mês. Recebe pagamentos vindos da taxa fixa de 6% aplicada sobre a fatura do cartão do Usuário. Contratos de no mínimo 18 meses com reinvestimento automático. Perfis compostos por "cestas de verticais" baseadas em consumo (saúde, seguros, mercados, etc.). 
- **Usuário (Tomador):** Recebe microcréditos em um cartão de crédito pré-pago (até R$ 2.500 no total), formado por múltiplos blocos de diferentes Aplicantes. Taxa do cartão rotativo (pago no fechamento) é de 6% fixo. Deve consumir 100% do limite no mês nas verticais de sua classificação. 

**Instruções para a IA Geradora de Telas (Ex: v0.dev, Cursor, Lovable):**
Crie componentes React/Tailwind em Dark Mode elegante (inspirado em Crypto/Web3, verde neon, roxo escuro e preto) para os cenários abaixo.

---

## TELA A-01: Dashboard do Aplicante (Investidor)
**Objetivo:** Mostrar clareza de onde está o dinheiro, como está performando e permitir escolha de portfólio.
- **Hero Metrics:** Valor Total em Stablecoin (USDC/USDT), Retorno Mensal Previsto, Risco Atual da Carteira, Tempo Restante no Contrato Base (Mín. 18 meses).
- **Composer de Verticais:** Interface de slider ou drag-and-drop para compor as cestas de consumo (Saúde, Transporte, Alimentação, Seguros). Nenhuma vertical pode ter 100% (min de 3 verticais obrigatórias). Mostrar como a mudança afeta os 3,5% a 5% de retorno.
- **Previsão de 60 Dias:** Gráfico de forecast com projeção de recebimento após carência de 60 dias da entrada na base.
- **Macro Hash Ledger:** Visualização "Deep Dive" Cripto. Um Macro Hash que se expande para centenas de Micro Hashes. Cada bloco mostra o status do recurso (Em Uso, Parado, Adimplente, Inadimplente). NUNCA exibir dados pessoais do tomador.
- **Contato:** Informações de contato e chat do "Gerente Executivo de Contas" que administra sua carteira.

## TELA U-01: App do Cartão do Usuário
**Objetivo:** Interface Mobile simples, empática e com visibilidade de controle.
- **Visão Principal:** Limite do Cartão (composto de microcréditos), Saldo da Fatura, Contador de dias até o Vencimento.
- **Taxa Clarificada:** "Use R$1.000, pague R$1.060 (Taxa de 6% fixa)". 
- **Histórico (até 5 anos):** Linha do tempo navegável com os gastos categorizados.
- **Educação e Negociação:** Chat integrado direto com o "Assistente Executivo" para educação financeira ou renegociação em caso de perigo de default. Opções para solicitar aumento de score/crédito baseado no histórico.

## TELA B-01: Dashboard VISÃO 360º (Executivo de Contas)
**Objetivo:** Ferramenta CRM para o Executivo de Contas validar e gerenciar a expansão na sua região.
- **Trava de Hash Ativa:** Banner indicando que o painel só exibe dados do hash regional (ex: São Paulo - Sul).
- **Métricas:** Volume em Merchants ativos, Rentabilidade da Carteira, Alertas de Inadimplência, Comissão de 3% (MDR) auferida na região com base de Lojas cadastradas.
- **Mapa de Merchants e Novos Usuários:** Base de credenciamento via mapa (pontos quentes e frios).

## TELA B-02: Dashboard BOARD 360º (Administração Geral)
**Objetivo:** Tela mestra com IA em tempo real.
- **Status Geral:** Fluxo das Stablecoins, Custódia global, Nível de Adimplência Médio vs Global por Executivo de Área.
- **Inteligência:** IA respondendo perguntas financeiras via Chat em linguagem natural. Exibição cruzada de Executivos, Diretores e Gerentes identificando quem tem as praças mais lucrativas.

---
**Instruções CSS/UI:**
Use fonte "Inter" ou "JetBrains Mono" (para hashes). Utilize Cards translúcidos (Glassmorphism leve), cores de alerta (Verde para retorno limpo, Vermelho para blocos não pagos). Priorizar a usabilidade do Investidor, inspirando extrema segurança e estabilidade, com toda blockchain operando nos bastidores (abstracted crypto layer).
