from scipy.cluster.vq import KMeans
import numpy as np

# Define the number of clusters (k) and the number of observations
k = 3
n_obs = 10

# Generate some random data for demonstration purposes
data = np.random.rand(n_obs, 2)

# Initialize the k-means algorithm with the specified number of clusters
kmeans = KMeans(n_clusters=k).fit(data)

# Predict the cluster assignments for each observation
labels = kmeans.predict(data)

print("Cluster assignments:")
for i in range(n_obs):
    print(f"Observation {i+1}: Cluster {labels[i]+1}")
