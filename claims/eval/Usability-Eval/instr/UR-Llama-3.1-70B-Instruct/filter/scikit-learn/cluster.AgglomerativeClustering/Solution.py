# Import necessary libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data (moon-shaped)
X, _ = make_moons(n_samples=200, noise=0.05)

# Define Agglomerative Clustering model
model = AgglomerativeClustering(
    n_clusters=2,  # number of clusters
    affinity='euclidean',  # 'euclidean', 'l1', 'l2','manhattan', 'cosine'
    memory=None,
    connectivity=None,
    compute_full_tree='auto',  # Compute the full tree if compute_full_tree='auto' and n_clusters is less than 128
    linkage='ward',  # which linkage criterion to use. It can be "ward", "complete", or "average"
    distance_threshold=None
)

# Fit model
model.fit(X)

# Get cluster labels
labels = model.labels_

# Plot clusters
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.title('Agglomerative Clustering')
plt.show()
