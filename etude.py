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

st.markdown("""
<div class="navbar">
    <div class="navbar-left">PickFlix</div>
    <div class="navbar-center">
        <a href="/app" target="_self">Accueil</a>
        <a href="/etude" target="_self">Étude de marché</a>
        <a href="/analyse" target="_self">Analyse</a>
        <a href="/conclusion" target="_self">Conclusion</a>
    </div>
    <div class="navbar-right">
        <a href="/app/#recherche" style="text-decoration:none">🔎</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <div class="hero-title">📖 <u>Étude de Marché</u></div>
            </div>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------------------ #
#                                                       CONTENU 
# ------------------------------------------------------------------------------------------------------------------------ #
st.markdown("<br><br><h1>C’est quoi ? C’est où la Creuse ?</h1><br>", unsafe_allow_html=True)
col1, col2 = st.columns(2, vertical_alignment="center")
with col1:        
    st.markdown("""
        <p>Département (23) qui tire son nom de la rivière Creuse qui le traverse.</p>
        <p>Dans la région nouvelle Aquitaine. Au centre de la France.</p>
        <p>Second département français le moins peuplé avec <strong>115 702</strong> habitants en 2021.</p> 
        <p>Sa plus grande ville et sa préfecture est <strong>Guéret</strong>.</p>
        <p>L'économie de la Creuse repose traditionnellement sur <strong>deux secteurs</strong>:<br>
                - l'agriculture (majoritairement l'élevage mais aussi la sylviculture);<br>
                - l'artisanat (comme la tapisserie d'Aubusson).</p>
        <p>Depuis quelques années, <strong>le développement du tourisme vert</strong> rapproche celui-ci du niveau des départements limitrophes par la création de nombreuses structures d'accueil, chambres d'hôtes, gîtes ruraux.</p>
    """, unsafe_allow_html=True)
with col2:
    #st.image("images/ecu_creuse.png")
    st.image("image/creuse-carte.png")

st.markdown("<br><br><h1>La population</h1>", unsafe_allow_html=True)
st.markdown("<p>Selon les estimations de l'INSEE au 1ᵉʳ janvier 2021, la Creuse, avec une population de 115 702 habitants, est le deuxième département le moins peuplé de France métropolitaine, juste après la Lozère.</p>", unsafe_allow_html=True)
col3, col4 = st.columns(2, vertical_alignment="center")
with col3: 
    st.markdown("""
        <p>En 2021, la population totale de la Creuse était de <strong>115 702</strong> habitants.</p> 

        <p>Parmi eux, <strong>69 661</strong> personnes étaient âgées de <strong>45 ans ou plus, ce qui représente environ <strong>60,2 %</strong> de la population totale.</p>

        <p>En moyenne, la population de la Creuse est répartie de manière <strong>équilibrée entre hommes et femmes</strong> dans chaque tranche d'âge.</p> 

        <p>Cependant, <strong>pour les 75 ans et plus</strong>, les femmes représentent une majorité significative, avec environ <strong>60 %</strong> de femmes.</p>
    """, unsafe_allow_html=True)
with col4: 
    st.image("images/repart_pop_creuse.png")

st.markdown("<br><p>Selon les estimations de l'INSEE au 1ᵉʳ janvier 2021, la Creuse, avec une population de 115 702 habitants, est le deuxième département le moins peuplé de France métropolitaine, juste après la Lozère.</p>", unsafe_allow_html=True)
col5, col6 = st.columns(2, vertical_alignment="center")
with col5: 
    st.markdown("""
        <p>Depuis 1968, la Creuse a connu une diminution significative de sa population, passant de <strong>156 876 habitants à 115 702 en 2021</strong>.</p> 

        <p>Cette tendance à la baisse reflète les défis démographiques auxquels le département est confronté, notamment l'exode rural et le vieillissement de la population.</p>

        <p>Ces facteurs peuvent influencer la fréquentation des cinémas locaux, avec une diminution potentielle du nombre de spectateurs.</p> 
    """, unsafe_allow_html=True)
with col6: 
    st.image("images/evol_pop_creuse.png")

st.markdown("<br><br><h1>Le cinéma - Données générales</h1>", unsafe_allow_html=True)
st.markdown("<p>Les habitudes de fréquentation des salles de cinéma en France varient selon l'âge et le sexe. Selon une étude de l'INSEE en 2022, la proportion de personnes étant allées au cinéma au cours des douze derniers mois est la suivante :</p>", unsafe_allow_html=True)
st.image("images/frequ_cinema.png")
st.markdown("<p>Ces données indiquent que la fréquentation des salles de cinéma diminue avec l'âge pour les deux sexes, avec une proportion légèrement plus élevée de femmes n'allant pas au cinéma, notamment dans les tranches d'âge supérieures.</p>", unsafe_allow_html=True)
st.markdown("<strong><p>Il est important de noter que ces statistiques sont nationales et peuvent varier localement, notamment dans des départements comme la Creuse, où la population est plus âgée et moins dense. Ces facteurs peuvent influencer la fréquentation des cinémas locaux.</p></strong><br>", unsafe_allow_html=True)
col7, col8 = st.columns(2, vertical_alignment="center")
with col7: 
    st.markdown("""
        <p>Les préférences cinématographiques varient selon l'âge et le sexe des spectateurs. Ces deux graphiques montrent les genres préférés au cinéma par les hommes et les femmes selon les tranches d'âge en France.</p> 

        <p><strong>Genre dominant par sexe :</strong> Les femmes préfèrent les comédies et les comédies romantiques, tandis que les hommes montrent une plus forte préférence pour les films d'action et les thrillers.</p>

        <p><strong>Variation avec l'âge :</strong> La popularité des genres évolue avec l'âge. Par exemple, les jeunes (18-24 ans) préfèrent les films fantastiques et d'action, tandis que les plus âgés (65 ans et plus) tendent à apprécier davantage les comédies et les films historiques.</p> 

        <p><strong>Genres stables et déclinants :</strong> La comédie reste un genre populaire dans toutes les tranches d'âge, mais les films de science-fiction et d'action sont plus appréciés par les jeunes, avec une baisse de popularité chez les spectateurs plus âgés.</p>
    """, unsafe_allow_html=True)
with col8: 
    st.image("images/pref_genre.png")

st.markdown("<br><br><h1>Le cinéma dans la Creuse </h1>", unsafe_allow_html=True)
col9, col10 = st.columns(2, vertical_alignment="center")
with col9: 
    data_cinema = {
        "Info 2023": [
            "Salles", "Fauteuils", "Entrées", "Recettes", 
            "Recettes moyennes / entrées", "Séances", 
            "Entrées par habitant en 2023", "Taux d'occupation des fauteuilles", 
            "PdM en entrées des films français (%)", "PdM en entrées des films américains (%)"
        ],
        "France": [
            "6 320", "1 160 000", "180,4M", "13 339M€", 
            "7,39", "8 300 000", "2,71", "12,40%", 
            "40,00%", "42,00%"
        ],
        "Creuse": [
            "7", "2 150", "1,4M", "9,3M€", 
            "6,76", "72 617", "2,47", "11,40%", 
            "50,10%", "34,20%"
        ]
    }

    df_cinema = pd.DataFrame(data_cinema)
    st.dataframe(df_cinema)

with col10: 
    st.markdown("""
        <p>Le département de la Creuse est un des département les moins bien équipé en salle de France. Il possède cependant une des population les plus faibles de france. Ce que l’on peut noter des données du CNC :</p> 

        <p>     - Il n’y a pas de multiplex (Pathé, Gaumont etc.).</p>

        <p>     - Les recettes sont plus faibles que la moyenne nationale et le taux d’occupation légèrement plus faible également.</p> 

        <p>     - On peut également noter que la répartition films français / américains est nettement différente qu’au niveau national (8% de moins pour les films américains et 10% de plus pour les films français).</p>
    """, unsafe_allow_html=True)
    
st.markdown("<br>", unsafe_allow_html=True)

col11, col12, col13 = st.columns(3)
with col11:
    st.image("images/evol_idf_creuse.png")
with col12:
    st.image("images/evol_recette.png")
with col13:
    st.image("images/evol_taux_occup.png")
    
st.markdown("""
    <p>D'après les données du CNC sur les fréquentations, recette et taux d’occupation des départements, la Creuse, malgré son faible niveau de service dans les ICC (Industrie Culturelles et Créatives), semble en évolution positive sur ces 3 critères.</p> 

    <p>Il faut cependant noter une chute importante de la fréquentation, des recettes et du taux d’occupation pendant la crise du COVID qui a pu mettre en difficulté votre établissement.</p>
    <br>
""", unsafe_allow_html=True)
# <p><strong>La baisse d’activité de votre cinéma ne semble donc pas lié à un désamour du cinéma part les Creusois.</strong></p> 

st.image("images/swot.png")

st.markdown("<br><br><h1>Nos conclusions</h1>", unsafe_allow_html=True)
st.markdown("<p>Pour concevoir une application de recherche de films pour un cinéma en tenant compte des préférences démographiques et cinématographiques, voici la marche à suivre basée sur nos analyses et graphiques :</p>", unsafe_allow_html=True)
col14, col15 = st.columns(2, vertical_alignment="center")
with col14: 
    st.markdown("""
        <p><strong>1. Segmenter les utilisateurs par âge et sexe</strong></p> 
        <p>L’application pourrait <strong>demander l’âge et le sexe des utilisateurs</strong> dès l’inscription, ou les recueillir de façon optionnelle <strong>pour proposer une sélection de films personnalisée.</strong></p>
        <br>
        <p><strong>2. Personnalisation des recommandations</strong></p> 
        <p>     - <strong>Jeunes utilisateurs (18-34 ans) : Mettre en avant des films d’action, fantastiques et comédies romantiques.</strong> Ces genres sont particulièrement populaires dans ce segment.</p>
        <p>     - <strong>Public plus âgé (35 ans et plus) : Proposer davantage de comédies et de films historiques</strong>, genres majoritairement appréciés par les 50 ans et plus, avec <strong>un accent particulier sur les films d’auteur et les drames</strong> pour les seniors. Nous ferons également <strong>un focus sur les films français</strong> (au regard des informations collectés lors de l’étude de marché).</p>

    """, unsafe_allow_html=True)
with col15: 
    st.markdown("""
        <p><strong>3. Filtrage et recherche avancée</strong></p> 
        <p>Intégrer un <strong>système de filtres permettant aux utilisateurs de rechercher des films par genre</strong> (action, comédie, drame, etc.) et éventuellement par sous-genre.</p>
        <br>
        <p><strong>4. Feedback et interaction utilisateur</strong></p> 
        <p>     - Permettre aux utilisateurs de <strong>noter et de commenter les films, afin d’optimiser les recommandations basées sur les préférences locales et les tendances du public.</strong></p>
        <p>     - <strong>Recueillir des données d’utilisation pour affiner les propositions</strong> et améliorer l’application.</p>
        <p>     - Diffuser des <strong>notifications pour des sorties de films correspondant aux préférences des utilisateurs</strong>, augmentant ainsi l’engagement et la fréquentation.</p>
        <p>     - <strong>Affichers les films les plus votés, pourrait vous permettre de proposer des rediffusions de ces films</strong> à intervalles réguliers.</p>

    """, unsafe_allow_html=True)