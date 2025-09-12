from sklearn.cluster import KMeans
import numpy as np

# Assuming X is your data
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Initialize the KMeans model
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Predict the closest cluster each sample in X belongs to
labels = kmeans.labels_

print("Closest cluster for each sample:", labels)
