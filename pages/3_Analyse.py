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
        <div class="hero-title">🎥 <u>Analyse du Cinéma</u></div>
            </div>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------------------ #
#                                                       CONTENU 
# ------------------------------------------------------------------------------------------------------------------------ #

# Création de 3 onglets
tab1, tab2, tab3 = st.tabs(["Films & Genres", "Acteurs & Réalisateurs", "Durée"])

with tab1:
    st.header("Les films de notre dataset :movie_camera: ")

    col1, col2 = st.columns([1,4])
    with col1:
        st.image("images/films_total.png")
    with col2:
        st.image("images/evol_films.png")
    
    st.markdown("""
                    <p class="custom-paragraph">‎</p>
          """, unsafe_allow_html=True)

    col3, col4 = st.columns([4,1])
    with col1:
        st.image("images/films_note.png")
    with col2:
        st.image("images/films_us.png")

    st.markdown("""
                    <p class="custom-paragraph">‎</p>
          """, unsafe_allow_html=True)

    col5, col6 = st.columns([1,4])
    with col5:
        st.image("images/films_fr.png")
    with col6:
        st.image("images/films_pop.png")
    
    st.markdown("""
                    <p class="custom-paragraph">‎</p>
          """, unsafe_allow_html=True)

    col7, col8 = st.columns([4,1])
    with col7:
        st.image("images/genre_pop.png")
    with col8:
        st.markdown("""
                    <p class="custom-paragraph">Ici, ce n'est pas très représentatif... </p>
                    <p class="custom-paragraph">Le film le plus populaire du dataset est un film du genre 'Horror'.</p>
                    <p class="custom-paragraph">Sa popularité est tellement élevée qu'elle perturbe complètement les moyennes.</p>
                    <p class="custom-paragraph">Il n'y a que 2,65% des films qui appartiennent au genre 'Horror' contre 52,11% de comédies (genre qui n'est même pas sur le podium du top 5).</p>
    """, unsafe_allow_html=True)
        
    st.markdown("""
                    <p class="custom-paragraph">‎</p>
          """, unsafe_allow_html=True)
        
    st.image("images/films_genres.png")

with tab2:
    st.header(" :eyes: Un petit coup d'oeil sur les acteurs / réalisateurs ")
    col1, col2, col3 = st.columns([1,2,3])

    with col1:
       st.image("images/age_moy.png")
       
    with col2:
        st.image("images/top10_acteurs.png")
    
    with col3:
        st.image("images/top10_real.png")
  
with tab3:
    st.header("La durée des films a-t-elle toujours été la même ?")

    col1, col2 = st.columns(2)
    with col1:          
       st.image("images/evol_duree.png")

    with col2:
        st.markdown("""
        <p class="custom-paragraph">Dans notre dataset, nous avons des films sortis entre 1914 et 2023.</p>
        <p class="custom-paragraph">Ah c'est sûr qu'il y a du choix, mais quand on veut regarder l'évolution de la durée des films c'est moins pratique.</p>
        <p class="custom-paragraph">En 1915 et en 1918, deux films extrêment longs ont été réalisés (respectivement 421 minutes et 191 minutes).</p> 
        <p class="custom-paragraph">Le paysage cinématographique était alors réduit.</p> 
        <p class="custom-paragraph">Ce qui nous donne une courbe qui malgré un début presque chaotique semble relativement plate.</p>    
    """, unsafe_allow_html=True)
         
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <p class="custom-paragraph">De ce fait, on va se permettre un zoom pour isoler ces outliers.</p>
        <p class="custom-paragraph">Maintenant, on peut voir que la durée des films a progressivement augmenté jusqu'en 1962.</p>
        <p class="custom-paragraph">Elle va osciller autour des 100 minutes jusqu'en 2023.</p>
    """, unsafe_allow_html=True)
        
    with col4:
        st.image("images/zoom_duree.png")

    st.markdown("""
        <p class="custom-paragraph">Et nos extrêmes alors ?</p>
    """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        st.image("images/top5_longs.png")
    with col6:
        st.image("images/top5_courts.png")

