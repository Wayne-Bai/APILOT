import numpy as np

# Create a matrix for which SVD is to be performed
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

# U, S, VT contain the singular value decomposition
print("U matrix:\n", U)
print("Singular values:\n", S)
print("VT matrix:\n", VT)
