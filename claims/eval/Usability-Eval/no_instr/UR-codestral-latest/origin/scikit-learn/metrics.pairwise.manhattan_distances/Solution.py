from sklearn.metrics.pairwise import manhattan_distances
import numpy as np

# Assume X and Y are your arrays
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

# Compute L1 distances
distances = manhattan_distances(X, Y)
print(distances)
