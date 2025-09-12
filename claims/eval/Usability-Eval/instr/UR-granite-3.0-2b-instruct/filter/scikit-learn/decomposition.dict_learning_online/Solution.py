from sklearn.decomposition import MiniBatchKMeans
import numpy as np

# Assuming you have a dictionary learning matrix factorization problem
# and you want to solve it online using MiniBatchKMeans

# Generate a random dictionary and data matrix
np.random.seed(0)
D = np.random.randn(100, 50)
X = np.dot(np.random.randn(100, 10), D) + np.random.randn(100, 10)

# Initialize MiniBatchKMeans with the desired number of clusters
mbk = MiniBatchKMeans(n_clusters=10, random_state=0)

# Fit the model to the data using mini-batches
mbk.fit(X)

# Get the cluster labels for each data point
labels = mbk.labels_

# Get the cluster centers
centers = mbk.cluster_centers_

# Print the first 5 data points and their assigned clusters
for i in range(5):
    print(f"Data point {i}: {X[i]} - Cluster: {labels[i]}")

# Print the first 5 cluster centers
print("\nCluster centers:")
for i in range(5):
    print(f"Center {i}: {centers[i]}")
