import torch

# Function to compute the least squares solution
def least_squares(A, B):
    # Compute the matrix A^T * A
    ATA = torch.matmul(A.T, A)
    
    # Compute the matrix A^T * B
    ATB = torch.matmul(A.T, B)
    
    # Solve the linear system (A^T * A) * X = A^T * B
    solution = torch.linalg.solve(ATA, ATB)
    return solution

# Example usage
# A is the matrix of coefficients
# B is the right-hand side vector/matrix
A = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
B = torch.tensor([7.0, 8.0, 9.0])

# Computing least squares solution
X = least_squares(A, B)
print("Least squares solution:", X)
