import numpy as np

# Define a matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform Singular Value Decomposition
U, s, VT = np.linalg.svd(A)

# Print the results
print("U:\n", U)
print("Singular Values:\n", s)
print("VT:\n", VT)
