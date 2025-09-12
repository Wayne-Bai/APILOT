from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic data
X, _ = make_blobs(n_samples=1000, centers=5, n_features=2, random_state=42)

# Initialize the MiniBatchKMeans model
mbk = MiniBatchKMeans(n_clusters=5, random_state=42)

# Fit the model to the data
mbk.fit(X)

# Get the cluster labels and cluster centers
labels = mbk.labels_
centers = mbk.cluster_centers_

# Plot the data points and cluster centers
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.show()
