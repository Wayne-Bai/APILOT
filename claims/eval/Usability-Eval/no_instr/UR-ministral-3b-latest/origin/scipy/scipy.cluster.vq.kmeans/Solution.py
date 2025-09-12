from scipy.cluster.vq import kmeans

# Assuming you have your data in a format that can be used by k-means
# For example: data is a 2D numpy array where each row is a vector/observation
data = ...
# The number of clusters
k = 5

# Perform k-means clustering
code = (centroids, labels) = kmeans(data, k)
