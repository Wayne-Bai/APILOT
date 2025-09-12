from sklearn.cluster import KMeans
import numpy as np

# Assume X is your data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Create a KMeans object with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(X)

# Get the labels for each sample
labels = kmeans.predict(X)

# Print the labels
print(labels)
