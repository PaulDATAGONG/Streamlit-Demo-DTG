import plotly.express as px

# Définition du thème graphique commun
TEMPLATE = "plotly_white"

def _apply_common(fig, title: str):
    # Applique le template, le titre et les marges à la figure
    fig.update_layout(template=TEMPLATE, title=title, margin=dict(l=40, r=20, t=60, b=40))
    return fig

def make_line(df, x, y, color=None, title="Courbe"):
    # Crée un graphique en courbe avec Plotly Express
    fig = px.line(df, x=x, y=y, color=color)
    # Applique les paramètres communs
    return _apply_common(fig, title)

def make_bar(df, x, y, color=None, title="Barres"):
    # Crée un graphique en barres avec Plotly Express
    fig = px.bar(df, x=x, y=y, color=color, barmode="group")
    # Applique les paramètres communs
    return _apply_common(fig, title)
