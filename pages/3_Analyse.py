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

tab1, tab2, tab3, tab4 = st.tabs(["Cinematic Overview", "Genres", "RunTime", "Cast & Crew"])
with tab1:
    df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    yearly_movies = df['release_year'].value_counts().reset_index()
    yearly_movies.columns = ['Année', 'Nombre de films']
    yearly_movies = yearly_movies.sort_values('Année')

    fig2 = px.line(yearly_movies, x='Année', y='Nombre de films', title="Évolution des sorties de films par année")
    fig2.update_traces(line=dict(color='indigo'))
    fig2.update_layout(xaxis_title="Année", yaxis_title="Nombre de films", height=600, margin=dict(l=50, r=50, t=50, b=50))
    st.plotly_chart(fig2, use_container_width=True)

    #st.subheader("Nombre de films par pays d'origine (Top 5 + Autres)")

    df['origin_country'] = df['origin_country'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    countries_expanded = df.explode('origin_country')
    country_counts = countries_expanded['origin_country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']

    top_5_countries = country_counts.head(5)
    autres_count = country_counts.iloc[5:]['count'].sum()
    autres_row = pd.DataFrame({'country': ['Autres'], 'count': [autres_count]})
    top_5_with_autres = pd.concat([top_5_countries, autres_row], ignore_index=True)

    custom_colors = px.colors.sequential.Plasma[:4] + ["#FFD700"]
    fig3 = px.pie(top_5_with_autres, values='count', names='country', title="Nombre de films par pays d'origine (Top 5 + Autres)", hole=0.4, color_discrete_sequence=custom_colors)
    fig3.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig3, use_container_width=True)

    # Afficher le heatmap
    #st.markdown("<p style='font-size:10px;'>Top 10 des acteurs les mieux notés avec au moins 10 films</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("images/Heatmap.png")
    # st.image("images/Heatmap.png")

with tab2:
    st.header("Genres")
    col1, col2 = st.columns(2)
    with col1:
        st.title('')
        df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        all_genres = df.explode('genres')
        all_genres['genre_name'] = all_genres['genres'].apply(lambda x: x['name'] if isinstance(x, dict) and 'name' in x else None)
        all_genres = all_genres.dropna(subset=['genre_name'])
        genre_counts = all_genres['genre_name'].value_counts().reset_index()
        genre_counts.columns = ['Genre', 'Count']
        fig1 = px.bar(
                genre_counts,
                x='Genre',
                y='Count',
                color='Count',
                title="Distribution des Genres les Plus Fréquents",
                labels={'Count': 'Nombre de films', 'Genre': 'Genre'},
                color_continuous_scale='viridis'
    )
        fig1.update_layout(
                xaxis_title="Genre",
                yaxis_title="Nombre de films",
                xaxis={'categoryorder': 'total descending'},  # Trier les genres par ordre décroissant de popularité
                height=600,
                width=1250,
                margin=dict(l=50, r=50, t=50, b=150)
    )   
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.title('')
        # Assurez-vous que la colonne 'genres' est bien en liste de dictionnaires
        df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

        # Étendre le DataFrame pour exploser les genres
        all_genres = df.explode('genres')

        # Extraire le nom du genre de chaque dictionnaire
        all_genres['genre_name'] = all_genres['genres'].apply(lambda x: x['name'] if isinstance(x, dict) and 'name' in x else None)

        # Supprimer les lignes sans genre valide
        all_genres = all_genres.dropna(subset=['genre_name'])

        # Grouper les votes par genre
        votes_by_genre = all_genres.groupby('genre_name', as_index=False)['vote_count'].sum()

        #   Grouper par genre et calculer la moyenne des notes (vote_average)
        average_votes_by_genre = all_genres.groupby('genre_name', as_index=False)['vote_average'].mean()

        # Créer un sous-graphe avec deux graphiques l'un en dessous de l'autre
        fig2 = make_subplots(
            rows=2, cols=1,  # Deux sous-graphes dans deux lignes
            subplot_titles=('Nombre de Votes par Genre', 'Moyenne des Notes par Genre')
        )

        # Créer un graphique pour les votes avec la palette 'Viridis'
        fig2.add_trace(
            go.Bar(
                x=votes_by_genre['genre_name'],
                y=votes_by_genre['vote_count'],
                marker=dict(
                    color=votes_by_genre['vote_count'],  # Appliquer la couleur en fonction du nombre de votes
                    colorscale='Viridis',  # Palette de couleurs Viridis
                    showscale=True  # Afficher l'échelle de couleurs
                ),
                name="Nombre de votes"
            ),
            row=1, col=1
        )

        # Créer un graphique pour la moyenne des notes avec la palette 'Viridis'
        fig2.add_trace(
            go.Bar(
                x=average_votes_by_genre['genre_name'],
                y=average_votes_by_genre['vote_average'],
                marker=dict(
                    color=average_votes_by_genre['vote_average'],  # Appliquer la couleur en fonction de la moyenne des notes
                    colorscale='Viridis',  # Palette de couleurs Viridis
                    showscale=True  # Afficher l'échelle de couleurs
                ),
                name="Moyenne des notes"
            ),
            row=2, col=1
        )

        # Mettre à jour la disposition du graphique
        fig2.update_layout(
            title="Répartition des Films par Genre",
            height=900,  # Augmenter la hauteur pour deux graphiques
            width=1250,
            showlegend=False,
            xaxis_title="Genre",
            yaxis_title="Nombre de votes",
            xaxis2_title="Genre",
            yaxis2_title="Moyenne des notes",
            xaxis={'categoryorder': 'total descending'},  # Trier les genres par ordre décroissant de popularité
            margin=dict(l=50, r=50, t=50, b=150),# Ajouter des marges pour une meilleure lisibilité
        )

        # Afficher le graphique
        st.plotly_chart(fig2, use_container_width=True)
  
with tab3:
    st.header("Durée")
    col1, col2 = st.columns(2)
    with col1:          
        df_cleaned = df.dropna(subset=['runtime'])
        fig3 = make_subplots(
            rows=1, cols=2,
            subplot_titles=("Histogramme des Durées", "Boîte à Moustaches des Durées"),
            column_widths=[0.5, 0.5]  
    ) 
        fig3.add_trace(
            go.Histogram(
            x=df_cleaned['runtime'],
            nbinsx=30,
            name="Histogramme",
            marker_color='indigo'
        ),
        row=1, col=1
)
# Ajouter la boîte à moustaches au sous-graphique 2
        fig3.add_trace(
            go.Box(
            y=df_cleaned['runtime'],
            name="distribution des durées des films",
            marker_color='indigo'
        ),
        row=1, col=2
)
        fig3.update_yaxes(tickprefix='min ', row=1, col=2)

        fig3.update_layout(
        title="Distribution des Durées des Films",
        xaxis_title="Durée des films (minutes)",
        yaxis_title="Fréquence",
        showlegend=False,
        height=600
)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        
        top_10_longest = df[['title', 'runtime']].sort_values(by='runtime', ascending=False).head(10)
        top_10_shortest = df[['title', 'runtime']].sort_values(by='runtime').head(10)

# Bar chart : Films les plus longs
        fig4 = px.bar(top_10_longest, x='title', y='runtime',
            title="Top 10 des films les plus longs", labels={'title': 'Titre des films', 'runtime': 'Durée (min)'}, color_discrete_sequence=['indigo'])
        fig4.update_xaxes(tickangle=45)
        st.plotly_chart(fig4, use_container_width=True)

# Bar chart : Films les plus courts
        fig5 = px.bar(top_10_shortest, x='title', y='runtime',
          title="Top 10 des films les plus courts", labels={'title': 'Titre des films', 'runtime': 'Durée (min)'}, color_discrete_sequence=['yellow'])
        fig5.update_xaxes(tickangle=45)
        st.plotly_chart(fig5, use_container_width=True)

with tab4:
        
    #col1, col2 = st.columns(2)
    #with col1:
        st.header("Cast")          
        st.image("images/Top 10 Acteurs.png")

    #with col2: 
        st.header(' Crew')   
        director_votes = df.explode('cast')
        director_votes = director_votes[director_votes['cast'].apply(
            lambda x: isinstance(x, dict) and x.get('known_for_department') == 'Directing')]

        director_votes['director_name'] = director_votes['cast'].apply(lambda x: x.get('name') if isinstance(x, dict) else None)


        director_votes = director_votes.dropna(subset=['director_name'])


        director_stats = director_votes.groupby('director_name').agg({
            'vote_average': 'mean',
            'vote_count': 'sum',
            'original_title': 'count'
    }).reset_index()


        director_stats.rename(columns={
            'original_title': 'film_count',
            'vote_average': 'average_rating',
            'vote_count': 'total_votes'
    }, inplace=True)


        director_stats = director_stats.sort_values(by='film_count', ascending=False)
        fig2 = px.bar(
        director_stats.head(10),  # Afficher les 10 meilleurs
        x='director_name',
        y='film_count',
        title="Top 10 des directeurs par nombre de films", 
        labels={'film_count': 'Nombre de films', 'director_name': 'Directeur'},
        color='film_count',
        color_continuous_scale='Plasma'
)
        st.plotly_chart(fig2, use_container_width=True)

# Diagramme pour la moyenne des votes par réalisateur
        fig3 = px.scatter(
        director_stats.head(10),
        x='director_name',
        y='average_rating',
        size='total_votes',
        title="Analyses de notes de top 10 directeurs(moyenne des notes vs total des votes)",
        labels={'average_rating': 'Moyenne des notes', 'total_votes': 'Total des votes', 'director_name': 'Directeur'},
        color='average_rating',
        color_continuous_scale='Plasma'
)
        st.plotly_chart(fig3, use_container_width=True)

