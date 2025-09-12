from sklearn.metrics.pairwise import manhattan_distances
import numpy as np

# Assuming X and Y are NumPy arrays
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

# Compute L1 distances between the vectors in X and Y
distances = manhattan_distances(X, Y)
print(distances)
