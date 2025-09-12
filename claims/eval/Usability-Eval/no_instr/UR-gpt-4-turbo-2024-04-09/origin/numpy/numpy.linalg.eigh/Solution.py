import numpy as np

def eigenvalues_eigenvectors(matrix):
    # Ensuring the matrix is symmetric by checking it against its transpose
    if np.allclose(matrix, matrix.T.conj()):
        # Calculate the eigenvalues and eigenvectors using numpy's linalg.eigh function
        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        return eigenvalues, eigenvectors
    else:
        return "The provided matrix is not Hermitian or symmetric."

# Example usage:
# Define a symmetric or Hermitian matrix
A = np.array([[2, 2+1j], [2-1j, 3]])
eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
