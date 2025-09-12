from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Create a KMeans instance with the desired number of clusters
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
closest_clusters = kmeans.predict(X)
print("Closest clusters for each sample:", closest_clusters)
