import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Ágora", layout="wide")

st.title("📊 Dashboard Sebrae - Ágora Pesquisas")

# ======= 🔗 Link direto do Google Sheets publicado =======
url_publica = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSEsiucgcv3oqHkQQk2hNtielDwa2o7YhbJczxC8JnjiSFA5APIaxE6FuD9_I8iRg/pub?output=csv"

# ======= 📥 Carregamento do CSV =======
try:
    modalidades = pd.read_csv(url_publica)

    # Debug visual (opcional)
    # st.write("Colunas carregadas:", modalidades.columns)
    # st.dataframe(modalidades.head())

    # Pega só as 3 primeiras colunas e renomeia
    modalidades = modalidades.iloc[:, :3]
    modalidades.columns = ["Modalidade", "Previsto", "Utilizado"]

    # ======= 🔁 Mapeamento dos nomes reais =======
    nomes_corretos = {
        "Modalidade 1": "Profundidade",
        "Modalidade 2": "Whatsapp",
        "Modalidade 3": "Telefone - voz",
        "Modalidade 4": "Omini - digital",
        "Modalidade 5": "Discussão de Grupo",
        "Modalidade 6": "Face a face 5’",
        "Modalidade 7": "Face a face 20’"
    }

    modalidades["Modalidade"] = modalidades["Modalidade"].replace(nomes_corretos)

    # ======= 📊 Geração do gráfico =======
    fig = px.bar(modalidades, 
                 x="Modalidade", 
                 y=["Previsto", "Utilizado"],
                 barmode="group",
                 title="Comparativo de Quantitativos por Modalidade")

    st.plotly_chart(fig, use_container_width=True)

    # ======= 📋 Tabela abaixo do gráfico =======
    st.subheader("📋 Tabela de Dados")
    st.dataframe(modalidades, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
