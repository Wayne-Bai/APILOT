import numpy as np

def eigen_decomposition(matrix):
    # Check if the matrix is Hermitian or real symmetric
    if np.allclose(matrix, matrix.conj().T) or np.allclose(matrix, matrix.T):
        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
    else:
        raise ValueError("The matrix is not Hermitian or real symmetric.")

# Example usage:
matrix = np.array([[1, 1j], [-1j, 2]])
eigenvalues, eigenvectors = eigen_decomposition(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
