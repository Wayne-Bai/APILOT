import numpy as np

# Create a sample matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform SVD on the matrix A
U, s, Vh = np.linalg.svd(A)

# Print the results
print("U =\n", U)
print("s =\n", s)
print("VT =\n", Vh)
