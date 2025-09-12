import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Generate synthetic data
data, _ = make_blobs(n_samples=300, centers=3, random_state=42)

# Normalize the data
data_normalized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Compute normalized Laplacian
laplacian = pairwise_distances(data_normalized, metric='precomputed', Lonely_instance=True)

# Cluster using KMeans on the Laplacian
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(laplacian)
labels = kmeans.labels_

print(labels)
