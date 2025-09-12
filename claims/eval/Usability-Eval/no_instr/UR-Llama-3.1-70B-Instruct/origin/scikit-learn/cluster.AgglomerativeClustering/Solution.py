# Import necessary libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data (moons shape)
X, _ = make_moons(n_samples=200, noise=0.05)

# Create Agglomerative Clustering object with linkage distance
cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')

# Fit the model to the data
cluster.fit(X)

# Get predicted labels
labels = cluster.labels_

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title("Agglomerative Clustering")
plt.show()
