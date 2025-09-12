
from scipy.cluster.vq import kmeans

# Generate observations (replace with actual observations)
observations = np.random.rand(100, 2)

# Perform k-means clustering with k clusters
k = 3  # Number of clusters
centroids, distortion = kmeans(observations, k)

print("Cluster centroids:")
print(centroids)
print("Distortion (sum of squared distances to nearest centroid):", distortion)
