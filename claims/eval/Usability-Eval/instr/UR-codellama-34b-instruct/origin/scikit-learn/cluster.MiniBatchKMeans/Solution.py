from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Generate some random data to cluster
X = np.random.rand(100, 10)

# Create a MiniBatchKMeans object and set the number of clusters
kmeans = MiniBatchKMeans(n_clusters=5)

# Fit the data to the model
kmeans.fit(X)

# Predict the cluster labels for the data
labels = kmeans.predict(X)

print("Cluster centers:")
print(kmeans.cluster_centers_)
print("\nLabels:")
print(labels)
