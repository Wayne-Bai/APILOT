from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate some random sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=0)

# Create an instance of the AgglomerativeClustering class
clf = AgglomerativeClustering(n_clusters=4)

# Fit the data to the model
clf.fit(X)

# Get the cluster labels for the data
labels = clf.labels_

# Plot the data with the cluster labels
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.show()
