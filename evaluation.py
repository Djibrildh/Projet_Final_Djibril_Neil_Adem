import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import trustworthiness

# Chargement
data_path = 'data/city_lifestyle_dataset.csv'
df_original = pd.read_csv(data_path)

X_original = df_original.drop(columns=['city_name', 'country'])

scaler = StandardScaler()
X_original_scaled = scaler.fit_transform(X_original)

output_dir = 'outputs/'
results = {}


files_to_check = {
    "PCA": "pca_city_lifestyle.csv", 
    "t-SNE": "tsne_emb_2d.csv", 
    "UMAP": "umap_emb_2d.csv"
}

for method, filename in files_to_check.items():
    file_path = os.path.join(output_dir, filename)
    
    if os.path.exists(file_path):
        
        X_reduced = pd.read_csv(file_path).values
        
        
        score = trustworthiness(X_original_scaled, X_reduced, n_neighbors=10)
        results[method] = score
        print(f"{method:10} : {score:.4f}")
    else:
        print(f"{method:10} : Fichier {filename} introuvable dans {output_dir}")


if results:
    best_method = max(results, key=results.get)
    print(f"\nLa méthode la plus fidèle à la structure locale est : {best_method}")