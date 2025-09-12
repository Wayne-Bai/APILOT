from sklearn.cluster import KMeans

# Initialize the KMeans model with the desired number of clusters
kmeans = KMeans(n_clusters=k)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster for each sample in X
labels = kmeans.labels_
