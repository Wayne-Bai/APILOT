from sklearn.cluster import KMeans

# Sample data: X is the dataset as a 2D array (list of lists)
X = [
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
]

# Create a KMeans instance with an appropriate number of clusters
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the KMeans model
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
closest_clusters = kmeans.predict(X)
print("Closest clusters for each sample:", closest_clusters)
