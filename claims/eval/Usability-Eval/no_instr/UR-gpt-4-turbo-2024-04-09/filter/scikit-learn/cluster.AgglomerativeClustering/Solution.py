from sklearn.cluster import AgglomerativeClustering

# Sample data
X = [[1, 2], [3, 2], [4, 4], [1, 2], [1, 3], [4, 3]]

# Create an instance of AgglomerativeClustering
# n_clusters defines the number of clusters, linkage defines the linkage criterion
agg_clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')

# Fit the model to the data
labels = agg_clustering.fit_predict(X)

print("Cluster labels:", labels)
