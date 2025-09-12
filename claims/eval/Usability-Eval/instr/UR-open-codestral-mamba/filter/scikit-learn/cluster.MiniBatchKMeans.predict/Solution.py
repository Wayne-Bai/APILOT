from sklearn.cluster import KMeans
import numpy as np

# Assuming we have some sample data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# We'll create a KMeans instance with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predictions = kmeans.predict(X)
print(predictions)
