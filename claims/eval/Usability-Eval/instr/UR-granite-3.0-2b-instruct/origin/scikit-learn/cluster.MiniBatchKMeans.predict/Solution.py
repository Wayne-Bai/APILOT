from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances

# Assume X is your data and n_clusters is the number of clusters
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Get the cluster labels for each sample
labels = kmeans.labels_

# Calculate the distances from each sample to the cluster centers
distances = pairwise_distances(X, kmeans.cluster_centers_)

# Find the index of the closest cluster center for each sample
closest_cluster = distances.argmin(axis=1)

# Add the closest cluster to the labels
labels = np.concatenate((labels, closest_cluster.reshape(-1, 1)), axis=1)
