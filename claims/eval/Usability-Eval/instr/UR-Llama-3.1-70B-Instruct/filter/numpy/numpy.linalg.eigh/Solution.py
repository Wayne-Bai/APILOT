import numpy as np

def get_eigenvalues_and_eigenvectors(matrix):
    """
    This function returns the eigenvalues and eigenvectors of a complex Hermitian 
    (conjugate symmetric) or a real symmetric matrix.

    Parameters:
    matrix (numpy.ndarray): A complex Hermitian (conjugate symmetric) or a real symmetric matrix.

    Returns:
    eigenvalues (numpy.ndarray): The eigenvalues of the matrix.
    eigenvectors (numpy.ndarray): The eigenvectors of the matrix.
    """

    # Check if the matrix is Hermitian or symmetric
    if not np.allclose(matrix, matrix.conj().T):
        raise ValueError("The input matrix must be Hermitian (conjugate symmetric) or symmetric")

    # Compute the eigenvalues and eigenvectors using the np.linalg.eigh function
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)

    # Check if all eigenvalues are real (this is guaranteed for Hermitian or symmetric matrices)
    if not np.allclose(eigenvalues, eigenvalues.real):
        raise ValueError("All eigenvalues must be real")

    return eigenvalues.real, eigenvectors

# Example usage
if __name__ == "__main__":
    # Create a complex Hermitian matrix
    matrix = np.array([[1+0j, -1+2j], [-1-2j, 1+0j]])

    # Get the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = get_eigenvalues_and_eigenvectors(matrix)

    # Print the results
    print("Eigenvalues: ", eigenvalues)
    print("Eigenvectors: ", eigenvectors)

    # Create a real symmetric matrix
    matrix = np.array([[1, -1], [-1, 1]])

    # Get the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = get_eigenvalues_and_eigenvectors(matrix)

    # Print the results
    print("Eigenvalues: ", eigenvalues)
    print("Eigenvectors: ", eigenvectors)
