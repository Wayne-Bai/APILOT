# Import necessary libraries
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate sample data
X, y = make_blobs(n_samples=200, centers=2, n_features=2, random_state=1)

# Define the KMeans model
kmeans = KMeans(n_clusters=2, random_state=1)

# Fit the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.show()

# Calculate silhouette score to evaluate boundary softness
silhouette = metrics.silhouette_score(X, labels)
print("Silhouette Score: ", silhouette)

# To detect soft boundary, if the silhouette score is close to 0, the boundary is soft, 
# if it's close to 1, the boundary is hard and if it's close to -1, the samples are assigned
# to the wrong cluster, indicating a soft boundary.
if silhouette < 0.1:
    print("Soft boundary detected.")
else:
    print("Hard boundary detected.")
