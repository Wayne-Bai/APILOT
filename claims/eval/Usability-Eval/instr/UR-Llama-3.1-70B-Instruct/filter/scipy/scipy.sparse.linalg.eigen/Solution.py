import numpy as np
from scipy.linalg import eigh

def get_eigenvalues_and_eigenvectors(matrix, k):
    """
    Find k eigenvalues and eigenvectors of the square matrix A.

    Args:
    matrix (numpy array): A square matrix.
    k (int): The number of eigenvalues and eigenvectors to find.

    Returns:
    eigenvalues (numpy array): The k eigenvalues of the matrix.
    eigenvectors (numpy array): The k eigenvectors of the matrix.
    """
    # Check if the matrix is square
    assert matrix.shape[0] == matrix.shape[1], "Input matrix must be square"

    # Use eigh to find all eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eigh(matrix)

    # Sort eigenvalues and eigenvectors in descending order
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Select k eigenvalues and eigenvectors
    eigenvalues = eigenvalues[:k]
    eigenvectors = eigenvectors[:, :k]

    return eigenvalues, eigenvectors

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 2
eigenvalues, eigenvectors = get_eigenvalues_and_eigenvectors(matrix, k)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
