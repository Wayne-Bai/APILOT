import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvalues, eigenvectors

# testing the function
matrix = np.array([[1, 2, 3], [2, 1, 2], [3, 2, 1]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
