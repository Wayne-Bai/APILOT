import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

class MiniBatchKMeans:
    def __init__(self, n_clusters=8, max_iter=100, batch_size=100, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.batch_size = batch_size
        self.random_state = random_state
        self.cluster_centers_ = None

    def partial_fit(self, X):
        if self.cluster_centers_ is None:
            initial_idx = np.random.choice(len(X), self.n_clusters, replace=False)
            self.cluster_centers_ = X[initial_idx]

        for _ in range(self.max_iter):
            batch_indices = np.random.choice(len(X), self.batch_size, replace=False)
            batch_data = X[batch_indices]

            # Assign labels
            distances = np.linalg.norm(batch_data[:, np.newaxis] - self.cluster_centers_, axis=2)
            labels = np.argmin(distances, axis=1)

            # Update cluster centers
            for i in range(self.n_clusters):
                points_for_cluster = batch_data[labels == i]
                if len(points_for_cluster) > 0:
                    self.cluster_centers_[i] = points_for_cluster.mean(axis=0)

    def fit(self, X):
        X = shuffle(X, random_state=self.random_state)
        self.partial_fit(X)

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.cluster_centers_, axis=2)
        return np.argmin(distances, axis=1)

# Usage
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=1000, centers=4, random_state=42)

mbkm = MiniBatchKMeans(n_clusters=4, batch_size=20, max_iter=10, random_state=42)
mbkm.fit(X)
cluster_labels = mbkm.predict(X)

print("Cluster centers:\n", mbkm.cluster_centers_)
print("Cluster labels for the first 10 samples:\n", cluster_labels[:10])
