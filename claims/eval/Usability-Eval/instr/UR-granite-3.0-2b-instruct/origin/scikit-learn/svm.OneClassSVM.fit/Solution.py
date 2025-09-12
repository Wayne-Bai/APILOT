from sklearn.cluster import KMeans
import numpy as np

# Assuming X is your dataset and it's a 2D numpy array
# X = np.random.rand(100, 2)

# Choose the number of clusters (soft boundary)
n_clusters = 3

# Initialize KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=0)

# Fit the model
kmeans.fit(X)

# Get the cluster labels for each sample
labels = kmeans.labels_

# The soft boundary can be defined as the point where the label changes
# We can find this point by finding the index where the labels change
change_index = np.where(np.diff(labels) != 0)[0][0]

# The soft boundary is then the sample at this index
soft_boundary = X[change_index]
