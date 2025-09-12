import numpy as np
from sklearn.cluster import MiniBatchKMeans

# Sample data
X = np.random.rand(100, 2)

# Define the number of clusters
n_clusters = 3

# Initialize and fit the MiniBatchKMeans
mbkm = MiniBatchKMeans(n_clusters=n_clusters, random_state=0, batch_size=20)
mbkm.fit(X)

# Predict the cluster for each data point
clusters = mbkm.predict(X)

# Print the cluster centroids
print("Cluster centroids:\n", mbkm.cluster_centers_)

# Print the cluster assignments
print("Cluster assignments:\n", clusters)
