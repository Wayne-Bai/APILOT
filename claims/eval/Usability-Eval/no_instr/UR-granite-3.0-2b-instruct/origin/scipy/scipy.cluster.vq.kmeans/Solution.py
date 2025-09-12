from scipy.cluster.vq import kmeans, vq

# Assuming X is your data matrix with shape (n_samples, n_features)
# and k is the number of clusters

# Perform k-means clustering
code, centers = kmeans(X, k)

# Encode the data points to their respective cluster centers
code, _ = vq(X, centers)
