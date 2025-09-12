import numpy as np

# Define your square array (matrix)
A = np.array([[4, 3], [1, 2]])

# Compute the eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Compute the right eigenvectors
eigenvectors, _ = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:", eigenvectors)
