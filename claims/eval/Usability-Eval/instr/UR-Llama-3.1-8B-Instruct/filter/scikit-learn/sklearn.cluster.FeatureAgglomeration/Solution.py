# Import necessary libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Generate random sample data with 3 features and 100 samples
X, _ = make_blobs(n_samples=100, centers=4, n_features=3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform Agglomerative clustering
agglo = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
agglo.fit(X_scaled)

# Get the cluster labels
labels = agglo.labels_

# Print the silhouette coefficient
print("Silhouette Coefficient:", silhouette_score(X_scaled, labels, metric='euclidean'))

# Plot the clusters
plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.scatter(agglo.cluster_centers_[:, 0], agglo.cluster_centers_[:, 1], c='red', s=200, label='Centroids')
plt.legend()
plt.show()
