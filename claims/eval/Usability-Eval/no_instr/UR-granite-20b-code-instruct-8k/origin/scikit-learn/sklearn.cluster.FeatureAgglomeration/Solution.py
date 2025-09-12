from sklearn.cluster import AgglomerativeClustering

# Initialize the AgglomerativeClustering object with the desired parameters
cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=0)

# Fit the data to the clusters
cluster.fit(X)

# Get the labels of the clusters
labels = cluster.labels_

# Get the number of clusters
n_clusters = len(set(labels))

# Print the results
print("Number of clusters:", n_clusters)
print("Cluster labels:", labels)
