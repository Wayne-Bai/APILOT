import numpy as np

# Generate a random matrix
A = np.random.rand(4, 3)

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

# Print the results
print("Matrix A:")
print(A)
print("\nLeft singular vectors (U):")
print(U)
print("\nSingular values (S):")
print(S)
print("\nRight singular vectors (VT):")
print(VT)
