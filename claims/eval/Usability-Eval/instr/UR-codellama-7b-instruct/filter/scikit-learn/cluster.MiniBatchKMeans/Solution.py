
import numpy as np
from sklearn.cluster import MiniBatchKMeans

# Generate random data for demonstration purposes
n_samples = 1000
n_features = 20
np.random.seed(42)
X = np.random.rand(n_samples, n_features)

# Define the number of clusters
n_clusters = 5

# Initialize the Mini-Batch K-Means model with the desired parameters
model = MiniBatchKMeans(n_clusters=n_clusters, batch_size=100)

# Fit the model to the data
model.fit(X)

# Get the cluster labels for each point in the dataset
labels = model.labels_

# Print the results
print("Cluster Labels:", labels)
print("Cluster Centers:", model.cluster_centers_)
