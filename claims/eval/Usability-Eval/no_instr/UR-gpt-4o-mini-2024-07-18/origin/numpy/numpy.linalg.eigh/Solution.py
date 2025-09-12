import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    # Ensure the matrix is either Hermitian or symmetric
    if not (np.allclose(matrix, matrix.conj().T) or np.allclose(matrix, matrix.T)):
        raise ValueError("Input matrix must be a Hermitian or symmetric matrix.")

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    return eigenvalues, eigenvectors

# Example usage:
# Create a 2x2 Hermitian matrix
hermitian_matrix = np.array([[1, 2 + 1j], [2 - 1j, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(hermitian_matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
