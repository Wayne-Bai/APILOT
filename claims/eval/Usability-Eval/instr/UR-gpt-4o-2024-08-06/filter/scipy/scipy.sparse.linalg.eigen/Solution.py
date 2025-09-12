import numpy as np
from scipy.linalg import eig

# Define the square matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Number of eigenvalues and eigenvectors to find
k = 2

# Compute eigenvalues and right eigenvectors
eigenvalues, eigenvectors = eig(A)

# Sort the eigenvalues and associated eigenvectors
# Sort eigenvalues in descending order and get indices
sorted_indices = np.argsort(-np.abs(eigenvalues))

# Select the first k eigenvalues and eigenvectors
selected_eigenvalues = eigenvalues[sorted_indices[:k]]
selected_eigenvectors = eigenvectors[:, sorted_indices[:k]]

# Print the results
print("Selected Eigenvalues:\n", selected_eigenvalues)
print("Selected Eigenvectors:\n", selected_eigenvectors)
