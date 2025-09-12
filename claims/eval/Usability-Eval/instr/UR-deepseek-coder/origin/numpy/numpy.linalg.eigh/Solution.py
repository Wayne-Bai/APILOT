import numpy as np

def eig_hermitian(matrix):
    # Ensure the matrix is Hermitian (conjugate symmetric) or real symmetric
    if not np.allclose(matrix, np.conj(matrix).T):
        raise ValueError("The input matrix must be Hermitian (conjugate symmetric) or real symmetric.")
    
    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    
    return eigenvalues, eigenvectors

# Example usage:
# A = np.array([[1, 2+3j], [2-3j, 4]])
# eigenvalues, eigenvectors = eig_hermitian(A)
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:", eigenvectors)
