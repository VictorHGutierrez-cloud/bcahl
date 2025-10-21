import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.patches import Wedge
import warnings
warnings.filterwarnings('ignore')

# Configuração do estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Dados financeiros da AHL Design & Engineering SRL
dados = {
    'Categoria': ['Vendas Líquidas', 'Lucro Líquido', 'Ativo Total', 'Capital Próprio'],
    '2022': [17997408, 389321, 11089173, 4021326],
    '2023': [45746692, 1452605, 16215449, 5473932],
    'Crescimento_%': [154.2, 273.0, 46.2, 36.1]
}

# Dados de composição do ativo
ativo_dados = {
    'Categoria': ['Ativo Imobilizado', 'Ativo Circulante'],
    'Valor_2023': [490691, 15724758],
    'Percentual': [3.0, 97.0]
}

# Dados de composição do passivo
passivo_dados = {
    'Categoria': ['Capital Próprio', 'Dívidas'],
    'Valor_2023': [5473932, 10741517],
    'Percentual': [33.8, 66.2]
}

# Dados de receitas
receitas_dados = {
    'Categoria': ['Serviços', 'Mercadorias', 'Outros'],
    'Valor_2023': [45626970, 119722, 28099],
    'Percentual': [99.7, 0.3, 0.1]
}

# Dados de despesas
despesas_dados = {
    'Categoria': ['Salários', 'Compras Externas', 'Matéria-Prima', 'Encargos', 'Outros'],
    'Valor_2023': [13156204, 17633929, 9170811, 2823344, 2900000],
    'Percentual': [30.6, 41.0, 21.3, 6.6, 6.7]
}

# Dados de dívidas
dividas_dados = {
    'Categoria': ['Fornecedores', 'Fiscais/Sociais', 'Bancárias', 'Outras'],
    'Valor_2023': [6200374, 1155262, 848377, 1157727],
    'Percentual': [57.7, 10.8, 7.9, 10.8]
}

# Dados de liquidez
liquidez_dados = {
    'Categoria': ['Caixa', 'Contas a Receber', 'Outros Circulantes'],
    'Valor_2023': [5462543, 8155227, 2106988],
    'Percentual': [34.7, 51.8, 13.4]
}

# Criar figura com subplots
fig = plt.figure(figsize=(20, 24))

# 1. GRÁFICO DE CRESCIMENTO - BARRAS
ax1 = plt.subplot(4, 3, 1)
categorias = dados['Categoria']
x = np.arange(len(categorias))
width = 0.35

bars1 = ax1.bar(x - width/2, dados['2022'], width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = ax1.bar(x + width/2, dados['2023'], width, label='2023', color='#4ECDC4', alpha=0.8)

ax1.set_xlabel('Categorias')
ax1.set_ylabel('Valores (R$)')
ax1.set_title('CRESCIMENTO FINANCEIRO 2022 vs 2023', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, rotation=45, ha='right')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=8)

for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=8)

# 2. GRÁFICO DE CRESCIMENTO PERCENTUAL
ax2 = plt.subplot(4, 3, 2)
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = ax2.bar(categorias, dados['Crescimento_%'], color=cores, alpha=0.8)
ax2.set_xlabel('Categorias')
ax2.set_ylabel('Crescimento (%)')
ax2.set_title('CRESCIMENTO PERCENTUAL 2023 vs 2022', fontsize=14, fontweight='bold')
ax2.set_xticklabels(categorias, rotation=45, ha='right')
ax2.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 3. COMPOSIÇÃO DO ATIVO - PIZZA
ax3 = plt.subplot(4, 3, 3)
cores_pizza = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = ax3.pie(ativo_dados['Valor_2023'], labels=ativo_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza, startangle=90)
ax3.set_title('COMPOSIÇÃO DO ATIVO 2023', fontsize=14, fontweight='bold')

# 4. COMPOSIÇÃO DO PASSIVO - PIZZA
ax4 = plt.subplot(4, 3, 4)
cores_pizza2 = ['#45B7D1', '#96CEB4']
wedges, texts, autotexts = ax4.pie(passivo_dados['Valor_2023'], labels=passivo_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza2, startangle=90)
ax4.set_title('COMPOSIÇÃO DO PASSIVO 2023', fontsize=14, fontweight='bold')

# 5. COMPOSIÇÃO DAS RECEITAS - PIZZA
ax5 = plt.subplot(4, 3, 5)
cores_pizza3 = ['#FFEAA7', '#DDA0DD', '#98D8C8']
wedges, texts, autotexts = ax5.pie(receitas_dados['Valor_2023'], labels=receitas_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza3, startangle=90)
ax5.set_title('COMPOSIÇÃO DAS RECEITAS 2023', fontsize=14, fontweight='bold')

# 6. COMPOSIÇÃO DAS DESPESAS - PIZZA
ax6 = plt.subplot(4, 3, 6)
cores_pizza4 = ['#FF7675', '#74B9FF', '#A29BFE', '#FD79A8', '#FDCB6E']
wedges, texts, autotexts = ax6.pie(despesas_dados['Valor_2023'], labels=despesas_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza4, startangle=90)
ax6.set_title('COMPOSIÇÃO DAS DESPESAS 2023', fontsize=14, fontweight='bold')

# 7. DÍVIDAS POR CATEGORIA - BARRAS HORIZONTAIS
ax7 = plt.subplot(4, 3, 7)
y_pos = np.arange(len(dividas_dados['Categoria']))
bars = ax7.barh(y_pos, dividas_dados['Valor_2023'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
ax7.set_yticks(y_pos)
ax7.set_yticklabels(dividas_dados['Categoria'])
ax7.set_xlabel('Valores (R$)')
ax7.set_title('DÍVIDAS POR CATEGORIA 2023', fontsize=14, fontweight='bold')
ax7.grid(True, alpha=0.3)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax7.text(width + width*0.01, bar.get_y() + bar.get_height()/2,
             f'R$ {width:,.0f}', ha='left', va='center', fontsize=9)

# 8. ANÁLISE DE LIQUIDEZ - BARRAS
ax8 = plt.subplot(4, 3, 8)
cores_liquidez = ['#00B894', '#FDCB6E', '#E17055']
bars = ax8.bar(liquidez_dados['Categoria'], liquidez_dados['Valor_2023'], color=cores_liquidez, alpha=0.8)
ax8.set_xlabel('Categorias')
ax8.set_ylabel('Valores (R$)')
ax8.set_title('ANÁLISE DE LIQUIDEZ 2023', fontsize=14, fontweight='bold')
ax8.set_xticklabels(liquidez_dados['Categoria'], rotation=45, ha='right')
ax8.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    ax8.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=9)

# 9. INDICADORES FINANCEIROS - BARRAS
ax9 = plt.subplot(4, 3, 9)
indicadores = ['Margem Líquida', 'Margem Operacional', 'Crescimento Vendas', 'Crescimento Lucro']
valores_2023 = [3.2, 4.7, 154.2, 273.0]
valores_2022 = [2.1, 3.0, 0, 0]

x = np.arange(len(indicadores))
width = 0.35

bars1 = ax9.bar(x - width/2, valores_2022, width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = ax9.bar(x + width/2, valores_2023, width, label='2023', color='#4ECDC4', alpha=0.8)

ax9.set_xlabel('Indicadores')
ax9.set_ylabel('Valores (%)')
ax9.set_title('INDICADORES FINANCEIROS', fontsize=14, fontweight='bold')
ax9.set_xticks(x)
ax9.set_xticklabels(indicadores, rotation=45, ha='right')
ax9.legend()
ax9.grid(True, alpha=0.3)

# 10. EVOLUÇÃO DAS MARGENS - LINHA
ax10 = plt.subplot(4, 3, 10)
anos = ['2022', '2023']
margem_liquida = [2.1, 3.2]
margem_operacional = [3.0, 4.7]

ax10.plot(anos, margem_liquida, marker='o', linewidth=3, label='Margem Líquida', color='#FF6B6B')
ax10.plot(anos, margem_operacional, marker='s', linewidth=3, label='Margem Operacional', color='#4ECDC4')
ax10.set_xlabel('Anos')
ax10.set_ylabel('Margem (%)')
ax10.set_title('EVOLUÇÃO DAS MARGENS', fontsize=14, fontweight='bold')
ax10.legend()
ax10.grid(True, alpha=0.3)

# Adicionar valores nos pontos
for i, (liq, op) in enumerate(zip(margem_liquida, margem_operacional)):
    ax10.text(i, liq + 0.1, f'{liq}%', ha='center', va='bottom', fontweight='bold')
    ax10.text(i, op + 0.1, f'{op}%', ha='center', va='bottom', fontweight='bold')

# 11. DASHBOARD EXECUTIVO - RESUMO
ax11 = plt.subplot(4, 3, 11)
ax11.axis('off')

# Texto do dashboard
dashboard_text = """
DASHBOARD EXECUTIVO
AHL DESIGN & ENGINEERING SRL

📈 CRESCIMENTO
• Vendas: +154.2%
• Lucro: +273.0%
• Ativo: +46.2%

💰 FINANCEIRO
• Receita: R$ 45.7M
• Lucro: R$ 1.5M
• Caixa: R$ 5.5M

⚠️ ATENÇÃO
• Dívidas: +52%
• Contas a Receber: R$ 8.2M
• Impostos em Atraso: R$ 573K

✅ PONTOS FORTES
• Margem Líquida: 3.2%
• Crescimento Sólido
• Boa Liquidez
"""

ax11.text(0.1, 0.9, dashboard_text, transform=ax11.transAxes, fontsize=12,
          verticalalignment='top', fontfamily='monospace',
          bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))

# 12. ANÁLISE DE RISCOS - RADAR
ax12 = plt.subplot(4, 3, 12, projection='polar')

# Dados para radar chart
categorias_risco = ['Liquidez', 'Endividamento', 'Crescimento', 'Rentabilidade', 'Estrutura']
valores_risco = [8, 4, 10, 9, 7]  # Valores de 1-10 (10 = melhor)

# Fechar o gráfico
valores_risco_fechado = valores_risco + [valores_risco[0]]

# Ângulos
angulos = np.linspace(0, 2 * np.pi, len(categorias_risco), endpoint=False)
angulos_fechado = np.concatenate((angulos, [angulos[0]]))

# Plotar
ax12.plot(angulos_fechado, valores_risco_fechado, 'o-', linewidth=2, color='#FF6B6B')
ax12.fill(angulos_fechado, valores_risco_fechado, alpha=0.25, color='#FF6B6B')
ax12.set_xticks(angulos)
ax12.set_xticklabels(categorias_risco)
ax12.set_ylim(0, 10)
ax12.set_title('ANÁLISE DE RISCOS', fontsize=14, fontweight='bold', pad=20)
ax12.grid(True)

# Ajustar layout
plt.tight_layout()
plt.suptitle('ANÁLISE FINANCEIRA COMPLETA - AHL DESIGN & ENGINEERING SRL 2023', 
             fontsize=16, fontweight='bold', y=0.98)

# Salvar gráfico
plt.savefig('Analise_Financeira_Completa_AHL_2023.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ GRÁFICOS CRIADOS COM SUCESSO!")
print("📁 Arquivo salvo como: Analise_Financeira_Completa_AHL_2023.png")
print("\n🎯 GRÁFICOS INCLUÍDOS:")
print("1. Crescimento Financeiro 2022 vs 2023")
print("2. Crescimento Percentual")
print("3. Composição do Ativo")
print("4. Composição do Passivo") 
print("5. Composição das Receitas")
print("6. Composição das Despesas")
print("7. Dívidas por Categoria")
print("8. Análise de Liquidez")
print("9. Indicadores Financeiros")
print("10. Evolução das Margens")
print("11. Dashboard Executivo")
print("12. Análise de Riscos")
