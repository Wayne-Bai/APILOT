import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, y = make_blobs(n_samples=100, n_features=2, centers=3, cluster_std=0.5)

# Predict the closest cluster each sample in X belongs to
kmeans = KMeans(n_clusters=3).fit(X)
predicted_clusters = kmeans.predict(X)

# Print the predicted clusters
print(predicted_clusters)
