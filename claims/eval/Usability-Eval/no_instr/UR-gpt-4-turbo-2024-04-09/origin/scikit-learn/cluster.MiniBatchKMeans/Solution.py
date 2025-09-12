import numpy as np
from sklearn.cluster import MiniBatchKMeans

# Example data
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Initialize MiniBatch K-Means
mb_kmeans = MiniBatchKMeans(n_clusters=2, batch_size=6)

# Fit the model
mb_kmeans.fit(X)

# Predict cluster indices for the data points
clusters = mb_kmeans.predict(X)

print("Cluster indices:", clusters)
