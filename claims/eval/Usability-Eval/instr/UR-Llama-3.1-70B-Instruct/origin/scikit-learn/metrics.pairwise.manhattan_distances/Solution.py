# Import necessary libraries
from sklearn.metrics.pairwise import manhattan_distances
import numpy as np

# Create sample vectors X and Y
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[7, 8, 9], [10, 11, 12]])

# Compute the L1 distances (Manhattan distance) between the vectors in X and Y
distances = manhattan_distances(X, Y)

# Print the computed distances
print(distances)
