import streamlit as st
import pandas as pd
from utils.data import load_data, filter_data
from utils.charts import make_line, make_bar

# Titre du dashboard
st.title("📊 Dashboard")

# Chargement des données
df = load_data()

# Sélecteur de catégorie (filtre interactif)
cat = st.selectbox("Catégorie", options=sorted(list(df["categorie"].cat.categories)))

# Filtrage des données selon la catégorie sélectionnée
df_cat = filter_data(df, categorie=[cat])

# Affichage des indicateurs clés (KPI)
col1, col2 = st.columns(2)
with col1:
    st.metric("Moyenne ventes", f"{df_cat['ventes'].mean():.1f}")
with col2:
    st.metric("Max ventes", f"{df_cat['ventes'].max():.0f}")

# Affichage du graphique de tendance
st.subheader("Tendance (catégorie)")
st.plotly_chart(make_line(df_cat, "date", "ventes", title=f"Tendance — {cat}"), use_container_width=True)

# Affichage du tableau filtré
st.subheader("Table filtrée")
st.dataframe(df_cat, use_container_width=True)

# Bouton de téléchargement du CSV filtré
csv = df_cat.to_csv(index=False).encode("utf-8")
st.download_button("Télécharger CSV filtré", data=csv, file_name=f"ventes_{cat}.csv", mime="text/csv")
