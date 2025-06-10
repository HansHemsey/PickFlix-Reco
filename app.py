import pandas as pd
import streamlit as st
import datetime
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
nltk.download('stopwords')
nltk.download('punkt_tab')
nlp = spacy.load('en_core_web_sm')

# --- CSS / HTML pour la Navbar et la Hero Section ---
st.markdown("""
    <style>
        body {
            background-color: #141414 !important;
            color: white;
        }
        .stApp {
            background-color: #141414;
        }

        .navbar {
            background-color: #141414;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
            font-family: 'Helvetica Neue', sans-serif;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .navbar-left {
            font-size: 1.8rem;
            font-weight: bold;
            color: red;
        }

        .navbar-center a {
            margin: 0 1rem;
            text-decoration: none;
            color: white;
            font-size: 1.1rem;
        }

        .navbar-center a:hover {
            color: #e50914;
        }

        .navbar-right {
            background-color: #e50914;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
        }

        .hero {
            background-color: #141414;
            padding: 6rem 2rem;
            text-align: center;
            color: white;
            font-family: 'Helvetica Neue', sans-serif;
        }

        .hero-title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }

        .stTextInput > div > div > input {
            width: 100%; /* Make Streamlit input fill its container */
            padding: 1rem;
            font-size: 1.2rem;
            border-radius: 5px;
            border: none;
            outline: none;
            background-color: #333; /* Darker background for input */
            color: white;
        }
        .stSelectbox > div > div > div {
            background-color: #333;
            color: white;
        }
        .stSelectbox > div > div > div > div[data-baseweb="select"] {
            background-color: #333;
            color: white;
        }
        .stSelectbox > div > div > div > div[role="listbox"] {
            background-color: #333;
            color: white;
        }
        .stSelectbox > div > div > div > div[role="option"] {
            color: white;
        }

        @media (max-width: 768px) {
            .hero-title {
                font-size: 2rem;
            }
        }

        img.movie-poster:hover {
            transform: scale(1.05);
            z-index: 10;
        }
    </style>

    <div class="navbar">
        <div class="navbar-left">PickFlix</div>
        <div class="navbar-center">
            <a href="#">Accueil</a>
            <a href="#">Catégories</a>
            <a href="#">Favoris</a>
        </div>
        <div class="navbar-right">
            <a href="#recherche" style="text-decoration:none">🔎</a>
        </div>
    </div>
""", unsafe_allow_html=True)

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
    df = pd.read_csv("./Datasets_cleaning/dataset_final.csv")
    df.dropna(subset=["title", "poster_path"], inplace=True)
    df['title'] = df['title'].astype(str)
    # conversion release_year en numérique
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

    base_image_url = "https://image.tmdb.org/t/p/w500"
    df['poster_path'] = df['poster_path'].apply(lambda x: base_image_url + str(x) if pd.notna(x) else None)
    return df

df = load_data()

# --- Fonction de recherche ---
st.markdown("<h2 style='color:white;'>🔍 Recherchez un film</h2>", unsafe_allow_html=True)


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
            st.markdown("<p style='color:gray; text-align: center;'>Aucun film ne correspond à votre recherche.</p>", unsafe_allow_html=True)
else:
    
    st.markdown("---")
    st.markdown("<h3 style='color:#e50914; text-align: center;'>Films Populaires du Moment</h3>", unsafe_allow_html=True)
    popular_movies = df.nlargest(5, 'popularity')
    cols = st.columns(5)
    for i, movie in enumerate(popular_movies.itertuples()):
        with cols[i]:
            if pd.notna(movie.poster_path):
                st.image(movie.poster_path, caption=movie.title, use_container_width=True)
            else:
                st.write(movie.title)

    # --- Affichage de films récents aléatoires ---
    st.markdown("---")
    st.markdown("<h3 style='color:#e50914; text-align: center;'>Nouveautés Aléatoires</h3>", unsafe_allow_html=True)

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
                    st.image(movie.poster_path, caption=f"{movie.title} ({int(movie.release_year)})", use_container_width=True)
                else:
                    st.write(f"{movie.title} ({int(movie.release_year)})") # Fallback to just title if poster is missing
    else:
        st.markdown("<p style='color:white; text-align: center;'>Aucun film récent disponible.</p>", unsafe_allow_html=True)

# --- Affiche le film sélectionné ---
if selected_title:
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
        

    with col3:
        st.markdown(f"<p style='color:white;'><b>Genres :</b> {selected_film['genres_x'] if pd.notna(selected_film['genres_x']) else 'N/A'}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'><b>Synopsis :</b> {selected_film['overview'] if pd.notna(selected_film['overview']) else 'N/A'}</p>", unsafe_allow_html=True)
       
        if pd.notna(selected_film['actors']):
            acteurs_list = ast.literal_eval(selected_film['actors'])
            acteurs = ", ".join(acteurs_list)
        else:
            acteurs = "N/A"
        st.markdown(f"<p style='color:white;'><b>Acteurs :</b> {acteurs}</p>", unsafe_allow_html=True)


    # Machine learning

    # Import du dataset utilisé pour le ML
    df1 = pd.read_csv('./Datasets_cleaning/dataset_final_splitted.csv')
    df_ml = df1.drop(columns = ['Unnamed: 0.1', 'Unnamed: 0']).copy()


    # Application du Lemmatizer
    # LEMMATIZER
    stop_words = set(stopwords.words('english'))

    # On créé une fonction pour passer le texte en minuscule
    def lower_case(text: str) -> str:
        return text.lower()

    # On créé une fonction pour supprimer les balises html du texte
    def remove_html_tags(text: str) ->  str:
        return re.sub(r'<.*?>', '', text)
    # <h1> </p> <b> </b> <a href="http://google.com"> </a>

    # On créé une fonction pour enlever les caractères spéciaux
    def remove_special_char(text: str) -> str:
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # On créé une fonction pour enlever les stopwords
    def remove_stopwords(text: str) -> str:
        return ' '.join([word for word in text.split() if word not in stop_words])

    # On créé une fonction pour appliquer le lemmatiser sur le texte
    def lemmatize(text: str) -> str:
        doc = nlp(text)
        return ' '.join([token.lemma_ for token in doc])

    # On créé une fonction qui va appliquer toutes les transformations sur le texte
    def main_clean(review: str) -> str:
        review = lower_case(review)
        review = remove_html_tags(review)
        review = remove_special_char(review)
        review = remove_stopwords(review)
        review = lemmatize(review)
        return review

    # Intégration dans le DF
    df_ml['clean_overview'] = df_ml['overview'].apply(main_clean)

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
                st.image(poster, caption=f"{row['title']} ({int(row['release_year'])})", use_container_width=True)
    