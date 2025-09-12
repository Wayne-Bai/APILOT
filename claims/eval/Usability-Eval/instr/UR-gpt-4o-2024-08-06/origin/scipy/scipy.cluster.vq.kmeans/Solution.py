import numpy as np
from scipy.spatial.distance import cdist

def kmeans(data, k, num_iterations=100):
    # Randomly choose initial centroids
    rand_indices = np.random.choice(data.shape[0], k, replace=False)
    centroids = data[rand_indices]
    
    for _ in range(num_iterations):
        # Compute distances from each point to each centroid
        distances = cdist(data, centroids, 'euclidean')
        
        # Assign each point to the nearest centroid
        closest_centroids = np.argmin(distances, axis=1)
        
        # Update centroids by taking the mean of assigned points
        for i in range(k):
            points_assigned_to_centroid = data[closest_centroids == i]
            if len(points_assigned_to_centroid) > 0:
                centroids[i] = np.mean(points_assigned_to_centroid, axis=0)
                
    return centroids, closest_centroids

# Example usage:
data = np.array([
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0],
    [8.0, 2.0],
    [10.0, 2.0],
    [9.0, 3.0],
])

k = 3
centroids, labels = kmeans(data, k)
print("Centroids:\n", centroids)
print("Labels:", labels)
