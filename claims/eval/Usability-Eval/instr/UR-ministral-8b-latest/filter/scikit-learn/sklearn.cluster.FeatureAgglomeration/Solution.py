from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import numpy as np

# Generate some sample data
X, _ = make_blobs(n_samples=300, centers=20, n_features=4, random_state=42)

# Initialize Agglomerative Clustering
agglomerative = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='complete')

# Fit the model
agglomerative.fit(X)

# Get clustered labels
labels = agglomerative.labels_

# Print the labels
print(labels)
