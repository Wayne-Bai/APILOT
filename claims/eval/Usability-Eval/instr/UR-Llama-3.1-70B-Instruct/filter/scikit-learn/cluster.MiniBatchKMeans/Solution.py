# Import necessary libraries
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
n_samples = 1000
n_features = 2
n_clusters = 5

X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, n_features=n_features, cluster_std=0.8, random_state=0)

# Define the KMeans model
kmeans = KMeans(n_clusters=n_clusters, init="k-means++", max_iter=100)

# Fit the model on the data in mini-batches (it's handled internally by the KMeans algorithm in scikit-learn)
# We use a big batch size to simulate the previous behavior of MiniBatchKMeans
kmeans.fit(X)

# Predict cluster labels
labels = kmeans.predict(X)

# Plot the clusters
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker="*", c="red", s=200)
plt.show()
