import numpy as np

# Example usage
A = np.array([[1, 1, 2],
              [2, 2, 1],
              [3, 2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
