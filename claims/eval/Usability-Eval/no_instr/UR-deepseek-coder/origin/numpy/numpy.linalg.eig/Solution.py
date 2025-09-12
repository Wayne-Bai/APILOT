import numpy as np

# Example square array
A = np.array([[4, 1], [2, 3]])

# Compute eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
