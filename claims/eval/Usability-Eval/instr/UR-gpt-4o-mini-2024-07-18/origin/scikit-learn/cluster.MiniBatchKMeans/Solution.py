import numpy as np
from sklearn.cluster import KMeans

# Generate synthetic data for clustering
X = np.random.rand(100, 2)  # 100 samples with 2 features

# Define the number of clusters
n_clusters = 3

# Create a KMeans instance with the desired number of clusters
kmeans = KMeans(n_clusters=n_clusters, batch_size=10, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

print("Cluster Labels:\n", labels)
print("Cluster Centers:\n", centers)
