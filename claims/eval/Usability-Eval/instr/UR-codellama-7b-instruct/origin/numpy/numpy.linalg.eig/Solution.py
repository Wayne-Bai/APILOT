
import numpy as np

# Define the square matrix
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors of A using NumPy
evals, evecs = np.linalg.eig(A)

print("Eigenvalues:", evals)
print("Right Eigenvectors:", evecs)
