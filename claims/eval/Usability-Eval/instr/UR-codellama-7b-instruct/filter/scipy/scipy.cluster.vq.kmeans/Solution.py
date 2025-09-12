import numpy as np
import scipy.cluster.vq as vq

def k_means(data, num_clusters):
    """Performs k-means clustering on a set of observation vectors forming k clusters."""
    # Initialize the centroids randomly
    centroids = np.random.rand(num_clusters, data.shape[1])

    # Loop until the centroids converge
    while True:
        # Assign each data point to the nearest centroid
        labels = vq.vq(data, centroids)

        # Calculate the new centroids as the mean of the assigned data points
        new_centroids = np.zeros((num_clusters, data.shape[1]))
        for i in range(num_clusters):
            indices = np.where(labels == i)[0]
            new_centroids[i] = np.mean(data[indices], axis=0)

        # Check if the centroids have converged
        if np.allclose(new_centroids, centroids):
            break

        # Update the centroids
        centroids = new_centroids

    return labels