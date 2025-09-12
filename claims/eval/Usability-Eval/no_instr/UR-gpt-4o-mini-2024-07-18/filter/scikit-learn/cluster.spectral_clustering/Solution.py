import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import SpectralEmbedding
from sklearn.datasets import make_moons

# Generate synthetic data
X, _ = make_moons(n_samples=100, noise=0.1, random_state=42)

# Normalize data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Compute the normalized Laplacian and its projection using Spectral Embedding
n_components = 2
embedding = SpectralEmbedding(n_components=n_components, affinity='nearest_neighbors')
X_embedded = embedding.fit_transform(X_normalized)

# Apply KMeans clustering on the embedded data
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X_embedded)

# Plot the results
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=labels, cmap='viridis')
plt.title('KMeans Clustering on Spectral Embedding')
plt.xlabel('First Component')
plt.ylabel('Second Component')
plt.show()
