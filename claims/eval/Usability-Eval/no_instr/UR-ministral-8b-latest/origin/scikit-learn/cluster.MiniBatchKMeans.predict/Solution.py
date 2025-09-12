from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import numpy as np

# Generate some sample data
X, _ = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define the KMeans algorithm
kmeans = KMeans(n_clusters=4, random_state=42)

# Fit the model to the data
kmeans.fit(X_scaled)

# Predict the closest cluster for each sample
clusters = kmeans.predict(X_scaled)

# Print the cluster labels
print(clusters)
