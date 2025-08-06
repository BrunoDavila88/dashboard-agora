
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
modalidades = pd.read_csv("modalidades.csv")

# Títulos e KPIs
st.title("📊 Dashboard Ágora Pesquisas – Projeto Sebrae SP 2025")

valor_faturar = 99549.15
valor_pago = 0
total_previsto = modalidades["Previsto"].sum()
total_utilizado = modalidades["Utilizado"].sum()
percentual_execucao = (total_utilizado / total_previsto) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Valor a Faturar", f"R$ {valor_faturar:,.2f}")
col2.metric("✅ Valor Pago", f"R$ {valor_pago:,.2f}")
col3.metric("📦 Utilizado", f"{total_utilizado} itens")
col4.metric("📈 Execução", f"{percentual_execucao:.1f} %")

# Gráfico de barras
st.subheader("📌 Utilização por Modalidade")
fig = px.bar(modalidades, x="Modalidade", y=["Previsto", "Utilizado"],
             barmode="group", height=400, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)

# Tabela
st.subheader("📋 Detalhamento")
st.dataframe(modalidades)
