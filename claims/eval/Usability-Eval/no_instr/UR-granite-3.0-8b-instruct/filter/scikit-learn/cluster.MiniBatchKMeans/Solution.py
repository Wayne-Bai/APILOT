from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
import numpy as np

# Generate some random data for demonstration purposes
X, _ = make_blobs(n_samples=1000, centers=5, random_state=42)

# Initialize the MiniBatchKMeans model
mbk = MiniBatchKMeans(n_clusters=5, random_state=42)

# Fit the model to the data
mbk.fit(X)

# Get the cluster labels for each data point
labels = mbk.labels_

# Get the cluster centers
centers = mbk.cluster_centers_

# Print the cluster labels and centers
print("Cluster labels:", labels)
print("Cluster centers:", centers)
