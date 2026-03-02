# [cite_start]Projet Final : Segmentation des Modes de Vie Urbains [cite: 1]

[cite_start]Ce projet simule un environnement de travail collaboratif en Data Science, reposant sur l'utilisation de Git pour la gestion du développement et de Docker pour la conteneurisation des résultats[cite: 5, 7]. [cite_start]L'objectif est d'analyser un jeu de données de villes à travers différentes méthodes de réduction de dimension[cite: 6].

## [cite_start]Structure du Repertoire [cite: 12]

[cite_start]L'organisation du projet respecte l'arborescence suivante pour garantir la clarté des contributions[cite: 13]:

* [cite_start]**data/** : Contient le jeu de données initial (city_lifestyle_dataset.csv)[cite: 14].
* [cite_start]**notebooks/** : Regroupe les fichiers Jupyter d'exploration pour chaque méthode (pca.ipynb, tsne.ipynb, umap.ipynb)[cite: 15].
* [cite_start]**outputs/** : Contient les exports des projections en 2 dimensions au format CSV (pca_emb_2d.csv, tsne_emb_2d.csv, umap_emb_2d.csv)[cite: 18, 19, 20].
* [cite_start]**evaluate.py** : Script Python dédié au calcul de la métrique de performance[cite: 16, 50].
* [cite_start]**Dockerfile** : Fichier de configuration pour la création de l'image Docker[cite: 21, 52].
* [cite_start]**README.md** : Documentation générale du projet[cite: 23].

## [cite_start]Methodes de Reduction de Dimension [cite: 31]

[cite_start]Chaque méthode a été implémentée dans une branche dédiée à partir de la branche principale[cite: 32, 33]:

* [cite_start]**PCA (Analyse en Composantes Principales)**[cite: 33].
* [cite_start]**t-SNE (t-Distributed Stochastic Neighbor Embedding)**[cite: 33].
* [cite_start]**UMAP (Uniform Manifold Approximation and Projection)**[cite: 33].

[cite_start]Chaque notebook contient la projection des données en 2 dimensions, une visualisation graphique, une observation sur la structure obtenue et l'export des données réduites[cite: 36, 37].

## [cite_start]Evaluation : Trustworthiness [cite: 38, 41]

[cite_start]La comparaison des méthodes s'appuie sur la métrique de **trustworthiness**[cite: 40].
* [cite_start]Cette métrique mesure dans quelle mesure les relations de voisinage de l'espace original sont préservées dans l'espace réduit[cite: 42].
* [cite_start]Une valeur proche de 1 indique une excellente conservation de la structure locale[cite: 45].
* [cite_start]Le script `evaluate.py` charge les fichiers CSV du dossier outputs et affiche les scores pour chaque méthode[cite: 50].

## [cite_start]Workflow Git et Collaboration [cite: 5]

[cite_start]Le développement a suivi une méthodologie collaborative stricte[cite: 12]:
* [cite_start]**Gestion des branches** : Utilisation de branches nommées selon la fonctionnalité (ex: method/PCA, method/T-SNE, feat/docker)[cite: 24, 25, 26, 28].
* [cite_start]**Commits** : Chaque branche contient au moins 2 commits[cite: 10].
* [cite_start]**Pull Requests** : Les contributions ont été fusionnées dans la branche main via des Pull Requests après validation[cite: 11].

## [cite_start]Utilisation avec Docker [cite: 51]

[cite_start]Le projet est conteneurisé pour permettre l'exécution du script de comparaison directement depuis la branche main[cite: 53].

Execution du script
Bash
docker run --rm projet-final-ds
Developpement avec volumes (Bonus) 

Pour permettre la mise à jour du code ou des données sans reconstruire l'image, ou pour travailler en local avec l'environnement Docker, un volume peut être monté :

Bash
docker run --rm -v $(pwd):/app projet-final-ds

Souhaitez-vous que je vous aide à présent pour la rédaction du `Dockerfile` ou pour compléter les o
### Construction de l'image
```bash
docker build -t projet-final-ds .
