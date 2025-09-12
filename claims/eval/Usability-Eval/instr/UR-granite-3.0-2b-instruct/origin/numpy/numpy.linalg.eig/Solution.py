import numpy as np

# Define a square matrix
matrix = np.array([[1, 2], [3, 4]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print eigenvectors
print("Eigenvectors:")
print(eigenvectors)
