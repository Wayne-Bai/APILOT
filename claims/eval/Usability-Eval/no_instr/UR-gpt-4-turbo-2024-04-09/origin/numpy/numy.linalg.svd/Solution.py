import numpy as np

# Sample matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the Singular Value Decomposition
U, s, Vt = np.linalg.svd(A, full_matrices=False)

print("U matrix:")
print(U)
print("\nSingular values:")
print(s)
print("\nV transpose matrix:")
print(Vt)
