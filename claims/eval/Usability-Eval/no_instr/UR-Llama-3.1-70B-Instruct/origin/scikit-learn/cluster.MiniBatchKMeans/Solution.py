# Import necessary libraries
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
n_samples = 1000
n_features = 2
n_clusters = 5

# Create a sample dataset
X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, n_features=n_features, random_state=0)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Define Mini-Batch K-Means model
mbk = MiniBatchKMeans(init='k-means++', n_clusters=n_clusters, batch_size=100, n_init=10, random_state=0)

# Fit the model
mbk.fit(X_std)

# Get predicted cluster labels
labels = mbk.labels_

# Get cluster centers
cluster_centers = mbk.cluster_centers_

# Plot clusters
plt.figure(figsize=(8, 8))
plt.scatter(X_std[:, 0], X_std[:, 1], c=labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, alpha=0.5)
plt.show()
