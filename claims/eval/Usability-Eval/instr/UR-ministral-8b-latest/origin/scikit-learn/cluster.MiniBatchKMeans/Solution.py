from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
import numpy as np

# Generate synthetic data
X, _ = make_blobs(n_samples=1000, centers=3, cluster_std=0.60, random_state=0)

# Define Mini-Batch K-Means
batch_size = 100
n_clusters = 3

# Initialize Mini-Batch K-Means
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=1000, n_init=10, batch_size=batch_size, verbose=True)

# Fit the model
kmeans.fit(X)

# Predict the clusters
labels = kmeans.labels_

# Calculate the silhouette score
silhouette_avg = silhouette_score(X, labels)

print(f"Silhouette Score: {silhouette_avg}")
