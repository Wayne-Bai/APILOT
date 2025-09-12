import torch
import numpy as np

# Define the function to compute the numerical rank
def numerical_rank(A, tol=1e-8):
    """
    Compute the numerical rank of a matrix A.
    
    Parameters:
    A (torch.Tensor): Input matrix
    tol (float): Tolerance value default is 1e-8
    
    Returns:
    int: Numerical rank of the matrix
    """
    # Compute the SVD decomposition of the matrix
    U, s, V = torch.svd(A)
    
    # Find the rank of the matrix by finding the threshold at which the singular values become very small
    rank = len(s[s > tol])
    
    return rank

# Example usage:
A = torch.randn(3, 4)
print("Matrix A:")
print(A)
print("Numerical rank of A:", numerical_rank(A))
