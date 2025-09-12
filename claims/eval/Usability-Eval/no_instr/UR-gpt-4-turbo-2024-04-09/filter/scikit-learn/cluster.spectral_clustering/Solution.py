import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_moons

# Generate synthetic data: two interleaving half circles
X, y = make_moons(n_samples=200, noise=0.07, random_state=42)

# Applying Spectral Clustering to normalized Laplacian
n_clusters = 2  # Example: 2 clusters
clustering = SpectralClustering(n_clusters=n_clusters,
                                assign_labels='kmeans',
                                random_state=42)

# Fit & predict clusters
labels = clustering.fit_predict(X)

# Visualization (Optional)
import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
plt.title('Clusters from Spectral Clustering')
plt.show()
