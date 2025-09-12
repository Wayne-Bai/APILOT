import numpy as np

# Define a complex Hermitian or real symmetric matrix
matrix = np.array([[1+2j, 3+4j], [3-4j, 5-2j]], dtype=complex)

# Extract the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
