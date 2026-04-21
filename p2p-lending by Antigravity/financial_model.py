import os

def run_simulation(output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# PLANO FINANCEIRO E DE EXPANSÃO (24 MESES) - NEXUS\n\n")
        f.write("Abaixo está a projeção contínua da operação com crescimento de 25% ao mês, iniciando com 5.000 aplicantes. Foi considerado um ticket médio de R$ 10.000 por aplicante e um limite utilizado de R$ 2.500 por usuário tomador.\n\n")
        
        f.write("## PREMISSAS DO BUSINESS PLAN\n")
        f.write("- **Taxa do Merchant (MDR):** 2.50% bruta.\n")
        f.write("- **Taxa da Adquirente/Dock:** 1.00%.\n")
        f.write("- **MDR Líquido (Interchange p/ Nexus):** 1.50% sobre o volume transacionado.\n")
        f.write("- **Taxa Mensal Paga pelo Usuário (Fatura):** 6.00% do saldo.\n")
        f.write("- **Inadimplência (NPL):** 11.00% do volume na fatura não performa no mês.\n")
        f.write("- **Repasse ao Aplicante:** 4.00% bruto prometido (reinvestido/composto).\n")
        f.write("- **Custo de Emissão de Cartão:** R$ 5,00 por novo cartão virtual/físico emitido.\n")
        f.write("- **Plano de RH Escalonado:** 1 Assistente para cada 500 contas ativas; 1 Executivo de Contato para 5 Assistentes; 1 Gerente para 5 Executivos, 1 Diretor para 4 Gerentes.\n")
        f.write("\n---\n\n")
        
        f.write("## 1. ESCALADA OPERACIONAL (MÊS 1 A MÊS 24)\n\n")
        f.write("| Mês | Aplicantes | Capital Investido | Usuários (Cartões) | Assistentes | Executivos | Gerentes | Diretores |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")

        # Initial Values
        aplicantes = 5000
        avg_ticket = 10000 # R$ 10,000
        user_limit = 2500  # R$ 2,500
        
        users_in_base = 0
        
        for mes in range(1, 25):
            capital = aplicantes * avg_ticket
            usuarios = int(capital / user_limit) # 1 aplicante = 4 usuarios de R$ 2500
            
            # Headcount
            assistentes = max(1, usuarios // 500)
            executivos = max(1, assistentes // 5)
            gerentes = max(1, executivos // 5)
            diretores = max(1, gerentes // 4)
            
            f.write(f"| Mês {mes:02} | {int(aplicantes):,} | R$ {capital:,.0f} | {usuarios:,} | {assistentes} | {executivos} | {gerentes} | {diretores} |\n")
            
            # Grow by 25%
            aplicantes = aplicantes * 1.25

        f.write("\n---\n\n")
        f.write("## 2. ANÁLISE ESTRESSADA DO REPASSE E INADIMPLÊNCIA (PER MONTH MODEL)\n\n")
        f.write("O ponto mais sensível de uma operação real é que a **Inadimplência de 11%** (a perda de capital rotativo) tem que ser mitigada pela taxa da fatura (6%) e pelo volume de novas emissões e giro.\n")
        f.write("\n**Simulação Unitária Dinâmica (Para R$ 10.000 da cota de 1 Aplicante):**\n")
        f.write("- A cota de R$ 10.000 fomenta saques de R$ 10.000 no crédito em diversos merchants.\n")
        f.write("- **Receita Imediata (Interchange na emissão Dock):** 1,5% de R$ 10.000 = **R$ 150,00** pagos à vista para a operação Nexus.\n")
        f.write("- **Faturamento Esperado no Vencimento (+6%):** R$ 10.600,00.\n")
        f.write("- **Impacto da Inadimplência Absoluta (11% quebra de safra no mês):** 11% de R$ 10.000 = **R$ 1.100,00 Perdidos**.\n")
        f.write("- **Valor Real Recuperado:** 89% dos usuários pagam R$ 10.600 (proporcional) = **R$ 9.434,00**.\n")
        
        f.write("\n> [!CAUTION]\n")
        f.write("> Atenção Analítica: Se 11% do fundo evaporar ao mês, o Aplicante terá um rendimento negativo! O modelo matemático só para de pé se a inadimplência for mitigada ou por **Recuperação de Crédito via Assessoria** (reciclando o default para NPL de 3% a 5% max) OU o repasse dos 6% e 1.5% das margens cruzadas funcionarem como fundo garantidor amortecendo o golpe (A Nexus doando o spread do MDR). O cenário de 11% de default mensal esmaga lucros de até 6% a.m.\n")

        f.write("\n### DRE e Caixa Operacional (Cenário do Mês 12)\n")
        aplicantes_12 = 5000 * (1.25**11)
        capital_12 = aplicantes_12 * 10000
        usuarios_12 = capital_12 / 2500
        
        mdr_revenue_12 = capital_12 * 0.015
        maintenance_cost_12 = usuarios_12 * 1.50 # estimate R$ 1.5 per card maintenance
        card_issuing_12 = (usuarios_12 * 0.25) * 5.0 # assume 25% new emission at 25% growth
        
        salarios_assistentes = (usuarios_12 // 500) * 4000
        salarios_executivos = ((usuarios_12 // 500) // 5) * 10000
        salarios_gerentes = (((usuarios_12 // 500) // 5) // 5) * 25000
        total_salarios = salarios_assistentes + salarios_executivos + salarios_gerentes
        
        f.write(f"- Volume Movimentado (Capital): R$ {capital_12:,.2f}\n")
        f.write(f"- Cartões Ativos (Usuários): {int(usuarios_12):,}\n")
        f.write(f"- Receita MDR Bruta (1.5%): R$ {mdr_revenue_12:,.2f}\n")
        f.write(f"- Custo de Manutenção Conta (R$ 1,50/cartão): R$ {maintenance_cost_12:,.2f}\n")
        f.write(f"- Custo de Novas Emissões (R$ 5,00/novo_cartão): R$ {card_issuing_12:,.2f}\n")
        f.write(f"- Custo Salarial RH Vendas/Assistentes: R$ {total_salarios:,.2f}\n")
        lucro_operacional = mdr_revenue_12 - maintenance_cost_12 - card_issuing_12 - total_salarios
        f.write(f"- **Lucro Operacional Base (Apenas do Interchange) ANTES do Repasse de NPL:** R$ {lucro_operacional:,.2f}\n")

if __name__ == '__main__':
    target = r"C:\LAPTOP\p2p-lending\p2p-lending by Antigravity\05_Projecao_Financeira_24_Meses.md"
    run_simulation(target)
    print(f"File created at {target}")
