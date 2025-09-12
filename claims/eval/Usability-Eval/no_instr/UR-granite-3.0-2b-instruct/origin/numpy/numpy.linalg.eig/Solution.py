import numpy as np

# Define a square array
matrix = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:\n", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
