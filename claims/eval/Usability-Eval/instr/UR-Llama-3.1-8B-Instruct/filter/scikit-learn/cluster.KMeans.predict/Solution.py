# Import the necessary libraries
from sklearn.cluster import KMeans
import numpy as np

# Generate random data
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 samples in 2D space

# Define the KMeans model
kmeans = KMeans(n_clusters=3, random_state=0)  # 3 clusters

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
labels = kmeans.labels_

# Print the labels
print("Cluster labels for each sample in X:")
print(labels)

# To get the cluster center coordinates
centroids = kmeans.cluster_centers_
print("\nCluster center coordinates:")
print(centroids)

# Alternatively, you can use the predict method to get the cluster labels
labels_alternative = kmeans.predict(X)
print("\nCluster labels for each sample in X (alternative method):")
print(labels_alternative)
