from sklearn.cluster import KMeans

# Assume X is your data and n_clusters is the number of clusters
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Get the labels for each sample in X
labels = kmeans.labels_

# Print the labels
print(labels)
