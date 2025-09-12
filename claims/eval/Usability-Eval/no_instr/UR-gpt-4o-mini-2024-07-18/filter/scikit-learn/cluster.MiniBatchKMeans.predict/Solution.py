from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Create a KMeans model
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster for each sample
closest_clusters = kmeans.predict(X)

print("Closest clusters for each sample:")
print(closest_clusters)
