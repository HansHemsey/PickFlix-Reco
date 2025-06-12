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
        <div class="hero-title">📖 <u>Étude de Marché</u></div>
            </div>
    </div>
""", unsafe_allow_html=True)
# ------------------------------------------------------------------------------------------------------------------------ #
#                                                       CONTENU 
# ------------------------------------------------------------------------------------------------------------------------ #
st.markdown("<br><br><h1 style='color: white;'>T'as des infos sur la Creuse ?</h1><br>", unsafe_allow_html=True)
col1, col2 = st.columns(2, vertical_alignment="center")
with col1:        
    st.markdown("""
        <p class="custom-paragraph">La Creuse est un département rural situé dans la région Nouvelle-Aquitaine, au centre de la France.</p>
        <p class="custom-paragraph">Elle est connue pour ses paysages vallonnés, ses forêts et ses rivières paisibles. D'ailleurs, 1 habitant sur 3 réside en milieu rural</p>
        <p class="custom-paragraph"><strong>Guéret</strong> en est la préfecture et principale ville.</p> 
        <p class="custom-paragraph">La Creuse attire les amateurs de nature, de randonnées et de patrimoine ancien.</p>
        <p class="custom-paragraph">Elle fait partie des zones les moins peuplées et les plus calmes de France.</p>
        
    """, unsafe_allow_html=True)
with col2:
    st.image("images/paysage_creuse.png")

st.markdown("<br><br><h1 style='color: white;'>Qui habite là-bas ?</h1>", unsafe_allow_html=True)

col3, col4 = st.columns(2, vertical_alignment="center")
with col3: 
    st.markdown("""
        <p class="custom-paragraph">En 2024, la population totale de la Creuse était de 113 922 habitants, et la densité est de 22 habitants par km².</p> 

        <p class="custom-paragraph">Le nombre d'habitants est en baisse de 1.79% depuis 2020.</p>        

        <p class="custom-paragraph">Presque un tiers des Creusois a <strong>65 ans ou plus, et 39,7% sont des retraités.</p>

        <p class="custom-paragraph">En moyenne, la population de la Creuse est équitablement répartie en fonction du sexe dans chaque tranche d'âge.</p> 

    """, unsafe_allow_html=True)
with col4: 
    st.image("images/population.png")

st.markdown("<br><br><h1 style='color: white;'>Le Cinéma - Paysage français</h1>", unsafe_allow_html=True)

st.markdown("<p class='custom-paragraph'>Le public des salles de cinéma françaises se répartit de la manière suivante :</p>", unsafe_allow_html=True)
st.image("images/public_francais.png")

st.markdown("<p class='custom-paragraph'>Ils consomment leur cinéma selon différents critères. Globalement, les comédies, les films d'action/aventure et les thrillers font plus de fans, ainsi que les films américains puis français.</p>", unsafe_allow_html=True)

col5, col6 = st.columns(2, vertical_alignment="center")
with col5: 
    st.image("images/genres_pref.png")
with col6: 
    st.image("images/nationalites_pref.png")

col7, col8 = st.columns(2, vertical_alignment="center")
with col7:
    st.markdown("<p class='custom-paragraph'>Sans surprise, les Français préférent leur films en VF, même si pour la tranche d'âge des 18-34 ans c'est très serré.</p>", unsafe_allow_html=True)
with col8:
    st.image("images/VO_VF.png")

st.markdown("<br><br><h1 style='color: white;'>Le Cinéma dans la Creuse </h1>", unsafe_allow_html=True)

st.markdown("""
            <p class='custom-paragraph'>Le département de la Creuse compte plusieurs salles de cinéma, dont :<br>
                - Cinéma Le Sénéchal à Guéret<br>
                - Cinéma Le Sénéchal à Guéret
                - Cinéma Eden à La Souterraine
                - Cinéma Alpha à Évaux-les-Bains
                - Cinéma Claude Miller à Bourganeuf
                - Salle des fêtes de Dun-le-Palestel </p>
             <p class='custom-paragraph'> Ces établissements sont classés "Art et Essai" et bénéficient de soutiens régionaux pour favoriser la diversité cinématographique et l'accès à la culture.</p>
                
             <p class='custom-paragraph'> La fréquentation des cinémas creusois a connu une nette amélioration en 2024 :<br>
                - Cinéma Le Sénéchal à Guéret a enregistré près de 95 000 entrées, avec une augmentation de près de 2 000 spectateurs par rapport à 2023.<br>
                - Cinéma Le Colbert à Aubusson a constaté une hausse de 1 800 entrées, soit une augmentation de près de 9 % par rapport à l'année précédente.
                - Cinéma Eden à La Souterraine a vendu 12 305 billets, marquant une hausse de 3 % par rapport à 2023.</p>
                
             <p class='custom-paragraph'> Ces chiffres témoignent d'une reprise de l'intérêt pour les salles de cinéma en Creuse, malgré les défis posés par la crise sanitaire et la concurrence du streaming.</p> 
             <p class='custom-paragraph'> Si vous souhaitez des informations plus détaillées sur les horaires, les tarifs ou les programmes spécifiques de ces cinémas, n'hésitez pas à me le faire savoir ! </p>  
                """, unsafe_allow_html=True)
st.image("images/cinema_gueret.png")

st.markdown("<p class='custom-paragraph'>Les Creusois consomme leur cinéma comme ceci:</p>", unsafe_allow_html=True) 

col9, col10 = st.columns(2, vertical_alignment="center")
with col9:
    st.image("images/genre_creuse.png")
with col10:
    st.image("images/genre_sexe.png")
st.image("images/genre_age.png")

st.markdown("<br><br><h1 style='color: white;'>Orientations</h1>", unsafe_allow_html=True)
st.image("images/ccl_1.png")
st.image("images/ccl_2.png")
st.image("images/ccl_3.png")