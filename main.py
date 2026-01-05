
import streamlit as st
import  pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacao_acao = dados_acao.history(start = "2025-01-01", end = "2025-12-31")
    cotacao_acao = cotacao_acao[["Close"]]
    return cotacao_acao

dados = carregar_dados("ITUB4.SA")

st.write("""
 # Preço de Ações
 O gráfico abaixo representa o preço das ações do Itaú ao longo dos anos.... 
 """)

st.line_chart(dados)