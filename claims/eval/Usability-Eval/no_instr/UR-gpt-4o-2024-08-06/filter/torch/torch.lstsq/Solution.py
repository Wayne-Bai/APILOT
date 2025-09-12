import torch

def least_squares_solution(A, b):
    # Compute the Least Squares solution using the pseudoinverse
    # A^+ = (A^T A)^(-1) A^T, so the solution x = A^+ b
    A_T = A.t()
    A_pseudo = torch.matmul(torch.inverse(torch.matmul(A_T, A)), A_T)
    x = torch.matmul(A_pseudo, b)
    return x

# Example usage
A = torch.tensor([[2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
b = torch.tensor([1.0, 2.0, 3.0])

solution = least_squares_solution(A, b)
print("Least squares solution:", solution)
