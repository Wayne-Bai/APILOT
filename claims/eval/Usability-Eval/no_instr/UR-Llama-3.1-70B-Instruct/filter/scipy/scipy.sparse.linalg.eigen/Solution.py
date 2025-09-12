import scipy.linalg as la
import numpy as np

def find_eigenvalues(A, k):
    """
    Find k eigenvalues and eigenvectors of the square matrix A.

    Parameters:
    A (numpy.ndarray): square matrix
    k (int): number of eigenvalues and eigenvectors to find

    Returns:
    eigenvalues (list): k eigenvalues of A
    eigenvectors (numpy.ndarray): matrix where each column is an eigenvector of A
    """
    # Ensure A is a numpy array
    A = np.array(A)

    # Check if A is a square matrix
    assert A.shape[0] == A.shape[1], "Matrix A must be square"

    # Check if k is not larger than the size of A
    assert k <= A.shape[0], "k cannot be larger than the size of A"

    # Use eigh function from scipy.linalg to find eigenvalues and eigenvectors
    eigenvalues, eigenvectors = la.eigh(A)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Return k eigenvalues and eigenvectors
    return eigenvalues[:k], eigenvectors[:, :k]

# Example usage
if __name__ == "__main__":
    # Define a square matrix A
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Find k eigenvalues and eigenvectors of A
    k = 2
    eigenvalues, eigenvectors = find_eigenvalues(A, k)

    print("Eigenvalues: ", eigenvalues)
    print("Eigenvectors: ", eigenvectors)
