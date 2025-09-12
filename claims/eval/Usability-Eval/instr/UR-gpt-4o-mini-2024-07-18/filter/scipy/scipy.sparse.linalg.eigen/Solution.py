import numpy as np
from scipy.linalg import eigh

def compute_eigenvalues_eigenvectors(A, k):
    """
    Compute k eigenvalues and eigenvectors of the square matrix A.
    
    Parameters:
    A (np.ndarray): A square matrix.
    k (int): Number of eigenvalues and eigenvectors to return.
    
    Returns:
    eigenvalues (np.ndarray): The k largest eigenvalues.
    eigenvectors (np.ndarray): The corresponding eigenvectors.
    """
    # Ensure A is a square matrix
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    
    # Compute all eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eigh(A)
    
    # Get the k largest eigenvalues and corresponding eigenvectors
    idx = np.argsort(eigenvalues)[-k:]  # Indices of the k largest eigenvalues
    return eigenvalues[idx], eigenvectors[:, idx]

# Example usage:
A = np.array([[4, -2], [1, 1]])
k = 1
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(A, k)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
