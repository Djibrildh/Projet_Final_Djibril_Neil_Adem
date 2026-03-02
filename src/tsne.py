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
