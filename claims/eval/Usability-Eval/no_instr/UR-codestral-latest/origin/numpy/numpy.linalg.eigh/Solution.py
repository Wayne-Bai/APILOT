import numpy as np

# Define your matrix
matrix = np.array([[1, 2j], [-2j, 3]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues and eigenvectors
print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
