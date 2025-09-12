import numpy as np

def get_eigenvalues_and_eigenvectors(matrix):
    # Ensure the matrix is symmetric or Hermitian
    if not (np.array_equal(matrix, matrix.conj().T) or np.array_equal(matrix, matrix.T)):
        raise ValueError("The provided matrix is not Hermitian or symmetric.")

    # Use numpy's linalg.eig function to compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    return eigenvalues, eigenvectors

# Example usage
# Create a Hermitian matrix
hermitian_matrix = np.array([[2, 1+1j], [1-1j, 3]])

eigenvalues, eigenvectors = get_eigenvalues_and_eigenvectors(hermitian_matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
