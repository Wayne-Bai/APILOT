from sklearn.cluster import KMeans

# Initialize the KMeans clustering algorithm with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the KMeans model to the data in X
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
closest_cluster = kmeans.predict(X)
