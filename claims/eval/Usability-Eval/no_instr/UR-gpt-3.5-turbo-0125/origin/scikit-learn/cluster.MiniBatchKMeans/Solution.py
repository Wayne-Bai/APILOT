
from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Create some data points for demonstration
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Initialize Mini-Batch K-Means with 2 clusters
kmeans = MiniBatchKMeans(n_clusters=2, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Get cluster assignments for each data point
labels = kmeans.labels_

# Get cluster centers
cluster_centers = kmeans.cluster_centers_

print("Cluster Assignments:", labels)
print("Cluster Centers:", cluster_centers)
