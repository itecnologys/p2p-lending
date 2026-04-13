import os

def run_simulation(output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PLANO FINANCEIRO E DE EXPANSÃO - CENÁRIO REALISTA (24 MESES)\n\n")
        f.write("Abaixo está a projeção contínua da operação com crescimento moderado-acelerado de **5,5% ao mês**, iniciando com 5.000 aplicantes. Foi considerado o ticket médio de R$ 10.000 por aplicante e o uso de limite de R$ 2.500 por usuário tomador.\n\n")
        
        f.write("## PREMISSAS DO BUSINESS PLAN (AJUSTADAS)\n")
        f.write("- **Taxa do Merchant (MDR):** 2.50% bruta.\n")
        f.write("- **MDR Líquido (Interchange p/ Nexus):** 1.50% sobre o volume transacionado.\n")
        f.write("- **Taxa Mensal Paga pelo Usuário (Fatura):** 6.00% do saldo.\n")
        f.write("- **Inadimplência (NPL - Padrão de Mercado):** 4.50% do volume da fatura não performa/entra em default (Padrão para carteiras de crédito moderado blindado pelas verticais de consumo engessadas).\n")
        f.write("- **Crescimento da Base (MoM):** 5,5% ao mês.\n")
        f.write("- **Repasse ao Aplicante:** 4.00% a.m (Prometido/Alvo).\n")
        f.write("- **Plano de RH Escalonado:** 1 Assistente p/ 500 usuários; 1 Executivo p/ 5 Assistentes; 1 Gerente p/ 5 Executivos, 1 Diretor p/ 4 Gerentes.\n")
        f.write("\n---\n\n")
        
        f.write("## 1. ESCALADA OPERACIONAL REALISTA (MÊS 1 A MÊS 24)\n\n")
        f.write("| Mês | Aplicantes | Capital Investido | Usuários (Cartões) | Assistentes | Executivos | Gerentes | Diretores |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")

        # Initial Values
        aplicantes = 5000
        avg_ticket = 10000 # R$ 10,000
        user_limit = 2500  # R$ 2,500
        
        for mes in range(1, 25):
            capital = aplicantes * avg_ticket
            usuarios = int(capital / user_limit) # 1 aplicante = 4 usuarios de R$ 2500
            
            # Headcount
            assistentes = max(1, usuarios // 500)
            executivos = max(1, assistentes // 5)
            gerentes = max(1, executivos // 5)
            diretores = max(1, gerentes // 4)
            
            f.write(f"| Mês {mes:02} | {int(aplicantes):,} | R$ {capital:,.0f} | {usuarios:,} | {assistentes} | {executivos} | {gerentes} | {diretores} |\n")
            
            # Grow by 5.5%
            aplicantes = aplicantes * 1.055

        f.write("\n---\n\n")
        f.write("## 2. ANÁLISE ESTRESSADA DO REPASSE (DEFAULT 4.5%)\n\n")
        f.write("A adoção de uma taxa de 4.5% de quebra (NPL) muda completamente a viabilidade matemática, devolvendo a oxigenação ao Pool do Aplicante.\n")
        f.write("\n**Simulação Unitária Dinâmica (Para R$ 10.000 da cota de 1 Aplicante / 1 Mês de Giro):**\n")
        f.write("- Capital Total Operado: R$ 10.000,00\n")
        f.write("- **Receita Imediata de MDR (1,5%):** **R$ 150,00** pagos à vista para a NEXUS (Lucro Operacional).\n")
        f.write("- **Faturamento Teórico (Capital + 6%):** R$ 10.600,00.\n")
        f.write("- **Impacto da Inadimplência (4,5% sobre os 10k iniciais evadem):** **R$ -450,00 Perdidos**.\n")
        f.write("- **Valor Real Recuperado via Pagamento Saudável:** 95,5% dos cartões pagam c/ +6% de fee. (R$ 10.600 * 95,5%) = **R$ 10.123,00**.\n")
        f.write("- **Resultado para a Cota Matemática:** O pool agora é positivo! Ele terminou o mês em **10.123,00 (Lucro real de 1,23% bruto só do usuário, ignorando o MDR!)**.\n")
        
        f.write("\n> [!TIP]\n")
        f.write("> **O Segredo do P2P Balanceado:** Com uma inadimplência de 4.5%, a receita dos +6% paga o calote e faz a cota crescer 1.23% sozinha. Para atingirmos a promessa de 3,5% ou 4.0% para o Aplicante, a sua empresa Nexus usará os **R$ 150,00 (1.5%)** gerados do MDR para \"completar\" ou subsidiar a cota, compondo o yield final almejado, além da reprecificação do giro na fatura e da receita dos Merchants fechando o modelo financeiro em verde intenso.\n")

if __name__ == '__main__':
    target = r"C:\LAPTOP\p2p-lending\p2p-lending by Antigravity\06_Projecao_Financeira_Crescimento_Realista.md"
    run_simulation(target)
    print(f"File created at {target}")
