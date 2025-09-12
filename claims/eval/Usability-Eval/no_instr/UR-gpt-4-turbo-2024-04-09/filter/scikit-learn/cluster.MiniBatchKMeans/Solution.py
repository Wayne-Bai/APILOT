import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=10000, centers=3, cluster_std=0.60, random_state=0)

# Define the Mini-Batch K-Means clustering model
mbk = MiniBatchKMeans(n_clusters=3, batch_size=100, random_state=0)

# Fit the model to the data
mbk.fit(X)

# Predict the cluster labels
labels = mbk.predict(X)

# Display the cluster centers
print("Cluster centers:", mbk.cluster_centers_)
