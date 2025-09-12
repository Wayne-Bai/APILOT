import scipy

# Import the necessary functions from scipy
from scipy.cluster.kmeans import KMeans

# Define the observation vectors
X = ...

# Define the number of clusters
k = ...

# Create a KMeans object with the specified number of clusters
kmeans = KMeans(n_clusters=k)

# Fit the model to the data
kmeans.fit(X)

# Get the cluster labels for each data point
labels = kmeans.labels_

# Get the cluster centers
centers = kmeans.cluster_centers_
