from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances

# Assuming X is your data and n_clusters is the number of clusters
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Get the labels for each sample in X
labels = kmeans.labels_

# Calculate the distances from each sample to the cluster centers
distances = pairwise_distances(X, kmeans.cluster_centers_)

# Find the index of the closest cluster for each sample
closest_clusters = [np.argmin(distances[i]) for i in range(len(X))]
