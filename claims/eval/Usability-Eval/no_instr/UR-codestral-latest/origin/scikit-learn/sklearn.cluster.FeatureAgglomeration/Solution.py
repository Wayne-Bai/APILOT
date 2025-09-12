from sklearn.cluster import AgglomerativeClustering

# Assuming you have a feature matrix X
# Replace 'n_clusters' with the desired number of clusters
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0)
clustering.fit(X)

# Now 'clustering.labels_' will give you the cluster assignments for each feature
print(clustering.labels_)
