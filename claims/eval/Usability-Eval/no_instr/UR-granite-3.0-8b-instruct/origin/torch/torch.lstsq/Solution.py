import torch

def least_squares_solver(A, b):
    """
    Computes a solution to the least squares problem of a system of linear equations.

    Args:
    A (torch.Tensor): The matrix of coefficients.
    b (torch.Tensor): The vector of constants.

    Returns:
    torch.Tensor: The solution vector.
    """
    # Compute the least squares solution using torch.matmul and torch.linalg.lstsq
    solution = torch.linalg.lstsq(A, b)[0]
    return solution
