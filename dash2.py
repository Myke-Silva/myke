import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


#======================================================
#FILTRO
#======================================================

st.header('Dashboard Analitico')

df = pd.read_csv('dados_dash.csv')

st.write(df.columns.tolist())

Genero = st.sidebar.selecbox('selecione o genero', df['Sexo'].unique())
df_filtrado = df[df['Sexo'] == Genero]
st.bar_chart(df_filtrado['produto'].value_counts())


graf_dados = df.groupby('loja_cidade')['produto_produto'].count().reset_index()
graf_produtos = df.groupby('produto_produto')['produto_valor'].count().reset_index()
graf_faturamento_cidade = df.groupby('loja_cidade')['produto_valor'].count().reset_index()
graf_faturamento_produto = df.groupby('produto_produto')['produto_valor'].count().reset_index()

#======================================================
#DADOS PARA GRAFICO
#======================================================

st.header('Dados')
df_pivot = graf_dados.pivot(index='loja_cidade',columns='produto_produto',values='produto_produto')

st.bar_chart(df_pivot)

st.header('PRODUTOS')
df_pivot = graf_produtos.pivot(index='produto_produto',columns='produto_valor',values='produto_valor')

st.bar_chart(df_pivot)

st.header('FATURAMENTO CIDADE')
df_pivot = graf_faturamento_cidade.pivot(index='loja_cidade',columns='produto_valor',values='produto_valor')

st.bar_chart(df_pivot)

st.header('FATURAMENTO PRODUTO')
df_pivot = graf_faturamento_produto.pivot(index='produto_produto',columns='produto_valor',values='produto_valor')

st.bar_chart(df_pivot)