import torch

def matrix_rank(A, tol=1e-10):
    """
    Computes the numerical rank of a matrix A using its singular values.

    Parameters:
        A (torch.Tensor): The input matrix.
        tol (float): The tolerance for determining the rank. Singular values smaller
                      than this value are considered zero.

    Returns:
        int: The numerical rank of the matrix.
    """
    # Compute the singular value decomposition
    _, S, _ = torch.svd(A)

    # Check how many singular values are greater than the tolerance
    rank = torch.sum(S > tol).item()
    
    return rank

# Example Usage:
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
rank = matrix_rank(A)

print("The numerical rank of the matrix is:", rank)
