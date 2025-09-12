from sklearn.cluster import KMeans
import numpy as np

# Assume that X is your data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Create a KMeans instance with 2 clusters: model
model = KMeans(n_clusters=2)

# Fit model to points
model.fit(X)

# Determine the cluster labels of new_points: labels (.predict() is used for this)
labels = model.predict(X)

# Print the cluster labels of the new_points
print(labels)
