from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Example usage of Mini-Batch K-Means clustering

# Number of clusters and number of initial clusters
n_clusters = 3
n_initial_clusters = 4

# Sample data for clustering
data = np.random.rand(100, 2)  # 100 samples, 2 features each

# Initialize and fit the Mini-Batch K-Means model
mbkmeans = MiniBatchKMeans(n_clusters=n_clusters, n_init=n_initial_clusters, batch_size=10)
mbkmeans.fit(data)

# Get the cluster labels
cluster_labels = mbkmeans.labels_

# Print the number of clusters, initial clusters, and the cluster labels
print(f"Number of clusters: {n_clusters}")
print(f"Number of initial clusters: {n_initial_clusters}")
print(f"Cluster labels: {cluster_labels}")
