import numpy as np
from sklearn.cluster import KMeans

# Sample data
X = np.array([[1.0, 2.0],
              [1.5, 1.8],
              [5.0, 8.0],
              [8.0, 8.0],
              [1.0, 0.6],
              [9.0, 11.0]])

# Create a KMeans model
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample belongs to
clusters = kmeans.predict(X)

print("Cluster assignments for each sample:", clusters)
