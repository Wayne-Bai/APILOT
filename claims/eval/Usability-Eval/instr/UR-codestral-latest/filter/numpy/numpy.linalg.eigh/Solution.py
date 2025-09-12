import numpy as np

# Define a complex Hermitian matrix for demonstration
matrix = np.array([[1, 1j, 2], [-1j, 2, -3], [2, -3, 4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
