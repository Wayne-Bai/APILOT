import numpy as np

# Let's consider a random 3x4 matrix for SVD demonstration
A = np.random.rand(3, 4)

# Perform Singular Value Decomposition
U, s, Vt = np.linalg.svd(A, full_matrices=True)

print("Original Matrix A:")
print(A)

print("\nMatrix U (left singular vectors):")
print(U)

print("\nVector s (singular values):")
print(s)

print("\nMatrix Vt (right singular vectors, transpose):")
print(Vt)

# Reconstruct the original matrix A using SVD components
A_reconstructed = U @ np.diag(s) @ Vt

print("\nOriginal Matrix A Reconstructed using SVD components:")
print(A_reconstructed)
