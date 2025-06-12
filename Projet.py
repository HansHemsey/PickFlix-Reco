import streamlit as st

st.set_page_config(page_title="🔎 Projet", layout="wide")

# --- Chargement du CSS via le fichier style.css ---
with open('style.css') as c:
    css = c.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# --- Logo ou bannière ---
st.image("images/pickflix-hori.png", use_container_width=True)

# --- Titre principal ---
#st.markdown("<h1 style='text-align: center; color: white; margin-top: -20px;'>🎬 Bienvenue !</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #AAAAAA;'>Votre assistant de recommandation de films personnalisée</h3>", unsafe_allow_html=True)

# --- Séparateur ---
st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)

# --- Texte de bienvenue ---
st.markdown("""
<div style='color: white; font-size: 18px; text-align: center; line-height: 1.6; max-width: 1000px; margin: auto;'>
    🔍 Recherchez des films<br>
    ⭐ Ajoutez vos films préférés à votre liste<br>
    🧠 Recevez des recommandations personnalisées selon vos goûts<br><br>
    <b>Utilisez le menu à gauche</b> pour commencer votre aventure cinéphile 🎞️
</div>
""", unsafe_allow_html=True)

# --- Footer ou note ---
st.markdown("<br><p style='text-align: center; color: #999;'>Application conçue avec ❤️ par Angéline, Stéphane & Yanis</p>", unsafe_allow_html=True)
