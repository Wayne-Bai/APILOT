
from sklearn.cluster import KMeans
import numpy as np

# Generate some random data for illustration purposes
X = np.random.rand(10, 5)

# Initialize a KMeans object with 3 clusters
kmeans = KMeans(n_clusters=3).fit(X)

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Predict the closest cluster for each sample in X
closest_clusters = np.argmin(np.linalg.norm(X - centroids, axis=1), axis=0)

# Print the result
print("Closest clusters:", closest_clusters)
