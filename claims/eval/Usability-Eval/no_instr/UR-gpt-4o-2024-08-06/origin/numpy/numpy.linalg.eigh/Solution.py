import numpy as np

# Define a complex Hermitian or a real symmetric matrix
matrix = np.array([[2, -1j], [1j, 3]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(matrix)

# Return the eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
