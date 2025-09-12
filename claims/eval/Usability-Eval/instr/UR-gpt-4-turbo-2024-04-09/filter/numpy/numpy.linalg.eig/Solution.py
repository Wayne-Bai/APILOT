import numpy as np

# Define a square matrix
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors using numpy's linalg.eig function
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
