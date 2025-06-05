# Introduction

« Netflix est un service de diffusion en streaming qui permet à ses membres de regarder une grande variété de séries TV, films, documentaires, etc. sur des milliers d’appareils connectés à Internet. »
Créé en 1998, Netflix pèse aujourd’hui plus de 20 milliards de dollars de chiffre d’affaires et consomme 12,6% de la bande passante Internet mondiale.
Lorsqu’on accède au service Netflix, le système de recommandations aide l’utilisateur à trouver aussi facilement que possible les séries TV ou films qu’il pourrait apprécier, grâce à un système de recommandation. 
Netflix calcule ainsi la probabilité que l’utilisateur regarde un titre donné du catalogue de Netflix, et peut ainsi optimiser ces partenariats ou plus globalement sa stratégie marketing. 
Netflix est l’archétype de la société data-driven.
Votre client n’est pas Netflix, mais il a de grandes ambitions !

# Objectif & Enjeux

Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse situé dans la Creuse vous contacte. Il a décidé de passer le cap du digital en créant un site Internet taillé pour les locaux.
Pour aller encore plus loin, il vous demande de créer un moteur de recommandations de films qui à terme, enverra des notifications aux clients via Internet.
Pour l’instant, aucun client n’a renseigné ses préférences, vous êtes dans une situation de cold start. Mais heureusement, le client vous donne une base de données de films basée sur la plateforme IMDb.

Commencez par une étude de marché sur la consommation de cinéma dans la région de la Creuse, afin de mieux comprendre les attentes et les préférences du public local. 
Cette étape préliminaire vous permettra de définir une orientation adaptée pour la suite de l’analyse de votre base de données.
Après cette étude, réalisez une analyse approfondie de votre base de données pour identifier des tendances et caractéristiques spécifiques. 
Cette analyse devrait inclure : l’identification des acteurs les plus présents et les périodes associées, l’évolution de la durée moyenne des films au fil des années, la comparaison entre les acteurs présents au cinéma et dans les séries, l’âge moyen des acteurs, ainsi que les films les mieux notés et les caractéristiques qu’ils partagent.
Sur la base des informations récoltées, vous pourrez affiner votre programmation en vous spécialisant par exemple sur les films des années 90 ou les genres d’action et d’aventure, afin de mieux répondre aux attentes du public identifié lors de l’étude de marché.

Après cette étape analytique, sur la fin du projet, vous utiliserez des algorithmes de machine learning pour recommander des films en fonction de films qui ont été appréciés par le spectateur.
Le client vous fournit également une base de données complémentaires venant de TMDB, contenant des données sur les pays des boîtes de production, le budget, les recettes et également un chemin vers les posters des films. 
Il vous est demandé de récupérer les images des films pour les afficher dans votre interface de recommandation.
Attention ! L’objectif n’est pas de diffuser dans le cinéma les films recommandés. L’objectif final est d’avoir une application avec d’une part des KPI et d’autre part le système de recommandation avec une zone de saisie de nom de film pour l’utilisateur. 
Cette application sera mise à disposition des clients du cinéma afin de leur proposer un service supplémentaire, en ligne, en plus du cinéma classique.

# Ressources

Les données sont disponibles sur le site IMDb, réparties en plusieurs tables (films, acteurs, réalisateurs, notes, etc.).
- Documentation des colonnes et tables : "https://developer.imdb.com/non-commercial-datasets/"
- Datasets IMDb : "https://datasets.imdbws.com/"
- Dataset complémentaire TMDB : "https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view"

# Remarques Techniques

Vous pouvez télécharger les datasets en local, sur votre Drive ou bien sur un GitHub. Mais vous pouvez surtout ne pas les télécharger, et importer directement les datasets dans Pandas en mettant le lien du dataset.
Les datasets sont très volumineux, il y a plus de 7M films et 10M acteurs référencés. Vous n’aurez sans doute pas besoin de la base complète. 
Une fois que vous aurez fait du nettoyage et des filtres sur ce que vous trouvez pertinent, pensez à exporter vos données “allégées”. Ce sera plus rapide à réimporter.
Pour rappel, Google Colab propose des serveurs “partagés”. Les performances dépendent donc du nombre de personnes connectées en même temps. 
Parfois, vous ne pourrez donc pas charger tous ces volumineux datasets. N’hésitez pas à les traiter en local grâce à Anaconda / Jupyter.
Les datasets IMDB sont au format TSV, pour “Tabulation Separated Values”. C’est similaire au format CSV, mais séparé par des tabulations plutôt que des virgules. 
Vous pouvez utiliser la fonction suivante, qui indique que le séparateur est une tabulation : pd.read_csv(“dataset_link”, sep = “\t”, nrows=1000)

# Organisation et Planning

Vous aurez besoin de faire des jointures (comme en SQL) entre les datasets, des graphiques en Python, des retraitements avec Pandas, du machine learning. 
Bien entendu, vous ne pourrez pas tout faire la première semaine, car vous apprendrez ces notions en parallèle du projet. 
Afin de vous donner de la visibilité, voici un planning indicatif, mais libre à vous de vous organiser :

- Semaine 1 & 2 : Réaliser une étude de marché sur la consomation de cinéma dans la région de la Creuse (CNC, Insee)
- Semaine 3 & 4 : Appropriation, exploration des données et nettoyage (Pandas, Matplotlib, Seaborn)
- Semaine 5 & 6 : Machine learning et recommandations (scikit-learn)
- Semaine 7 : Affinage, interface et présentation

# Besoins Clients

Le client aurait souhaité intégrer votre analyse et vos recommandations à son site pour pouvoir le tester, mais le timing est trop serré. 
Force de proposition, vous lui proposer de __le rendre testable au moyen d’un outil de votre choix__.
Le client a 2 besoins, qui peuvent être dans 2 outils séparés :
- Obtenir quelques statistiques sur les films (type, durée), acteurs (nombre de films, type de films) et d’autres. Vous le ferez notamment à l’aide de visualisations.
  Vous pouvez utiliser un outil de business intelligence, ou des graphiques via Python.
- Retourner une liste de films recommandés en fonction d’IDs ou de noms de films choisis par un utilisateur.
  Vous pouvez intégrer ces recommandations à un outil de dashboarding, ou bien faire ces recommandations directement depuis la ligne de commande (“input”).
L’objectif n’est pas d’arriver à un travail parfait, mais que le système fonctionne et que vous arriviez à déceler les points à améliorer.*

# Missions et Livrables Attendus

  1. Missions
- Faire une présentation pour présenter votre travail, expliquer votre démarche, les outils utilisés, les difficultés rencontrées, et des pistes d’amélioration.
- Présenter les indicateurs statistiques et KPI pertinents sur les films.
- Créer un système de recommandation de film en utilisant des algorithmes de machine learning et faire une démonstration de ces recommandations sur des films proposés en séance par le client.
  
2. Livrables
- Un notebook contenant l’exploration et le nettoyage des données ainsi que les visualisations. Vous expliquerez vos choix de nettoyage et vos conclusions d’exploration dans un document de votre choix.
- Un dashboard présentant les KPI pertinents.
- Un notebook pour l’étape Système de recommandation avec le code source avec vos commentaires.

