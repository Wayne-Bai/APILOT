from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=3, n_features=2, random_state=42)

# Normalize the data
X_normalized = X / np.linalg.norm(X, axis=1, keepdims=True)

# Compute the normalized Laplacian
L = np.linalg.norm(X_normalized, axis=0)[:, np.newaxis] * np.linalg.norm(X_normalized, axis=1, keepdims=True)
D = L**(-1)

# Project the Laplacian
Normalized_Laplacian = X_normalized.T @ D @ X_normalized

# Apply PCA to the projection of the normalized Laplacian
pca = PCA(n_components=2)
X_pca = pca.fit_transform(Normalized_Laplacian)

# Perform clustering using KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_pca)

print("Cluster labels:", clusters)
