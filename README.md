Projet Final : Segmentation des Modes de Vie Urbains
Ce projet consiste en une étude collaborative de Data Science visant à analyser et regrouper 300 villes mondiales selon des indicateurs de qualité de vie. L'objectif technique est de comparer trois méthodes de réduction de dimension (PCA, t-SNE, UMAP) en utilisant la métrique de Trustworthiness (fidélité).
Structure du Répertoire
Conformément aux exigences de l'examen, le projet est organisé de la manière suivante:
.
├── data/                       # Dataset fourni pour l'étude 
│   └── city_lifestyle_dataset.csv
├── notebooks/                  # Expérimentations par méthode 
│   ├── pca.ipynb               
│   ├── tsne.ipynb              
│   └── umap.ipynb              
├── outputs/                    # Projections 2D exportées 
│   ├── pca_emb_2d.csv
│   ├── tsne_emb_2d.csv
│   └── umap_emb_2d.csv
├── evaluate.py                 # Script de calcul de trustworthiness 
├── Dockerfile                  # Configuration pour la conteneurisation 
└── README.md                   # Documentation (ce fichier) 

Méthodologie et Workflow Git
Le développement a suivi un flux collaboratif strict basé sur des branches thématiques:
•	Branches de fonctionnalités : Chaque méthode a été développée sur une branche dédiée (method/PCA, method/T-SNE, method/UMAP).
•	Gestion des versions : Chaque branche contient au moins deux commits pour tracer l'évolution du travail.
•	Intégration : Les contributions ont été fusionnées dans la branche main via des Pull Requests.

Analyse des Réductions de Dimension
L'objectif est de projeter les 8 variables initiales du dataset vers un espace en 2 dimensions pour faciliter la visualisation.
1. PCA (Analyse en Composantes Principales)
•	Approche : Méthode linéaire cherchant à capturer le maximum de variance.
•	Observation : Utile pour voir la structure globale, mais peut écraser certains détails locaux complexes.
2. t-SNE
•	Approche : Technique non-linéaire optimisant les voisinages locaux.
•	Observation : Très efficace pour faire apparaître des clusters distincts de villes ayant des profils similaires.
3. UMAP
•	Approche : Fondée sur la géométrie riemannienne, elle préserve souvent mieux la structure globale que le t-SNE tout en étant performante sur la structure locale.
________________________________________
Évaluation (Trustworthiness)
Le script evaluate.py charge les fichiers situés dans outputs/ et calcule le score de fidélité:
•	Définition : Elle mesure si les points proches dans l'espace d'origine restent proches après réduction.
•	Interprétation : Une valeur proche de 1 indique que la structure locale est bien préservée. Une valeur faible indique une déformation importante des voisinages.

Déploiement avec Docker
Le projet est conteneurisé pour assurer une exécution reproductible du script de comparaison.
Construction de l'image
docker build -t city-segmentation-app .
Exécution du script de comparaison
docker run --rm city-segmentation-app
Options avancées (Bonus)
•	Persistance des données : Pour mettre à jour les exports sans reconstruire l'image, utilisez un volume: docker run --rm -v $(pwd)/outputs:/app/outputs city-segmentation-app
•	Développement en local : Le montage de volume permet de travailler en temps réel sur le code tout en restant dans l'environnement Docker.


