import numpy as np

# Assuming 'A' is your square array
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
