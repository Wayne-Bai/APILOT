import torch

def solve_least_squares(A, b):
    """
    Solve the least squares problem Ax = b using QR decomposition.
    
    Args:
    A (torch.Tensor): The coefficient matrix.
    b (torch.Tensor): The right-hand side vector or matrix.
    
    Returns:
    torch.Tensor: The solution vector or matrix x that minimizes |Ax - b|.
    """
    # QR decomposition
    Q, R = torch.linalg.qr(A)
    
    # Compute Q^T * b
    Qt_b = torch.matmul(Q.T, b)
    
    # Solve Rx = Q^T*b for x using triangular_solve
    x = torch.linalg.solve_triangular(R, Qt_b)
    
    return x

# Example usage:
A = torch.tensor([[2.0, 1.0], [1.0, 2.0]], dtype=torch.float32)
b = torch.tensor([1.0, 2.0], dtype=torch.float32)

x = solve_least_squares(A, b)
print("Solution x:", x)
