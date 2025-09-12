import numpy as np
# Define a complex Hermitian matrix
matrix = np.array([[1, 2j], [-2j, 3]], dtype=complex)
# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
