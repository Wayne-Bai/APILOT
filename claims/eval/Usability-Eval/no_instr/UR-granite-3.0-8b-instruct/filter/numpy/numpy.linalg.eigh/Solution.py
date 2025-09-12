import numpy as np

def eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage:
# matrix = np.array([[1, 2j], [-2j, 1]])
# eigenvalues, eigenvectors = eigenvalues_eigenvectors(matrix)
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:", eigenvectors)
