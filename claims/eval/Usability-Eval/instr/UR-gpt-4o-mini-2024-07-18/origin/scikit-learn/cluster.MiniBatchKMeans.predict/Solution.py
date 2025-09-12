from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Create KMeans model
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model
kmeans.fit(X)

# Predict the closest cluster each sample belongs to
predictions = kmeans.predict(X)

print(predictions)
