# Mapeamento de Contas Francesas para Factorial

## Resumo Executivo

Criado mapeamento completo das contas do balanço francês da AHL Design & Engineering SRL para o formato de importação da Factorial, com **59 contas** organizadas por categoria.

## Estrutura do Mapeamento

### 📊 Distribuição por Tipo de Conta

| Tipo | Quantidade | Descrição |
|------|------------|-----------|
| **Income** | 6 | Receitas (Vendas, Serviços, Comissões, etc.) |
| **Expense** | 25 | Despesas Operacionais e Administrativas |
| **Bank** | 4 | Contas Bancárias e Caixa |
| **Current Asset** | 8 | Ativo Circulante (Estoques, Clientes, etc.) |
| **Current Liability** | 7 | Passivo Circulante (Fornecedores, Impostos, etc.) |
| **Equity** | 4 | Patrimônio Líquido (Capital, Reservas, etc.) |
| **Non-current Asset** | 5 | Ativo Não Circulante (Imobilizações) |

### 🎯 Principais Categorias Mapeadas

#### **RECEITAS (Income)**
- Ventes de marchandises (Vendas de mercadorias)
- Prestations de services (Prestações de serviços)
- Revenus de locations (Receitas de aluguéis)
- Revenus de commissions (Receitas de comissões)

#### **DESPESAS (Expense)**
- Achats de marchandises (Compras de mercadorias)
- Salaires et traitements (Salários e tratamentos)
- Charges sociales (Encargos sociais)
- Locations et canons (Aluguéis e taxas)
- Transports (Transportes)
- Services bancaires (Serviços bancários)

#### **ATIVO CIRCULANTE (Current Asset)**
- Clients et comptes rattachés (Clientes e contas relacionadas)
- Disponibilités (Disponibilidades/Tesouraria)
- Stocks de matières premières (Estoques de matérias-primas)

#### **PASSIVO CIRCULANTE (Current Liability)**
- Dettes fournisseurs (Dívidas com fornecedores)
- Dettes fiscales et sociales (Dívidas fiscais e sociais)
- Emprunts bancaires (Empréstimos bancários)

#### **PATRIMÔNIO LÍQUIDO (Equity)**
- Capital social (Capital social)
- Réserves (Reservas)
- Résultat de l'exercice (Resultado do exercício)

## 📁 Arquivos Gerados

1. **`Mapeamento_Contas_Francesas_Factorial.csv`** - Tabela de mapeamento detalhada
2. **`Chart_of_Accounts_French_Import.xlsx`** - Arquivo de importação simples
3. **`Chart_of_Accounts_French_Import_Complete.xlsx`** - Arquivo completo com todas as abas

## 🔧 Como Usar

1. **Importar na Factorial**: Use o arquivo `Chart_of_Accounts_French_Import_Complete.xlsx`
2. **Verificar Mapeamento**: Consulte o arquivo CSV para detalhes de cada conta
3. **Ajustar se Necessário**: Modifique os nomes em francês conforme necessário

## ✅ Benefícios

- **Padronização**: Contas organizadas no padrão francês
- **Compatibilidade**: Formato exato da Factorial
- **Completude**: Cobertura de todas as categorias do balanço
- **Rastreabilidade**: Identificadores únicos para cada conta
- **Flexibilidade**: Fácil modificação e manutenção

## 📋 Próximos Passos

1. Revisar os nomes em francês com especialista
2. Testar importação na Factorial
3. Ajustar códigos de conta se necessário
4. Configurar saldos iniciais
5. Treinar equipe no novo plano de contas
