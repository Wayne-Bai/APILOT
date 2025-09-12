
import numpy as np

# Define a square matrix A
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors of A
evals, evecs = np.linalg.eig(A)

# Print the eigenvalues
print("Eigenvalues:", evals)

# Print the right eigenvectors
print("Right eigenvectors:", evecs)
