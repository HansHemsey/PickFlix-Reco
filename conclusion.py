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
        <div class="hero-title">🎯 <u>Conclusion</u></div>
            </div>
    </div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------------------ #
#                                                       CONTENU 
# ------------------------------------------------------------------------------------------------------------------------ #