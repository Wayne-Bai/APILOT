import numpy as np

def eigenvalues_eigenvectors(matrix):
    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvalues, eigenvectors

# Example matrix (symmetric matrix)
A = np.array([[2, 1, 0], 
              [1, 3, 1],
              [0, 1, 2]])

# Get eigenvalues and eigenvectors
eigenvals, eigenvecs = eigenvalues_eigenvectors(A)

print("Eigenvalues:", eigenvals)
print("Eigenvectors:", eigenvecs)
