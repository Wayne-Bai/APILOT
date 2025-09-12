import numpy as np
from sklearn.metrics.pairwise import manhattan_distances

# Example data
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[1, 2, 3], [7, 8, 9]])

# Compute L1 distances
distances = manhattan_distances(X, Y)

print(distances)
