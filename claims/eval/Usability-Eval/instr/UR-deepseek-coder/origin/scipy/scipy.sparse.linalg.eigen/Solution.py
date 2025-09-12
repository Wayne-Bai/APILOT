import numpy as np
from scipy.linalg import eig

def find_k_eigenvalues_and_eigenvectors(A, k):
    # Compute the eigenvalues and eigenvectors of the matrix A
    eigenvalues, eigenvectors = eig(A)
    
    # Sort the eigenvalues and corresponding eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Select the top k eigenvalues and corresponding eigenvectors
    top_k_eigenvalues = eigenvalues[:k]
    top_k_eigenvectors = eigenvectors[:, :k]
    
    return top_k_eigenvalues, top_k_eigenvectors

# Example usage:
A = np.array([[4, 2], [2, 4]])
k = 2
eigenvalues, eigenvectors = find_k_eigenvalues_and_eigenvectors(A, k)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
