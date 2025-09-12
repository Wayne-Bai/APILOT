import numpy as np

def get_eigenvalues_and_eigenvectors(matrix):
    # Perform the eigenvalues and eigenvectors computation using the more modern numpy.linalg routines.
    eigenvalues, eigenvectors = np.linalg.eigh(matrix) if matrix.iscomplex() else np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    A = np.array([[4, -1+2j], [-1-2j, 5]], dtype=complex)  # Example complex Hermitian matrix
    B = np.array([[4, 1], [1, 5]])  # Example real symmetric matrix

    eigenvalues_A, eigenvectors_A = get_eigenvalues_and_eigenvectors(A)
    eigenvalues_B, eigenvectors_B = get_eigenvalues_and_eigenvectors(B)

    print("Eigenvalues of A and eigenvectors of A:")
    print("Eigenvalues: ", eigenvalues_A)
    print("Eigenvectors: ", eigenvectors_A)

    print("\nEigenvalues of B and eigenvectors of B:")
    print("Eigenvalues: ", eigenvalues_B)
    print("Eigenvectors: ", eigenvectors_B)
