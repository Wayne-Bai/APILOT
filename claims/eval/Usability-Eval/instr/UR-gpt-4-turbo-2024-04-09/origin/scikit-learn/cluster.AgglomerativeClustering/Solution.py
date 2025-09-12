from sklearn.cluster import AgglomerativeClustering

# Example data
X = [[0, 0], [1, 1], [1, 0], [0, 1], 
     [5, 5], [6, 6], [5, 6], [6, 5]]

# Create an instance of AgglomerativeClustering
agglomerative_clustering = AgglomerativeClustering(n_clusters=2)

# Fit and predict the labels of clusters
labels = agglomerative_clustering.fit_predict(X)

print(labels)
