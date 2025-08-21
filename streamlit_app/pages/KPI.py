import streamlit as st
import pandas as pd
from utils.data import load_data, filter_data
from utils.charts import make_line

# Titre de la page
st.title("📈 KPI")

# Chargement des données
data = load_data()

# Affichage des indicateurs clés dans 3 colonnes
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total lignes", f"{len(data):,}".replace(",", " "))
with col2:
    st.metric("Dates", f"{data['date'].min().date()} → {data['date'].max().date()}")
with col3:
    st.metric("Catégories", ", ".join(map(str, data['categorie'].cat.categories)))

# Affichage de la tendance globale sous forme de courbe
st.subheader("Tendance globale")
st.plotly_chart(
    make_line(data, "date", "ventes", "categorie", "Ventes — global"),
    use_container_width=True
)
