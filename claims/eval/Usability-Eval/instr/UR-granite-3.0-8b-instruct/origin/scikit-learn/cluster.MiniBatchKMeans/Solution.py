from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate some sample data
X, _ = make_blobs(n_samples=300, centers=5, random_state=0)

# Initialize the MiniBatchKMeans algorithm
mbk = MiniBatchKMeans(n_clusters=5, random_state=0)

# Fit the algorithm to the data
mbk.fit(X)

# Get the cluster labels for each sample
labels = mbk.labels_

# Get the cluster centers
centers = mbk.cluster_centers_

# Plot the data and the cluster centers
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.show()
