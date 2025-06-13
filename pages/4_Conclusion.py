import pandas as pd
import streamlit as st
import datetime
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px
import ast

# --- Chargement du CSS via le fichier style.css ---
with open('style.css') as c:
    css = c.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/pickflix-hori.png", width=500)

# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <div class="hero-title">🎯 <u>Conclusion</u></div>
            </div>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------------------ #
#                                                       CONTENU 
# ------------------------------------------------------------------------------------------------------------------------ #

st.markdown("""
<div class="custom-paragraph">

### 🤯 Difficultés rencontrées

La création de notre algorithme de recommandation basé sur **KNN non supervisé** nous a confrontés à plusieurs défis techniques et méthodologiques :

- **Prétraitement des données** : il a fallu transformer certaines colonnes contenant des chaînes de caractères (comme les genres, les acteurs, ou l'overview) en données numériques exploitables dans le dataset mais aussi par le modèle. Ce processus, notamment via l'encodage et la vectorisation, s’est avéré plus complexe que prévu.
- **Choix des features pertinentes** : il était essentiel de bien sélectionner les variables qui allaient alimenter notre algorithme pour garantir des recommandations cohérentes. Cela a nécessité plusieurs itérations et tests.
- **Détermination de la distance optimale** : nous avons dû expérimenter avec différentes métriques de distance (euclidienne, cosinus…) afin d’obtenir des résultats satisfaisants.
- **Temps de calcul** : sur de grands jeux de données, l’algorithme KNN peut devenir lent, car il repose sur le calcul de distances entre tous les points.

---

### 🚀 Pistes d'amélioration

Pour aller plus loin et améliorer la qualité de notre application et la performance de notre système de recommandation, plusieurs pistes sont envisageables :

- **Ajouter la possibilité de cliquer** sur les affiches de films afin d'accéder à leur détails.
- **Intégrer des données utilisateur** (notes, historique de visionnage, interactions) pour personnaliser davantage les recommandations.
- **Optimiser le déploiement** : par exemple, en pré-calculant les plus proches voisins et en les stockant dans une base, afin de gagner du temps lors des appels.
- **Évaluer la qualité des recommandations** avec des métriques précises (RMSE, précision, rappel, taux de clics) pour guider les itérations.
            
Il y a également de nombreuses améliorations sur l'application en elle-même que nous pourrions apporter. L'ajout d'informations via des API nous permettrait d'ajouter les photos des acteurs présents dans chaque film, avec leur rôle dans le film, la bande-annonce, des extraits d'articles de presse spécialisée, la liste est longue.

---
            
### 🤘 Un grand merci à Teddy qui nous a guidé avec bienveillance et PATIENCE !
            
---

</div>
""", unsafe_allow_html=True)
