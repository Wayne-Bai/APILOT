import torch

def least_squares_solution(A, b):
    # Compute the pseudoinverse of A
    A_pinv = torch.linalg.pinv(A)
    
    # Compute the least squares solution
    x = A_pinv @ b
    
    return x

# Example usage:
A = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
b = torch.tensor([1.0, 2.0, 3.0])

solution = least_squares_solution(A, b)
print(solution)
