
import streamlit as st
import  pandas as pd
import yfinance as yf
from streamlit import columns


@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacao_acao = dados_acao.history(start = "2025-01-01", end = "2025-12-31")
    cotacao_acao = cotacao_acao["Close"]
    print(cotacao_acao)
    return cotacao_acao


acoes = ["MGLU3.SA", "PETR4.SA", "ITUB4.SA", "VALE3.SA"]
dados = carregar_dados(acoes)

st.write("""
 # Preço de Ações
 O gráfico abaixo representa o preço das ações ao longo dos anos.... 
 """)

st.sidebar.header("Filtros")

lista_selecao = st.sidebar.multiselect("Escolha as ações para visualizar: ",dados.columns)

data_ini =dados.index.min().to_pydatetime()
data_fin = dados.index.max().to_pydatetime()
intervalor= st.sidebar.slider("Selecione o periodo:" ,
                  min_value=data_ini,
                  max_value=data_fin,
                  value=(data_ini,data_fin)
                  )

if lista_selecao:
    dados = dados[lista_selecao]
    if len(lista_selecao) == 1:
        acao_unica = lista_selecao[0]
        dados = dados.rename(columns={acao_unica:"Close"})

dados = dados.loc[intervalor[0]:intervalor[1]]
st.line_chart(dados)