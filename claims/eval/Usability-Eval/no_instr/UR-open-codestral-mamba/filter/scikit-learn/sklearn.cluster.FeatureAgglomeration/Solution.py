# Import the necessary libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

# Generate some blobs for demonstration purposes
n_samples = 1000
n_features = 20
n_clusters = 5

X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters)

# Initialize the AgglomerativeClustering class
clustering = AgglomerativeClustering()

# Fit the data to the model
clusters = clustering.fit_predict(X)

# The variable 'clusters' now contains the cluster labels for each sample
