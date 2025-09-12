from sklearn.cluster import MiniBatchKMeans

# Data preparation (example data)
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=1000, centers=5, random_state=42)

# Mini-Batch K-Means clustering
n_clusters = 5
batch_size = 100
mb_kmeans = MiniBatchKMeans(n_clusters=n_clusters, batch_size=batch_size, random_state=0)
mb_kmeans.fit(X)

# Cluster centers
print("Cluster centers:")
print(mb_kmeans.cluster_centers_)

# Predicting labels for new data points:
new_points = [[1, 2], [4, 1], [-3, 3], [5, 6]]
predicted_labels = mb_kmeans.predict(new_points)
print("Predicted labels for new points:")
print(predicted_labels)
