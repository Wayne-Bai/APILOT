import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data for clustering
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Define the number of clusters (k)
k = 4

# Create a KMeans instance and fit it to the data
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)

# Predict the closest cluster for each sample
labels = kmeans.predict(X)

print(labels)
