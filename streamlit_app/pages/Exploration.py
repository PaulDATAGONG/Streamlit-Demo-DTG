import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data import load_data

# Titre de la page
st.title("🔎 Exploration")

# Chargement des données
df = load_data()

# Création de deux onglets pour différentes visualisations
tab1, tab2 = st.tabs(["Scatter", "Boxplot"])

with tab1:
    # Affichage d'un nuage de points (scatter plot)
    fig = px.scatter(df, x="date", y="ventes", color="categorie", title="Dispersion")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Affichage d'un boxplot par catégorie
    fig = px.box(df, x="categorie", y="ventes", title="Répartition par catégorie")
    st.plotly_chart(fig, use_container_width=True)
