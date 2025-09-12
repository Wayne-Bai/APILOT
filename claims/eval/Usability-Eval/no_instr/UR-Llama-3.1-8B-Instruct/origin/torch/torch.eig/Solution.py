import torch
import numpy as np

def compute_eigendecomposition(matrix):
    """
    Computes the eigenvalue decomposition of a square matrix if it exists.
    
    Args:
    matrix (torch.Tensor): A square matrix.
    
    Returns:
    eigenvalues (torch.Tensor): A 1D tensor containing the eigenvalues.
    eigenvectors (torch.Tensor): A 2D tensor containing the eigenvectors.
    """
    
    # Check if the matrix is a square matrix
    assert matrix.shape[0] == matrix.shape[1], "Input matrix must be a square matrix"
    
    # Compute the eigenvalue decomposition
    eigenvalues, eigenvectors = torch.symeig(matrix, eigenvectors=True)
    
    return eigenvalues, eigenvectors

# Create a sample matrix
matrix = torch.tensor([[2, 1], [4, 3]])

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = compute_eigendecomposition(matrix)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: \n", eigenvectors)
