import streamlit as st
import pandas as pd
import plotly.express as px

# Link público direto para CSV
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSEsiucgcv3oqHkQQk2hNtielDwa2o7YhbJczxC8JnjiSFA5APIaxE6FuD9_I8iRg/pub?output=csv"

# Carregar os dados
modalidades = pd.read_csv(sheet_url)

# Se necessário renomear colunas
modalidades.columns = ["Modalidade", "Previsto", "Utilizado"]

# KPIs
valor_faturar = modalidades["Previsto"].sum()
valor_pago = modalidades["Utilizado"].sum()  # ou outra lógica
total_previsto = modalidades["Previsto"].sum()
total_utilizado = modalidades["Utilizado"].sum()
percentual_execucao = total_utilizado / total_previsto * 100

st.title("📊 Dashboard Ágora Pesquisas – Projeto Sebrae SP 2025")
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Valor a Faturar", f"R$ {valor_faturar:,.2f}")
col2.metric("✅ Valor Pago", f"R$ {valor_pago:,.2f}")
col3.metric("📦 Utilizado", f"{total_utilizado} itens")
col4.metric("📈 Execução", f"{percentual_execucao:.1f} %")

st.subheader("📌 Utilização por Modalidade")
fig = px.bar(modalidades, x="Modalidade", y=["Previsto", "Utilizado"],
             barmode="group", height=400, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)

st.subheader("📋 Detalhamento")
st.dataframe(modalidades)
