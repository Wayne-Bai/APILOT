
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the data
X = ... # Your dataset

# Scaling the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-Means clustering with 2 clusters
kmeans = KMeans(n_clusters=2).fit(X_scaled)

# Get the cluster labels for each sample
labels = kmeans.labels_

# Compute the soft boundary between the clusters using DBSCAN algorithm
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=10).fit(X_scaled)
core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True
labels = dbscan.labels_

# Visualize the results using matplotlib
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='nipy_spectral')
plt.show()
