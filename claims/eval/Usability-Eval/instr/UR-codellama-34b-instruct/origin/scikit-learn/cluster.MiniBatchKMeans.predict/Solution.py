
import numpy as np
from sklearn.cluster import KMeans

# Initialize the KMeans algorithm with the number of clusters you want to create
kmeans = KMeans(n_clusters=3)

# Fit the data to the model
kmeans.fit(X)

# Get the cluster labels for each sample in X
cluster_labels = kmeans.labels_
