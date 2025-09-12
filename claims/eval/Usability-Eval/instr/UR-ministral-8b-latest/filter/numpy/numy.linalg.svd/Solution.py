import numpy as np

# Matrices for Singular Value Decomposition
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 0], [0, 1]])

# Perform Singular Value Decomposition on matrix A
U, S, Vt = np.linalg.svd(A, full_matrices=False)

print("U matrix:")
print(U)
print("\nSingular Values:")
print(S)
print("\nV transpose matrix:")
print(Vt)

# Verify the decomposition
reconstructed_A = U @ (S @ Vt)
reconstructed_B = U @ B @ Vt

print("\nReconstructed A from U, S, and V transpose:")
print(reconstructed_A)
print("\nReconstructed B from U, B, and V transpose:")
print(reconstructed_B)
