import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Perform Singular Value Decomposition
U, sigma, VT = np.linalg.svd(matrix)

# Print the results
print("U:\n", U)
print("Sigma:\n", sigma)
print("VT:\n", VT)
