import numpy as np

# Example matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform Singular Value Decomposition
U, s, VT = np.linalg.svd(A)

# Construct the diagonal matrix S from the singular values
S = np.zeros(A.shape)
np.fill_diagonal(S, s)

# Reconstruct the original matrix A
A_reconstructed = U @ S @ VT

print("Original Matrix A:")
print(A)
print("\nU:")
print(U)
print("\nS:")
print(S)
print("\nVT:")
print(VT)
print("\nReconstructed Matrix A:")
print(A_reconstructed)
