
import numpy as np
from sklearn.cluster import KMeans

# Load the data
X = ... # load your data here

# Initialize the KMeans algorithm with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predictions = kmeans.predict(X)
