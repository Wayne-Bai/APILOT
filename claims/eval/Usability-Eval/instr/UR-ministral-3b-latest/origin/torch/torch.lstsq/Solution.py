import torch

def least_squares_solve(A, B):
    """Solve the least squares problem of the system of linear equations Ax = B.

    Args:
        A (torch.Tensor): Input matrix A of shape (n, m).
        B (torch.Tensor): Input vector B of shape (n, ).

    Returns:
        torch.Tensor: Solution vector x of shape (m, ).
    """
    m, n = A.shape
    A_transpose = A.t()
    q, _, _ = torch.svd(A_transpose)
    q_inv = q.inverse()
    b_transpose = B.t().matmul(q_inv)
    return A.t().matmul(b_transpose)
