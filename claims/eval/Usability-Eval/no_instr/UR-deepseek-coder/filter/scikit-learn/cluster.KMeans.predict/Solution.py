import numpy as np
from sklearn.cluster import KMeans

# Example data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Initialize the KMeans model with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predicted_clusters = kmeans.predict(X)

print(predicted_clusters)
