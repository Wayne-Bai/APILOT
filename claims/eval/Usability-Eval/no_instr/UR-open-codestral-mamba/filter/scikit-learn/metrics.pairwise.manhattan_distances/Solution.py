from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
Y = np.array([[2, 3], [4, 5], [6, 7]])

# Compute the L1 distances between the vectors in X and Y
distances = pairwise_distances(X, Y, metric='manhattan')

print("L1 distances between the vectors in X and Y:")
print(distances)
