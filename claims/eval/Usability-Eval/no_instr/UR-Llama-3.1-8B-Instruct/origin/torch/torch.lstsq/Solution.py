# Import the necessary torch modules
import torch
import torch.nn.functional as F

def least_squares_problem(A, b):
    """
    Computes a solution to the least squares problem of a system of linear equations.
    
    Args:
    A (torch.Tensor): The coefficient matrix.
    b (torch.Tensor): The right-hand side vector.
    
    Returns:
    x (torch.Tensor): The solution vector.
    """
    
    # Compute the pseudo inverse of A using the Moore-Penrose inverse formula
    A_pseudo_inverse = torch.pinverse(A)
    
    # Compute the solution vector by multiplying the pseudo inverse of A with b
    x = torch.mm(A_pseudo_inverse, b)
    
    return x

# Create a coefficient matrix A
A = torch.tensor([[2, 1], [4, 3]], dtype=torch.float32)

# Create a right-hand side vector b
b = torch.tensor([6, 14], dtype=torch.float32)

# Compute the solution vector
x = least_squares_problem(A, b)

print("Solution vector: ", x)
