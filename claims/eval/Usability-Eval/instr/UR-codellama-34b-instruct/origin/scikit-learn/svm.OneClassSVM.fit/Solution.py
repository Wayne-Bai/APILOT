from sklearn.cluster import DBSCAN
import numpy as np

# Generate some random sample data
n_samples = 100
np.random.seed(0)
X = np.random.rand(n_samples, 2)

# Define the parameters for DBSCAN
eps = 0.5  # Maximum distance between samples for them to be considered neighbors
min_samples = 10  # Minimum number of samples in a cluster

# Create a DBSCAN object and fit it to the data
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
dbscan.fit(X)

# Extract the labels for each sample (cluster)
labels = dbscan.labels_
