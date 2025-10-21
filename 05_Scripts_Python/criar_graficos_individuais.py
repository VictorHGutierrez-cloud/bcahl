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

print("🚀 CRIANDO GRÁFICOS INDIVIDUAIS...")

# 1. GRÁFICO DE CRESCIMENTO - BARRAS
print("📊 Criando Gráfico 1: Crescimento Financeiro...")
plt.figure(figsize=(12, 8))
categorias = dados['Categoria']
x = np.arange(len(categorias))
width = 0.35

bars1 = plt.bar(x - width/2, dados['2022'], width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = plt.bar(x + width/2, dados['2023'], width, label='2023', color='#4ECDC4', alpha=0.8)

plt.xlabel('Categorias', fontsize=12)
plt.ylabel('Valores (R$)', fontsize=12)
plt.title('CRESCIMENTO FINANCEIRO 2022 vs 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(x, categorias, rotation=45, ha='right')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars1:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('01_Crescimento_Financeiro_2022_vs_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. GRÁFICO DE CRESCIMENTO PERCENTUAL
print("📊 Criando Gráfico 2: Crescimento Percentual...")
plt.figure(figsize=(12, 8))
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = plt.bar(categorias, dados['Crescimento_%'], color=cores, alpha=0.8)
plt.xlabel('Categorias', fontsize=12)
plt.ylabel('Crescimento (%)', fontsize=12)
plt.title('CRESCIMENTO PERCENTUAL 2023 vs 2022\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('02_Crescimento_Percentual_2023_vs_2022.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. COMPOSIÇÃO DO ATIVO - PIZZA
print("📊 Criando Gráfico 3: Composição do Ativo...")
plt.figure(figsize=(10, 8))
cores_pizza = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = plt.pie(ativo_dados['Valor_2023'], labels=ativo_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza, startangle=90)
plt.title('COMPOSIÇÃO DO ATIVO 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

# Melhorar a aparência dos textos
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('03_Composicao_Ativo_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. COMPOSIÇÃO DO PASSIVO - PIZZA
print("📊 Criando Gráfico 4: Composição do Passivo...")
plt.figure(figsize=(10, 8))
cores_pizza2 = ['#45B7D1', '#96CEB4']
wedges, texts, autotexts = plt.pie(passivo_dados['Valor_2023'], labels=passivo_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza2, startangle=90)
plt.title('COMPOSIÇÃO DO PASSIVO 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('04_Composicao_Passivo_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. COMPOSIÇÃO DAS RECEITAS - PIZZA
print("📊 Criando Gráfico 5: Composição das Receitas...")
plt.figure(figsize=(10, 8))
cores_pizza3 = ['#FFEAA7', '#DDA0DD', '#98D8C8']
wedges, texts, autotexts = plt.pie(receitas_dados['Valor_2023'], labels=receitas_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza3, startangle=90)
plt.title('COMPOSIÇÃO DAS RECEITAS 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('05_Composicao_Receitas_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. COMPOSIÇÃO DAS DESPESAS - PIZZA
print("📊 Criando Gráfico 6: Composição das Despesas...")
plt.figure(figsize=(10, 8))
cores_pizza4 = ['#FF7675', '#74B9FF', '#A29BFE', '#FD79A8', '#FDCB6E']
wedges, texts, autotexts = plt.pie(despesas_dados['Valor_2023'], labels=despesas_dados['Categoria'], 
                                   autopct='%1.1f%%', colors=cores_pizza4, startangle=90)
plt.title('COMPOSIÇÃO DAS DESPESAS 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('06_Composicao_Despesas_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. DÍVIDAS POR CATEGORIA - BARRAS HORIZONTAIS
print("📊 Criando Gráfico 7: Dívidas por Categoria...")
plt.figure(figsize=(12, 8))
y_pos = np.arange(len(dividas_dados['Categoria']))
bars = plt.barh(y_pos, dividas_dados['Valor_2023'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
plt.yticks(y_pos, dividas_dados['Categoria'])
plt.xlabel('Valores (R$)', fontsize=12)
plt.title('DÍVIDAS POR CATEGORIA 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + width*0.01, bar.get_y() + bar.get_height()/2,
             f'R$ {width:,.0f}', ha='left', va='center', fontsize=11)

plt.tight_layout()
plt.savefig('07_Dividas_por_Categoria_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. ANÁLISE DE LIQUIDEZ - BARRAS
print("📊 Criando Gráfico 8: Análise de Liquidez...")
plt.figure(figsize=(12, 8))
cores_liquidez = ['#00B894', '#FDCB6E', '#E17055']
bars = plt.bar(liquidez_dados['Categoria'], liquidez_dados['Valor_2023'], color=cores_liquidez, alpha=0.8)
plt.xlabel('Categorias', fontsize=12)
plt.ylabel('Valores (R$)', fontsize=12)
plt.title('ANÁLISE DE LIQUIDEZ 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.savefig('08_Analise_Liquidez_2023.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. INDICADORES FINANCEIROS - BARRAS
print("📊 Criando Gráfico 9: Indicadores Financeiros...")
plt.figure(figsize=(12, 8))
indicadores = ['Margem Líquida', 'Margem Operacional', 'Crescimento Vendas', 'Crescimento Lucro']
valores_2023 = [3.2, 4.7, 154.2, 273.0]
valores_2022 = [2.1, 3.0, 0, 0]

x = np.arange(len(indicadores))
width = 0.35

bars1 = plt.bar(x - width/2, valores_2022, width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = plt.bar(x + width/2, valores_2023, width, label='2023', color='#4ECDC4', alpha=0.8)

plt.xlabel('Indicadores', fontsize=12)
plt.ylabel('Valores (%)', fontsize=12)
plt.title('INDICADORES FINANCEIROS\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(x, indicadores, rotation=45, ha='right')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('09_Indicadores_Financeiros.png', dpi=300, bbox_inches='tight')
plt.close()

# 10. EVOLUÇÃO DAS MARGENS - LINHA
print("📊 Criando Gráfico 10: Evolução das Margens...")
plt.figure(figsize=(12, 8))
anos = ['2022', '2023']
margem_liquida = [2.1, 3.2]
margem_operacional = [3.0, 4.7]

plt.plot(anos, margem_liquida, marker='o', linewidth=4, markersize=10, label='Margem Líquida', color='#FF6B6B')
plt.plot(anos, margem_operacional, marker='s', linewidth=4, markersize=10, label='Margem Operacional', color='#4ECDC4')
plt.xlabel('Anos', fontsize=12)
plt.ylabel('Margem (%)', fontsize=12)
plt.title('EVOLUÇÃO DAS MARGENS\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Adicionar valores nos pontos
for i, (liq, op) in enumerate(zip(margem_liquida, margem_operacional)):
    plt.text(i, liq + 0.1, f'{liq}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
    plt.text(i, op + 0.1, f'{op}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('10_Evolucao_Margens.png', dpi=300, bbox_inches='tight')
plt.close()

# 11. DASHBOARD EXECUTIVO - RESUMO
print("📊 Criando Gráfico 11: Dashboard Executivo...")
plt.figure(figsize=(14, 10))
plt.axis('off')

# Texto do dashboard
dashboard_text = """
DASHBOARD EXECUTIVO
AHL DESIGN & ENGINEERING SRL - 2023

📈 CRESCIMENTO EXCEPCIONAL
• Vendas: +154.2% (R$ 17.9M → R$ 45.7M)
• Lucro: +273.0% (R$ 389K → R$ 1.5M)
• Ativo: +46.2% (R$ 11.1M → R$ 16.2M)
• Capital Próprio: +36.1% (R$ 4.0M → R$ 5.5M)

💰 SITUAÇÃO FINANCEIRA
• Receita Total: R$ 45.7 MILHÕES
• Lucro Líquido: R$ 1.5 MILHÕES
• Caixa Disponível: R$ 5.5 MILHÕES
• Margem Líquida: 3.2% (vs 2.1% em 2022)

⚠️ PONTOS DE ATENÇÃO
• Dívidas: +52% (R$ 7.1M → R$ 10.7M)
• Contas a Receber: R$ 8.2 MILHÕES
• Impostos em Atraso: R$ 573 MIL
• Dívidas Sociais: R$ 581 MIL

✅ PONTOS FORTES
• Crescimento Explosivo e Sustentável
• Margens em Melhoria Constante
• Excelente Liquidez
• Investimento em Pessoas (+513%)
• Estrutura Financeira Sólida

🎯 RECOMENDAÇÕES
• Focar na Cobrança de Clientes
• Controlar Endividamento
• Regularizar Impostos
• Manter Crescimento Controlado
"""

plt.text(0.05, 0.95, dashboard_text, transform=plt.gca().transAxes, fontsize=14,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))

plt.tight_layout()
plt.savefig('11_Dashboard_Executivo.png', dpi=300, bbox_inches='tight')
plt.close()

# 12. ANÁLISE DE RISCOS - RADAR
print("📊 Criando Gráfico 12: Análise de Riscos...")
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')

# Dados para radar chart
categorias_risco = ['Liquidez', 'Endividamento', 'Crescimento', 'Rentabilidade', 'Estrutura']
valores_risco = [8, 4, 10, 9, 7]  # Valores de 1-10 (10 = melhor)

# Fechar o gráfico
valores_risco_fechado = valores_risco + [valores_risco[0]]

# Ângulos
angulos = np.linspace(0, 2 * np.pi, len(categorias_risco), endpoint=False)
angulos_fechado = np.concatenate((angulos, [angulos[0]]))

# Plotar
ax.plot(angulos_fechado, valores_risco_fechado, 'o-', linewidth=3, markersize=8, color='#FF6B6B')
ax.fill(angulos_fechado, valores_risco_fechado, alpha=0.25, color='#FF6B6B')
ax.set_xticks(angulos)
ax.set_xticklabels(categorias_risco, fontsize=12)
ax.set_ylim(0, 10)
ax.set_title('ANÁLISE DE RISCOS\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold', pad=30)
ax.grid(True)

# Adicionar valores nos pontos
for i, (angulo, valor) in enumerate(zip(angulos, valores_risco)):
    ax.text(angulo, valor + 0.5, f'{valor}', ha='center', va='center', fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('12_Analise_Riscos.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✅ TODOS OS GRÁFICOS INDIVIDUAIS CRIADOS COM SUCESSO!")
print("\n📁 ARQUIVOS GERADOS:")
print("01_Crescimento_Financeiro_2022_vs_2023.png")
print("02_Crescimento_Percentual_2023_vs_2022.png")
print("03_Composicao_Ativo_2023.png")
print("04_Composicao_Passivo_2023.png")
print("05_Composicao_Receitas_2023.png")
print("06_Composicao_Despesas_2023.png")
print("07_Dividas_por_Categoria_2023.png")
print("08_Analise_Liquidez_2023.png")
print("09_Indicadores_Financeiros.png")
print("10_Evolucao_Margens.png")
print("11_Dashboard_Executivo.png")
print("12_Analise_Riscos.png")
print("\n🎯 Agora você pode ver cada gráfico individualmente com melhor legibilidade!")
