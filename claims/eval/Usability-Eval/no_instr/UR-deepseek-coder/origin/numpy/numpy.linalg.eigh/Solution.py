import numpy as np

def eigenvalues_and_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvalues, eigenvectors

# Example usage:
# A = np.array([[1, -1], [-1, 1]])
# eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:", eigenvectors)
