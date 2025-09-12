import numpy as np

# Create a random matrix
A = np.random.rand(4, 3)

# Perform Singular Value Decomposition
U, s, Vt = np.linalg.svd(A, full_matrices=False)

# Print the results
print("Matrix A:")
print(A)
print("\nU matrix:")
print(U)
print("\nSingular values (vector s):")
print(s)
print("\nVt matrix:")
print(Vt)

# Reconstruct the original matrix using U, s, and Vt
Sigma = np.diag(s)
A_reconstructed = np.dot(U, np.dot(Sigma, Vt))

print("\nReconstructed Matrix A:")
print(A_reconstructed)
