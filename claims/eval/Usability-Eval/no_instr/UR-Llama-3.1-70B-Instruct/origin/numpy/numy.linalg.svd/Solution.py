import numpy as np

# Generate a random matrix for demonstration
A = np.random.rand(3, 4)
print("Original Matrix A:")
print(A)

# Perform Singular Value Decomposition (SVD)
U, sigma, V = np.linalg.svd(A)

# Create a diagonal matrix from the singular values
Sigma = np.diag(sigma)

# Print the resulting matrices
print("\nMatrix U:")
print(U)
print("\nDiagonal Matrix Sigma:")
print(Sigma)
print("\nMatrix V:")
print(V)

# To verify the decomposition, we can compute A again by multiplying U, Sigma, and V
A_reconstructed = np.dot(U, np.dot(Sigma, V))
print("\nReconstructed Matrix A:")
print(A_reconstructed)

# Compute the difference between the original and reconstructed matrices to verify accuracy
diff = np.abs(A - A_reconstructed)
print("\nDifference between Original and Reconstructed Matrices:")
print(diff)
