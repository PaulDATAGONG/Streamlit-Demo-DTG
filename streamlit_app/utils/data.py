from __future__ import annotations
from typing import Optional, Iterable
import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data(path: str = "streamlit_app/data/ventes.csv") -> pd.DataFrame:
    '''Charge le CSV et assure les bons types.'''
    # Lecture du fichier CSV avec conversion de la colonne "date"
    df = pd.read_csv(path, parse_dates=["date"])
    # Conversion de la colonne "categorie" en type category pour optimiser la mémoire
    df["categorie"] = df["categorie"].astype("category")
    return df

def filter_data(df: pd.DataFrame, categorie: Optional[Iterable[str]] = None, date_min=None, date_max=None) -> pd.DataFrame:
    '''Applique des filtres simples et retourne une copie filtrée.'''
    q = "True"
    # Filtre sur les catégories si précisé
    if categorie:
        cats = ",".join([f"'{c}'" for c in categorie])
        q += f" and categorie in [{cats}]"
    # Filtre sur la date minimale si précisé
    if date_min is not None:
        q += f" and date >= @date_min"
    # Filtre sur la date maximale si précisé
    if date_max is not None:
        q += f" and date <= @date_max"
    # Application du filtre avec .query()
    return df.query(q)
