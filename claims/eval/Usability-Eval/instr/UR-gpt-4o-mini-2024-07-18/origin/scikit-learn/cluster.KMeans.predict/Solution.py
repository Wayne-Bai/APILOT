from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Create KMeans model
kmeans = KMeans(n_clusters=4)

# Fit the model
kmeans.fit(X)

# Predict the closest cluster each sample belongs to
closest_clusters = kmeans.labels_

# Output the result
print(closest_clusters)
