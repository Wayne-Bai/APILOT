import torch

def solve_least_squares(A, b):
    """
    Solves the least squares problem for A*x = b using Torch.

    Parameters:
    A (torch.Tensor): The coefficient matrix.
    b (torch.Tensor): The right-hand side vector.

    Returns:
    torch.Tensor: Solution vector x.
    """

    # Using torch.linalg.lstsq to solve the least squares problem
    solution = torch.linalg.lstsq(A, b).solution

    return solution

# Example usage:
A = torch.tensor([[1., 2.], [3., 4.], [5., 6.]], dtype=torch.float32)
b = torch.tensor([1., 2., 3.], dtype=torch.float32)

x = solve_least_squares(A, b)
print("Solution x:", x)
