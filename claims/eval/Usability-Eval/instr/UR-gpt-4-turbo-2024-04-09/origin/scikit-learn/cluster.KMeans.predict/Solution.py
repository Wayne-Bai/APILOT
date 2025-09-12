from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Create KMeans model
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Predict the closest cluster each sample in X belongs to
labels = kmeans.predict(X)
print(labels)
