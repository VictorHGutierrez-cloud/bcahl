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
    'Category': ['Net Sales', 'Net Profit', 'Total Assets', 'Shareholders Equity'],
    '2022': [17997408, 389321, 11089173, 4021326],
    '2023': [45746692, 1452605, 16215449, 5473932],
    'Growth_%': [154.2, 273.0, 46.2, 36.1]
}

# Dados de composição do ativo
ativo_dados = {
    'Category': ['Fixed Assets', 'Current Assets'],
    'Value_2023': [490691, 15724758],
    'Percentage': [3.0, 97.0]
}

# Dados de composição do passivo
passivo_dados = {
    'Category': ['Shareholders Equity', 'Debts'],
    'Value_2023': [5473932, 10741517],
    'Percentage': [33.8, 66.2]
}

# Dados de receitas
receitas_dados = {
    'Category': ['Services', 'Goods', 'Other'],
    'Value_2023': [45626970, 119722, 28099],
    'Percentage': [99.7, 0.3, 0.1]
}

# Dados de despesas
despesas_dados = {
    'Category': ['Salaries', 'External Purchases', 'Raw Materials', 'Corporate Charges', 'Other'],
    'Value_2023': [13156204, 17633929, 9170811, 2823344, 2900000],
    'Percentage': [30.6, 41.0, 21.3, 6.6, 6.7]
}

# Dados de dívidas
dividas_dados = {
    'Category': ['Suppliers', 'Tax/Social', 'Banking', 'Other'],
    'Value_2023': [6200374, 1155262, 848377, 1157727],
    'Percentage': [57.7, 10.8, 7.9, 10.8]
}

# Dados de liquidez
liquidez_dados = {
    'Category': ['Cash', 'Accounts Receivable', 'Other Current'],
    'Value_2023': [5462543, 8155227, 2106988],
    'Percentage': [34.7, 51.8, 13.4]
}

print("🚀 CREATING INDIVIDUAL CHARTS IN ENGLISH...")

# 1. FINANCIAL GROWTH CHART - BARS
print("📊 Creating Chart 1: Financial Growth...")
plt.figure(figsize=(12, 8))
categorias = dados['Category']
x = np.arange(len(categorias))
width = 0.35

bars1 = plt.bar(x - width/2, dados['2022'], width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = plt.bar(x + width/2, dados['2023'], width, label='2023', color='#4ECDC4', alpha=0.8)

plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values (R$)', fontsize=12)
plt.title('FINANCIAL GROWTH 2022 vs 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(x, categorias, rotation=45, ha='right')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add values on bars
for bar in bars1:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('01_Financial_Growth_2022_vs_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. PERCENTAGE GROWTH CHART
print("📊 Creating Chart 2: Percentage Growth...")
plt.figure(figsize=(12, 8))
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = plt.bar(categorias, dados['Growth_%'], color=cores, alpha=0.8)
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Growth (%)', fontsize=12)
plt.title('PERCENTAGE GROWTH 2023 vs 2022\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Add values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('02_Percentage_Growth_2023_vs_2022_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. ASSETS COMPOSITION - PIE
print("📊 Creating Chart 3: Assets Composition...")
plt.figure(figsize=(10, 8))
cores_pizza = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = plt.pie(ativo_dados['Value_2023'], labels=ativo_dados['Category'], 
                                   autopct='%1.1f%%', colors=cores_pizza, startangle=90)
plt.title('ASSETS COMPOSITION 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

# Improve text appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('03_Assets_Composition_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. LIABILITIES COMPOSITION - PIE
print("📊 Creating Chart 4: Liabilities Composition...")
plt.figure(figsize=(10, 8))
cores_pizza2 = ['#45B7D1', '#96CEB4']
wedges, texts, autotexts = plt.pie(passivo_dados['Value_2023'], labels=passivo_dados['Category'], 
                                   autopct='%1.1f%%', colors=cores_pizza2, startangle=90)
plt.title('LIABILITIES COMPOSITION 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('04_Liabilities_Composition_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. REVENUE COMPOSITION - PIE
print("📊 Creating Chart 5: Revenue Composition...")
plt.figure(figsize=(10, 8))
cores_pizza3 = ['#FFEAA7', '#DDA0DD', '#98D8C8']
wedges, texts, autotexts = plt.pie(receitas_dados['Value_2023'], labels=receitas_dados['Category'], 
                                   autopct='%1.1f%%', colors=cores_pizza3, startangle=90)
plt.title('REVENUE COMPOSITION 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('05_Revenue_Composition_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. EXPENSES COMPOSITION - PIE
print("📊 Creating Chart 6: Expenses Composition...")
plt.figure(figsize=(10, 8))
cores_pizza4 = ['#FF7675', '#74B9FF', '#A29BFE', '#FD79A8', '#FDCB6E']
wedges, texts, autotexts = plt.pie(despesas_dados['Value_2023'], labels=despesas_dados['Category'], 
                                   autopct='%1.1f%%', colors=cores_pizza4, startangle=90)
plt.title('EXPENSES COMPOSITION 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.tight_layout()
plt.savefig('06_Expenses_Composition_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. DEBTS BY CATEGORY - HORIZONTAL BARS
print("📊 Creating Chart 7: Debts by Category...")
plt.figure(figsize=(12, 8))
y_pos = np.arange(len(dividas_dados['Category']))
bars = plt.barh(y_pos, dividas_dados['Value_2023'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
plt.yticks(y_pos, dividas_dados['Category'])
plt.xlabel('Values (R$)', fontsize=12)
plt.title('DEBTS BY CATEGORY 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)

# Add values on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + width*0.01, bar.get_y() + bar.get_height()/2,
             f'R$ {width:,.0f}', ha='left', va='center', fontsize=11)

plt.tight_layout()
plt.savefig('07_Debts_by_Category_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. LIQUIDITY ANALYSIS - BARS
print("📊 Creating Chart 8: Liquidity Analysis...")
plt.figure(figsize=(12, 8))
cores_liquidez = ['#00B894', '#FDCB6E', '#E17055']
bars = plt.bar(liquidez_dados['Category'], liquidez_dados['Value_2023'], color=cores_liquidez, alpha=0.8)
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values (R$)', fontsize=12)
plt.title('LIQUIDITY ANALYSIS 2023\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)

# Add values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.savefig('08_Liquidity_Analysis_2023_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. FINANCIAL INDICATORS - BARS
print("📊 Creating Chart 9: Financial Indicators...")
plt.figure(figsize=(12, 8))
indicadores = ['Net Margin', 'Operating Margin', 'Sales Growth', 'Profit Growth']
valores_2023 = [3.2, 4.7, 154.2, 273.0]
valores_2022 = [2.1, 3.0, 0, 0]

x = np.arange(len(indicadores))
width = 0.35

bars1 = plt.bar(x - width/2, valores_2022, width, label='2022', color='#FF6B6B', alpha=0.8)
bars2 = plt.bar(x + width/2, valores_2023, width, label='2023', color='#4ECDC4', alpha=0.8)

plt.xlabel('Indicators', fontsize=12)
plt.ylabel('Values (%)', fontsize=12)
plt.title('FINANCIAL INDICATORS\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.xticks(x, indicadores, rotation=45, ha='right')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add values on bars
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
plt.savefig('09_Financial_Indicators_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 10. MARGINS EVOLUTION - LINE
print("📊 Creating Chart 10: Margins Evolution...")
plt.figure(figsize=(12, 8))
anos = ['2022', '2023']
margem_liquida = [2.1, 3.2]
margem_operacional = [3.0, 4.7]

plt.plot(anos, margem_liquida, marker='o', linewidth=4, markersize=10, label='Net Margin', color='#FF6B6B')
plt.plot(anos, margem_operacional, marker='s', linewidth=4, markersize=10, label='Operating Margin', color='#4ECDC4')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Margin (%)', fontsize=12)
plt.title('MARGINS EVOLUTION\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add values on points
for i, (liq, op) in enumerate(zip(margem_liquida, margem_operacional)):
    plt.text(i, liq + 0.1, f'{liq}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
    plt.text(i, op + 0.1, f'{op}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('10_Margins_Evolution_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 11. EXECUTIVE DASHBOARD - SUMMARY
print("📊 Creating Chart 11: Executive Dashboard...")
plt.figure(figsize=(14, 10))
plt.axis('off')

# Dashboard text
dashboard_text = """
EXECUTIVE DASHBOARD
AHL DESIGN & ENGINEERING SRL - 2023

📈 EXCEPTIONAL GROWTH
• Sales: +154.2% (R$ 17.9M → R$ 45.7M)
• Profit: +273.0% (R$ 389K → R$ 1.5M)
• Assets: +46.2% (R$ 11.1M → R$ 16.2M)
• Shareholders Equity: +36.1% (R$ 4.0M → R$ 5.5M)

💰 FINANCIAL SITUATION
• Total Revenue: R$ 45.7 MILLION
• Net Profit: R$ 1.5 MILLION
• Available Cash: R$ 5.5 MILLION
• Net Margin: 3.2% (vs 2.1% in 2022)

⚠️ ATTENTION POINTS
• Debts: +52% (R$ 7.1M → R$ 10.7M)
• Accounts Receivable: R$ 8.2 MILLION
• Overdue Taxes: R$ 573 THOUSAND
• Social Debts: R$ 581 THOUSAND

✅ STRENGTHS
• Explosive and Sustainable Growth
• Constantly Improving Margins
• Excellent Liquidity
• Investment in People (+513%)
• Solid Financial Structure

🎯 RECOMMENDATIONS
• Focus on Customer Collection
• Control Debt Levels
• Regularize Tax Situation
• Maintain Controlled Growth
"""

plt.text(0.05, 0.95, dashboard_text, transform=plt.gca().transAxes, fontsize=14,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))

plt.tight_layout()
plt.savefig('11_Executive_Dashboard_EN.png', dpi=300, bbox_inches='tight')
plt.close()

# 12. RISK ANALYSIS - RADAR
print("📊 Creating Chart 12: Risk Analysis...")
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')

# Data for radar chart
categorias_risco = ['Liquidity', 'Debt Level', 'Growth', 'Profitability', 'Structure']
valores_risco = [8, 4, 10, 9, 7]  # Values from 1-10 (10 = best)

# Close the chart
valores_risco_fechado = valores_risco + [valores_risco[0]]

# Angles
angulos = np.linspace(0, 2 * np.pi, len(categorias_risco), endpoint=False)
angulos_fechado = np.concatenate((angulos, [angulos[0]]))

# Plot
ax.plot(angulos_fechado, valores_risco_fechado, 'o-', linewidth=3, markersize=8, color='#FF6B6B')
ax.fill(angulos_fechado, valores_risco_fechado, alpha=0.25, color='#FF6B6B')
ax.set_xticks(angulos)
ax.set_xticklabels(categorias_risco, fontsize=12)
ax.set_ylim(0, 10)
ax.set_title('RISK ANALYSIS\nAHL Design & Engineering SRL', fontsize=16, fontweight='bold', pad=30)
ax.grid(True)

# Add values on points
for i, (angulo, valor) in enumerate(zip(angulos, valores_risco)):
    ax.text(angulo, valor + 0.5, f'{valor}', ha='center', va='center', fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('12_Risk_Analysis_EN.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✅ ALL INDIVIDUAL CHARTS IN ENGLISH CREATED SUCCESSFULLY!")
print("\n📁 FILES GENERATED:")
print("01_Financial_Growth_2022_vs_2023_EN.png")
print("02_Percentage_Growth_2023_vs_2022_EN.png")
print("03_Assets_Composition_2023_EN.png")
print("04_Liabilities_Composition_2023_EN.png")
print("05_Revenue_Composition_2023_EN.png")
print("06_Expenses_Composition_2023_EN.png")
print("07_Debts_by_Category_2023_EN.png")
print("08_Liquidity_Analysis_2023_EN.png")
print("09_Financial_Indicators_EN.png")
print("10_Margins_Evolution_EN.png")
print("11_Executive_Dashboard_EN.png")
print("12_Risk_Analysis_EN.png")
print("\n🎯 Now you have professional charts in English for international presentations!")
