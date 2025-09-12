import torch

def least_squares(A, b):
    """
    Computes a solution to the least squares problem of a system of linear equations.

    Args:
    A (torch.Tensor): A 2D tensor representing the matrix of coefficients.
    b (torch.Tensor): A 1D tensor representing the vector of constants.

    Returns:
    torch.Tensor: A 1D tensor representing the solution to the least squares problem.
    """
    # Compute the QR decomposition of A
    Q, R = torch.qr(A)

    # Solve the upper triangular system R * x = Q^T * b
    x = torch.solve(R, Q.t() @ b)[0]

    return x
