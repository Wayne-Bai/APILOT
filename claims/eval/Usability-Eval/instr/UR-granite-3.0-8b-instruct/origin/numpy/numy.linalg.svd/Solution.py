import numpy as np

# Let's assume we have a matrix A
A = np.array([[1, 2], [3, 4]])

# Perform Singular Value Decomposition
U, sigma, VT = np.linalg.svd(A)

# Print the results
print("U:")
print(U)
print("Sigma:")
print(sigma)
print("VT:")
print(VT)
