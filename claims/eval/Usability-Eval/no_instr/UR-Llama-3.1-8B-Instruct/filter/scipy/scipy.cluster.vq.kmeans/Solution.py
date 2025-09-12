# Import necessary modules
from sklearn.cluster import KMeans
import numpy as np

# Function to generate random observation vectors
def generate_data(num_samples, num_features):
    np.random.seed(0)
    return np.random.rand(num_samples, num_features)

# Generate 200 random observation vectors in 2D space (200 samples, 2 features)
observation_vectors = generate_data(200, 2)

# Perform k-means clustering with k = 3 clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(observation_vectors)

# Get cluster labels for each observation vector
labels = kmeans.labels_

# Get cluster centers
center = kmeans.cluster_centers_

# Print cluster labels and centers
print("Cluster labels:", labels)
print("Cluster centers:\n", center)
