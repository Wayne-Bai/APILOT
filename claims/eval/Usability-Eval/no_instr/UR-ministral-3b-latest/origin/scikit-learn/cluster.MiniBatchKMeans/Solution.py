from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs

# Generate a random dataset for clustering
X, _ = make_blobs(n_samples=300, centers=5, random_state=42)

# Train the MiniBatchKMeans model
msk = MiniBatchKMeans(n_clusters=5, init='k-means++', n_init=1, random_state=42)
msk.fit(X)

# Get the cluster labels
labels = msk.labels_
