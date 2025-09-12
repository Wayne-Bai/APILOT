import numpy as np

# Assuming 'matrix' is your square array
matrix = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
