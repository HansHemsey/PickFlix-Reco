    #----------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                               Librairies                                                                 #
    #----------------------------------------------------------------------------------------------------------------------------------------------- #

import pandas as pd
import streamlit as st
import datetime
import time
import ast
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import nltk
from nltk.corpus import stopwords, movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import spacy
import base64
nltk.download('stopwords')
nltk.download('punkt_tab')

st.set_page_config(page_title="Accueil", layout="wide")

@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

# --- Chargement du CSS via le fichier style.css ---
with open('style.css') as c:
    css = c.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



# --- Logo centré ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/pickflix-hori.png", width=500)




# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <div class="hero-title">Trouvez votre prochain film préféré</div>
        <div id="recherche" class="search-box">
            </div>
    </div>
""", unsafe_allow_html=True)

# --- Chargement de la data ---
@st.cache_data
def load_data():
    df = pd.read_csv("Datasets-and-cleaning/dataset_final.csv")
    df.dropna(subset=["title", "poster_path"], inplace=True)
    df['title'] = df['title'].astype(str)
    # conversion release_year en numérique
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

    base_image_url = "https://image.tmdb.org/t/p/w500"
    df['poster_path'] = df['poster_path'].apply(lambda x: base_image_url + str(x) if pd.notna(x) else None)
    return df

df = load_data()

# --- Fonction de recherche ---
st.markdown("<h2 style='color:white;text-align: center'>🔍 Recherchez un film</h2>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 4, 1])
with col2: 
    search_input = st.text_input("Commencez à taper un titre de film", placeholder="Par ex. Inception...", label_visibility="collapsed")

matching_titles = []
if search_input:
    matching_titles = df[df["title"].str.contains(search_input, case=False, na=False)]["title"].unique()

selected_title = None
if search_input:
    if len(matching_titles) > 0:
        
        with col2:
            selected_title = st.selectbox("Résultats correspondants :", matching_titles, key="title_selector", label_visibility="collapsed")
    else:
        with col2:
            st.markdown("<p style='color:white; text-align: center;'>Aucun film ne correspond à votre recherche.</p>", unsafe_allow_html=True)
else:
    # --- Affichage de 5 films populaires ---
    st.markdown("---")
    st.markdown("<h3 style='color:#e50914; text-align: center;'>Films Populaires du Moment</h3>", unsafe_allow_html=True)
    popular_movies = df.nlargest(5, 'popularity')
    cols = st.columns(5)
    for i, movie in enumerate(popular_movies.itertuples()):
        with cols[i]:
            if pd.notna(movie.poster_path):
                st.image(movie.poster_path, use_container_width=True)

                # Titre en blanc, centré
                st.markdown(
                    f"<div style='text-align: center; color: white; font-weight: ;'>{movie.title} ({movie.release_year})</div>",
                    unsafe_allow_html=True
                )
            else:
                st.write(movie.title)


    # --- Affichage de films récents aléatoires ---
    st.markdown("---")
    st.markdown("<h3 style='color:#e50914; text-align: center;'>Films Aléatoires</h3>", unsafe_allow_html=True)

    current_year = datetime.datetime.now().year
    years_back = 10 

    # Filtrage par films récents
    recent_movies_df = df[(df['release_year'] >= (current_year - years_back)) & (df['release_year'].notna())]

    if not recent_movies_df.empty:
        # Sors 5 films aléatoires en tête d'affiche parmis les films récents
        random_recent_movies = recent_movies_df.sample(n=min(5, len(recent_movies_df)), random_state=None) # random_state=None for true randomness

        recent_cols = st.columns(5)
        for i, movie in enumerate(random_recent_movies.itertuples()):
            with recent_cols[i]:
                if pd.notna(movie.poster_path):
                    st.image(movie.poster_path, use_container_width=True)

                    # Titre en blanc, centré
                    st.markdown(
                        f"<div style='text-align: center; color: white; font-weight: ;'>{movie.title} ({movie.release_year})</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.write(f"{movie.title} ({int(movie.release_year)})")
    else:
        st.markdown("<p style='color:white; text-align: center;'>Aucun film récent disponible.</p>", unsafe_allow_html=True)

# --- Affiche le film sélectionné ---
if selected_title:
    with st.spinner("Recherche de votre film ainsi que de ses recommandations..."):
        time.sleep(4)
        
        selected_film = df[df["title"] == selected_title].iloc[0]

        st.markdown("---")
        st.markdown(f"<h3 style='color:#e50914;'>{selected_film['title']} ({int(selected_film['release_year']) if not pd.isna(selected_film['release_year']) else 'N/A'})</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 0.5, 3])
        
        if pd.notna(selected_film["poster_path"]):
            with col1:
                st.image(selected_film["poster_path"], use_container_width=True, caption=f"Affiche de {selected_film['title']}")
        else:
                st.warning("Affiche non disponible pour ce film.")

        with col2:
            st.markdown(f"<p style='color:white;'> ⌚ {int(selected_film['runtimeMinutes'])} min" if pd.notna(selected_film['runtimeMinutes']) else "**Durée :** N/A</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:white;'> ⭐ {selected_film['vote_average']:.2f} / 10" if pd.notna(selected_film['vote_average']) else "**Note moyenne :** N/A</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:white;'> 🔥 {selected_film['popularity']:.2f}" if pd.notna(selected_film['popularity']) else "**Popularité :** N/A</p>", unsafe_allow_html=True)
            st.button("⭐ Ajouter aux favoris")

        with col3:
            st.markdown(f"<p style='color:white;'><b>Genres :</b> {selected_film['genres_x'] if pd.notna(selected_film['genres_x']) else 'N/A'}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:white;'><b>Synopsis :</b> {selected_film['overview'] if pd.notna(selected_film['overview']) else 'N/A'}</p>", unsafe_allow_html=True)
        
            if pd.notna(selected_film['actors']):
                acteurs_list = ast.literal_eval(selected_film['actors'])
                acteurs = ", ".join(acteurs_list)
            else:
                acteurs = "N/A"
            st.markdown(f"<p style='color:white;'><b>Acteurs :</b> {acteurs}</p>", unsafe_allow_html=True)


    #----------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                               Machine learning                                                                 #
    #----------------------------------------------------------------------------------------------------------------------------------------------- #


    # Import du dataset utilisé pour le ML
    @st.cache_data
    def chargement(): 
        df1 = pd.read_csv('Datasets-and-cleaning/dataset_final_splitted.csv')
        df_ml = df1.drop(columns = ['Unnamed: 0.1', 'Unnamed: 0']).copy()
        return df_ml
    df_ml = chargement()

    # Application du Lemmatizer
    @st.cache_data
    def clean_text(text: str) -> str:
        nlp = load_spacy_model()
        # Chargement des stopwords
        stop_words = set(stopwords.words('english'))
        # 1. Conversion en minuscules
        text = text.lower()
        # 2. Suppression des balises HTML
        text = re.sub(r'<.*?>', '', text)
        # 3. Suppression des caractères spéciaux (garde lettres, chiffres et espaces)
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        # 4. Suppression des stopwords
        text = ' '.join([word for word in text.split() if word not in stop_words])
        # 5. Lemmatization avec spaCy
        doc = nlp(text)
        text = ' '.join([token.lemma_ for token in doc])
        # 6. Nettoyage final des espaces multiples
        text = ' '.join(text.split())
        return text

    @st.cache_data
    def clean_dataframe_column(df_ml, column_name: str, language: str = 'english'):
        # Appliquer le nettoyage sur la colonne spécifiée
        df_ml[f'clean_{column_name}'] = df_ml[column_name].apply(clean_text)
        return df_ml
    
    # Intégration dans le DF
    with st.spinner("Nettoyage des titres..."):
        df_ml = clean_dataframe_column(df_ml, 'overview')

    # Sélection des features
    X = df_ml[['release_year', 'runtimeMinutes', 'vote_average', 'vote_count', 'genre_1', 'nationality_1', 'title', 'actor_1', 'clean_overview']]

    # Standardisation des données
    # ----> Définition des colonnes selon si elles sont numériques ou catégorielles
    col_num = ['release_year', 'runtimeMinutes', 'vote_average', 'vote_count']
    col_cat = ['genre_1', 'nationality_1', 'actor_1']
    col_text = ['clean_overview']

    # ----> Définition des tranformations à apporter sur les colonnes selon leurs valeurs
    transfo_num = Pipeline(steps=[('scaler', StandardScaler()),
                                    ])

    transfo_cat = Pipeline(steps=[('imputation', SimpleImputer(strategy='constant', fill_value='manquant')),
                                    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    transfo_text = Pipeline(steps=[('flatten', FunctionTransformer(lambda x: x.iloc[:,0], validate=False)),
                                    ('Count vectorizer', TfidfVectorizer())])

    # ----> Définition du process de transformation
    preprocessor = ColumnTransformer([('num', transfo_num, col_num),
                                    ('cat', transfo_cat, col_cat),
                                    ('text', transfo_text, col_text)])

    # Construction du pipeline global avec préprocessing et régression
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),  # Transformation des données
        ('neighbor', NearestNeighbors(n_neighbors=6, metric='euclidean', algorithm='auto'))])  # Modèle de régression pour imputation

    # Entraînement du modèle
    model_pipeline.fit(X)

    # Choix d'un film de référence
    movie_ref = X[X['title'] == selected_film['title']]  # double crochet pour garder un DataFrame

    # transformer les données pour qu'elles soient standardisées
    X_transformed = model_pipeline.named_steps['preprocessor'].transform(X)
    movie_transformed = model_pipeline.named_steps['preprocessor'].transform(movie_ref)

    # trouver les 5 films voisins
    distances, indices = model_pipeline.named_steps['neighbor'].kneighbors(movie_transformed)

    #----------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                               Post Processing                                                                 #
    #----------------------------------------------------------------------------------------------------------------------------------------------- #


    # Récupérer les lignes correspondantes dans df_ml
    films_proches = df_ml.iloc[indices[0]]
    # Enlever le film sélectionné de la sélection
    films_proches = films_proches[films_proches['title'] != selected_film['title']]
    # Obtenir les titres restants en liste
    recommended_titles = films_proches['title'].tolist()
    # Récupérer les infos nécessaires pour affichage de la liste pour afficher les bonnes valeurs
    recommended_movies = df[df['title'].isin(recommended_titles)].copy()
    # On récupère les indices sans le film sélectionné
    valid_indices = [i for i in indices[0] if df.iloc[i]['title'] != selected_film['title']]
    recommended_movies = df.iloc[valid_indices]
    

    # Merge pour avoir accès aux affiches de films et titres
    recommended_movies = recommended_movies.merge(
    df[['title', 'poster_path']], on='title', how='left', suffixes=('', '_merged'))


    # Choisir la colonne `poster_path` correcte
    if 'poster_path_merged' in recommended_movies.columns:
        recommended_movies['poster_path'] = recommended_movies['poster_path_merged']
        recommended_movies.drop(columns=['poster_path_merged'], inplace=True)

    with col3:
        st.markdown("---")
        st.markdown(f"<h3 style='color:#e50914;'>🎬 Recommandations similaires à : {selected_film['title']}</h3>", unsafe_allow_html=True)

        cols_reco = st.columns(len(recommended_movies))
        for i, row in recommended_movies.iterrows():
            with cols_reco[i]:
                poster = row['poster_path'] if pd.notna(row['poster_path']) else "https://via.placeholder.com/300x450?text=No+Poster"
                
                st.image(poster, use_container_width=True)

                # Titre et année en blanc, centré, et un peu d'espace
                st.markdown(
                    f"<div style='text-align: center; color: white; margin-top: 5px;'>{row['title']} ({int(row['release_year'])})</div>",
                    unsafe_allow_html=True
                )
