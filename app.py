import pandas as pd
import streamlit as st
import datetime
import ast

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
        st.markdown(f"<p style='color:white;'>**Genres :** {selected_film['genres_x'] if pd.notna(selected_film['genres_x']) else 'N/A'}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:white;'>**Synopsis :** {selected_film['overview'] if pd.notna(selected_film['overview']) else 'N/A'}</p>", unsafe_allow_html=True)
       
        if pd.notna(selected_film['actors']):
            acteurs_list = ast.literal_eval(selected_film['actors'])
            acteurs = ", ".join(acteurs_list)
        else:
            acteurs = "N/A"
        st.markdown(f"<p style='color:white;'>**Acteurs :** {acteurs}</p>", unsafe_allow_html=True)

    

        