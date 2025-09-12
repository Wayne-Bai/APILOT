import numpy as np

# Define a square array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute the eigenvalues and right eigenvectors of the square array
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues
print("Eigenvalues: ", eigenvalues)

# Print the right eigenvectors
print("Right Eigenvectors: \n", eigenvectors)
