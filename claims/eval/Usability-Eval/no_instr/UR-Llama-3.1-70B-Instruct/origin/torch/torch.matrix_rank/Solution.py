import torch

def numerical_rank(matrix, tol=None):
    """
    Computes the numerical rank of a matrix.

    Args:
    matrix (torch.Tensor): The input matrix.
    tol (float, optional): The tolerance for the singular values. Defaults to None.

    Returns:
    int: The numerical rank of the matrix.
    """
    # Compute the singular values of the matrix
    u, s, vh = torch.linalg.svd(matrix)

    # If tolerance is not provided, set it to the maximum singular value times the machine epsilon
    if tol is None:
        tol = s.max() * torch.finfo(s.dtype).eps

    # Count the number of singular values greater than the tolerance
    rank = torch.sum(s > tol)

    return int(rank)


# Example usage
if __name__ == "__main__":
    # Create a matrix
    matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

    # Compute the numerical rank of the matrix
    rank = numerical_rank(matrix)

    print("Numerical rank of the matrix:", rank)
