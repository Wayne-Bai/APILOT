import numpy as np
from scipy.cluster.k_means import KMeans

# Generate random data
np.random.seed(0)
X = np.random.rand(100, 2)

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Get the cluster labels
labels = kmeans.labels_

# Get the cluster centers
centers = kmeans.cluster_centers_