import numpy as np

# Generate a random 3x3 matrix
A = np.random.rand(3, 3)

# Perform SVD on the matrix A
U, s, V = np.linalg.svd(A)

# Print the singular values
print("Singular values of A:")
print(s)
