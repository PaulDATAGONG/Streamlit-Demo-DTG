# 📊 Application Streamlit + Plotly — Capstone Data Visualization

Bienvenue dans ce projet de Data Visualization interactif, construit avec **Streamlit** et **Plotly**. Cette application a pour objectif de vous offrir une expérience complète de visualisation de données, tout en illustrant les meilleures pratiques de structuration, de packaging et de documentation d’un projet professionnel.

## 🚀 Présentation de l’application

Cette application vous permet de :
- Explorer des jeux de données variés via une interface web moderne et intuitive.
- Générer des graphiques interactifs grâce à Plotly.
- Filtrer, exporter et analyser les données en temps réel.
- Naviguer entre plusieurs pages thématiques (exploration, analyses, dashboards…).

Elle a été conçue pour être facilement maintenable, évolutive et partageable dans un cadre professionnel ou pédagogique.


## 🛠️ Installation et lancement

Pour utiliser l’application sur votre machine, suivez ces étapes :

1. **Cloner le dépôt ou récupérer les fichiers du projet**  
    Placez-vous dans le dossier de votre choix et récupérez le projet.

2. **Installer les dépendances**  
    Toutes les librairies nécessaires sont listées dans le fichier `requirements.txt`. Installez-les avec la commande suivante :
    ```bash
    pip install -r requirements.txt
    ```

3. **Lancer l’application Streamlit**  
    Depuis la racine du projet, exécutez :
    ```bash
    streamlit run app.py
    ```
    L’application s’ouvrira automatiquement dans votre navigateur par défaut.

## 🗂️ Structure du projet

Le projet est organisé pour garantir clarté et maintenabilité :

- **`app.py`** : point d’entrée principal de l’application Streamlit.
- **`pages/`** : contient les différentes pages de l’application (exploration, analyses, dashboards…).
- **`utils/`** : fonctions utilitaires réutilisables :
  - `data.py` : gestion et traitement des données.
  - `charts.py` : création et personnalisation des graphiques.
- **`data/`** : jeux de données utilisés par l’application.
- **`.streamlit/`** : fichiers de configuration de Streamlit (thème, options avancées).
- **`requirements.txt`** : liste des dépendances Python.
- **`README.md`** : documentation du projet (ce fichier).

## 📋 Bonnes pratiques et conseils

- **Modularité** : chaque fonctionnalité est isolée dans un fichier ou un dossier dédié.
- **Lisibilité** : le code est commenté et structuré pour faciliter la prise en main.
- **Documentation** : ce README vous guide pas à pas pour l’installation, l’utilisation et la compréhension du projet.
- **Partage** : respectez les conditions d’utilisation, ne publiez pas ce projet sur des plateformes publiques sans autorisation.

Bonne exploration et visualisation de vos données !

