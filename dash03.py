import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Cria um cabeçalho
st.header('Dashboard analítico')

#Importa a base de dados
df = pd.read_csv('dados_dash.csv')


#==========================
#         SIDEBAR
#==========================

#Ordena em ordem alfabética, converte a coluna para string 
#e retorna valores únicos 

#clientes = sorted(df['cliente_nome'].astype(str).unique())

#Remove os nulos
clientes = sorted(df['cliente_nome'].fillna('').astype(str).unique())

st.sidebar.title('Filtros')

#Filtros por cliente
#cliente_selecionado = st.sidebar.multiselect(
    #label='Selecione os clientes',
    #options = clientes, 
    #default = clientes, #começa com o nome de todos os clientes
#)

#Aplicar o filtro
#if cliente_selecionado:
    #df_filtrado = df[df['cliente_nome'].astype(str).isin(cliente_selecionado)].copy()
#else:
    #df_filtrado = df.copy()


#Mostrar o df no Dash Online
#st.dataframe(df)


#==========================
#          KPIs
#==========================

# KPIs (Key Performance Indicators), ou Indicadores-Chave de Desempenho, são métricas 
# quantitativas essenciais que medem o sucesso de processos, projetos ou estratégias de uma empresa. 
# Eles servem para acompanhar se os objetivos de negócio estão sendo alcançados, 
# permitindo uma tomada de decisão mais rápida e assertiva com base em dados, não em suposições. 


faturamento_total = df['produto_valor'].sum()
media_total = df['produto_valor'].mean()
maximo = df['produto_valor'].max()
minimo = df['produto_valor'].min()

col1, col2 = st.columns(2) 
col3, col4 = st.columns(2)

with col1: 
    st.metric('Total Faturado', f'R$ {faturamento_total:,.2f}')

with col2:
    st.metric('Média Total', f'R$ {media_total:,.2f}')

with col3:
    st.metric('Máximo', f'R$ {maximo:,.2f}') 

with col4:
    st.metric('Mínimo', f'R$ {minimo:,.2f}') 

#==========================
#  DADOS PARA OS GRÁFICOS
#==========================

graf_dados = df.groupby('loja_cidade')['produto_produto'].count()
graf_produto = df.groupby('produto_produto')['produto_valor'].count()
graf_faturamento_cidade = df.groupby('loja_cidade')['produto_valor'].sum()
graf_faturamento_produto = df.groupby('produto_produto')['produto_valor'].sum()

#Para visualizar as variáveis no dash on line (os groupby):
#st.dataframe(nome_da_variável)


#==========================
#  GRÁFICOS MATPLOT (2X2)
#==========================

fig = plt.figure(figsize=(10,7))

#Gráfico 1
plt.subplot(2,2,1)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por loja')
plt.xticks(rotation=45)

#Gráfico 2
plt.subplot(2,2,2)
plt.bar(graf_faturamento_cidade.index, graf_faturamento_cidade.values)
plt.title('Faturamento por loja')
plt.xticks(rotation=45)

#Gráfico 3
plt.subplot(2,2,3)
plt.bar(graf_produto.index, graf_produto.values)
plt.title('Vendas por produto')
plt.xticks(rotation=45)

#Gráfico 4
plt.subplot(2,2,4)
plt.bar(graf_faturamento_produto.index, graf_faturamento_produto.values)
plt.title('Faturamento por produto')
plt.xticks(rotation=45)

#Organiza todos os gráficos no dashboard online
plt.tight_layout()

#Visualizar os gráficos no dashboard online
st.pyplot(fig)


