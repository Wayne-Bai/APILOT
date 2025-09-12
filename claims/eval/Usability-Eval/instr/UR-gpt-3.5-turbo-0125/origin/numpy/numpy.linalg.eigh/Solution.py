
import numpy as np

# Create a symmetric matrix
M = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(M)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
