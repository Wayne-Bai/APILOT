from sklearn.cluster import KMeans
import numpy as np

# Example data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Create a KMeans model
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predictions = kmeans.predict(X)

print("Cluster assignments for each sample:", predictions)
