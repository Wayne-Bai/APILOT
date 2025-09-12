
import numpy as np

# Create a symmetric matrix
matrix = np.array([[1, 5, 3],
                   [5, 2, 4],
                   [3, 4, 6]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(matrix)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
