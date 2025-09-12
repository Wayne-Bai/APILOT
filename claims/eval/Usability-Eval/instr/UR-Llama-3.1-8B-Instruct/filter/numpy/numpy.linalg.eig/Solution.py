import numpy as np

# Define a square array
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors of the array
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
