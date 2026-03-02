import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/city_lifestyle_dataset.csv")

# Keep only numerical columns
X = df.select_dtypes(include=[np.number])

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# t-SNE projection
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# Create dataframe for visualization
tsne_df = pd.DataFrame(X_tsne, columns=["TSNE1", "TSNE2"])

# Plot
plt.figure(figsize=(8,6))
plt.scatter(tsne_df["TSNE1"], tsne_df["TSNE2"])
plt.title("t-SNE Projection")
plt.xlabel("TSNE1")
plt.ylabel("TSNE2")
plt.show()

# Save reduced data
tsne_df.to_csv("data/tsne_output.csv", index=False)

# ==============================
# Analyse des résultats
# ==============================

# Après réduction de dimension avec t-SNE, on passe de 8 variables initiales
# à seulement 2 composantes (TSNE1 et TSNE2).

# En observant le nuage de points obtenu, on remarque que les données
# forment des groupes plus nets et mieux séparés dans l’espace 2D.

# On distingue environ 4 à 5 zones de forte densité,
# ce qui suggère l’existence de profils de villes bien différenciés.

# La réduction de dimension met donc en évidence
# des structures cachées dans les données.
'''
Après réduction de dimension avec t-SNE, on passe de 8 colonnes à 2. 
En regardant le nuage de points, on remarque que les points forment des groupes beaucoup plus nets et écartés. 
On distingue clairement 4 ou 5 fortes densités, ce qui met bien en évidence des profils de villes très différents.
'''
