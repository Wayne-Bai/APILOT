import torch
import torch.nn as nn

def least_squares_problem(A, b):
    """
    Computes a solution to the least squares problem of a system of linear equations.

    Parameters:
    A (torch.Tensor): The matrix of coefficients in the system of equations.
    b (torch.Tensor): The vector of constants in the system of equations.

    Returns:
    x (torch.Tensor): The least squares solution to the system of equations.
    """
    # Compute the transpose of the matrix A
    A_T = A.transpose(0, 1)
    
    # Compute the matrix product of A^T and A
    A_T_A = torch.matmul(A_T, A)
    
    # Compute the matrix product of A^T and b
    A_T_b = torch.matmul(A_T, b)
    
    # Compute the inverse of the matrix product of A^T and A
    try:
        A_T_A_inv = torch.inverse(A_T_A)
    except torch.linalg.LinferenceError:
        print("Matrix A^T A is singular. Solution is not unique.")
        return None
    
    # Compute the matrix product of the inverse of A^T A and A^T b
    x = torch.matmul(A_T_A_inv, A_T_b)
    
    return x

# Example usage:
A = torch.tensor([[2, 1], [4, 3]])
b = torch.tensor([10, 20])
solution = least_squares_problem(A, b)

print("Least Squares Solution:")
print(solution)
