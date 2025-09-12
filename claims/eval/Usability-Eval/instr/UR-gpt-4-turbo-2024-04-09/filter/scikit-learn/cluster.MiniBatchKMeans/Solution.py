from sklearn.cluster import MiniBatchKMeans

# Sample data
X = [[1, 2], [1, 4], [1, 0],
     [10, 2], [10, 4], [10, 0]]

# Initialize the MiniBatchKMeans model
n_clusters = 2
mb_kmeans = MiniBatchKMeans(n_clusters=n_clusters)

# Fit the model to the data
mb_kmeans.fit(X)

# Predicting labels for the data
labels = mb_kmeans.predict(X)

# Print cluster centers and labels
print("Cluster centers:", mb_kmeans.cluster_centers_)
print("Labels:", labels)
