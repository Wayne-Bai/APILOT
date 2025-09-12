
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# load the dataset
X = ... # your data goes here

# scale the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# perform k-means clustering on the scaled data
kmeans = KMeans(n_clusters=2, random_state=0).fit(X_scaled)

# find the soft boundary of the clusters using the epsilon parameter in KMeans
epsilon = 1e-5
distance_matrix = np.zeros((kmeans.labels_.size, kmeans.labels_.size))
for i in range(kmeans.labels_.size):
    for j in range(i+1, kmeans.labels_.size):
        distance_matrix[i, j] = np.min([np.linalg.norm(X_scaled[kmeans.labels_[i]] - X_scaled[kmeans.labels_[j]]), 2*epsilon])
distance_matrix += distance_matrix.T

# find the soft boundary of each cluster by taking the minimum distance to any other point in the same cluster
boundary = np.min(np.amin(distance_matrix, axis=1))

print("Soft boundary:", boundary)
