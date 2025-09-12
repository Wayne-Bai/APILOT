import torch
from torch.linalg import svd

def numerical_rank(matrix, tol=1e-6):
    """
    Computes the numerical rank of a matrix.

    Args:
    - matrix (torch.tensor): Matrix for which to compute the numerical rank.
    - tol (float, optional): Tolerance for zero singular values. Default: 1e-6.

    Returns:
    - rank (int): Numerical rank of the input matrix.
    """
    # Compute SVD of the input matrix
    u, s, vh = svd(matrix)
    
    # Compute the threshold for zero singular values
    threshold = tol * s[0]
    
    # Count the number of singular values greater than the threshold
    rank = torch.sum(s > threshold)
    
    return rank

# Example usage
if __name__ == "__main__":
    # Create a matrix
    matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

    # Compute and print the numerical rank
    rank = numerical_rank(matrix)
    print("Numerical rank:", rank)
