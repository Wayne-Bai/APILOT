from sklearn.cluster import KMeans

# Sample data
X = [[1, 2], [1, 4], [1, 0],
     [10, 2], [10, 4], [10, 0]]

# Number of clusters
k = 2

# Initialize the KMeans object
kmeans = KMeans(n_clusters=k, random_state=0)

# Fitting the model
kmeans.fit(X)

# Predicting the closest cluster each sample in X belongs to
closest_clusters = kmeans.predict(X)

print("Closest clusters:", closest_clusters)
