
import numpy as np
from scipy.cluster.vq import kmeans

# Generate some sample data for demonstration purposes
data = np.array([[1,2], [3,4], [5,6], [7,8], [9,10]])

# Perform k-means clustering with 2 clusters
kmeans_model = kmeans(data, 2)

# Print the cluster centers and cluster assignments
print("Cluster centers:", kmeans_model.cluster_centers_)
print("Cluster assignments:", kmeans_model.labels_)
