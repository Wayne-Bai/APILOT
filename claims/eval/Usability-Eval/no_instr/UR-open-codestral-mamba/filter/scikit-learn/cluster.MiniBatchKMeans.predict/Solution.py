from sklearn.cluster import KMeans
import numpy as np

# Assuming X is our data points, and k is the number of clusters.
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])
k = 2

# Initialize k-means object
kmeans = KMeans(n_clusters=k)

# Fit model with X
kmeans.fit(X)

# Labels(contains the clustering result) for each sample in X
labels = kmeans.labels_

# Cluster centers
centers = kmeans.cluster_centers_

(labels, centers)
