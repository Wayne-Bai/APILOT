import numpy as np
from sklearn.cluster import KMeans

# Example data
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Number of clusters
k = 2

# Create and fit the KMeans model
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Predict the cluster for each sample in X
labels = kmeans.labels_

print("Cluster labels for each sample in X:")
print(labels)
