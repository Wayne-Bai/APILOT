# Import necessary libraries
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
centers = [(1, 1), (5, 5), (4, 8)]
X, _ = make_blobs(n_samples=500, centers=centers, cluster_std=1.0, random_state=42)

# Reshape the data (optional)
X = X.reshape(-1, 2)

# Perform Mini-Batch K-Means clustering
mbk = MiniBatchKMeans(n_clusters=3, init='k-means++', max_iter=100, batch_size=100, random_state=42)
mbk.fit(X)

# Get cluster labels for each data point
labels = mbk.labels_

# Create a list of unique cluster labels
unique_labels = np.unique(labels)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(mbk.cluster_centers_[:, 0], mbk.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)

# Show the plot
plt.show()

# Print the cluster centers
print(mbk.cluster_centers_)
