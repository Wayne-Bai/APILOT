import torch

def least_squares_solution(A, b):
    """
    Computes a solution to the least squares problem of a system of linear equations.

    Args:
        A (torch.tensor): Coefficient matrix of the linear system.
        b (torch.tensor): Right-hand side vector of the linear system.

    Returns:
        torch.tensor: Solution to the least squares problem.
    """
    # Compute the Moore-Penrose pseudoinverse of A
    A_pinv = torch.pinverse(A)
    
    # Compute the least squares solution
    x = torch.matmul(A_pinv, b)
    
    return x

# Example usage:
if __name__ == "__main__":
    # Define the coefficient matrix A and the right-hand side vector b
    A = torch.tensor([[3., 1], [1, 2]])
    b = torch.tensor([9., 8])

    # Compute and print the least squares solution
    x = least_squares_solution(A, b)
    print("Least squares solution:", x)
