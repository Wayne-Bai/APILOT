# Import necessary libraries
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate a random dataset
X, y = make_blobs(n_samples=200, centers=5, cluster_std=0.60, random_state=0)

# Initialize KMeans with 5 clusters
kmeans = KMeans(n_clusters=5, random_state=0)

# Return cluster labels for each sample in X
labels = kmeans.labels_

# Predict the closest cluster each sample in X belongs to
closest_clusters = kmeans.predict(X)

# Plot the clusters with their respective labels
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='*', label = 'Centroids')
plt.title('K-means clustering')
plt.legend()
plt.show()
