from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Sample data generation
data = np.random.rand(100, 2)  # 100 samples, 2 features

# Parameters
num_clusters = 3
batch_size = 10

# Create MiniBatchKMeans instance
kmeans = MiniBatchKMeans(n_clusters=num_clusters, batch_size=batch_size)

# Fit the model
kmeans.fit(data)

# Get the cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Print the results
print("Cluster Centers:\n", centers)
print("Labels:\n", labels)
