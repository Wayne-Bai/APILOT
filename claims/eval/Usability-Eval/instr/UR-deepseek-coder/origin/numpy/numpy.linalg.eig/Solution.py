import numpy as np

# Define a square array
array = np.array([[4, 1], [2, 3]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(array)

# Output the results
print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
