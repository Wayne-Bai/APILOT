# Import necessary modules
from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Create a MiniBatchKMeans object
kmeans = MiniBatchKMeans(n_clusters=3, random_state=0, batch_size=6)

# Fit the data to the model
kmeans.fit(data)

# Get the cluster assignments for each data point
labels = kmeans.predict(data)

# Print locations of cluster centroids
print(kmeans.cluster_centers_)
