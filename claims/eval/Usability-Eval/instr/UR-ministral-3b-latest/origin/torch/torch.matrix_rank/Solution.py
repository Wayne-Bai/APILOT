import torch

# Function to compute the numerical rank of a matrix
def numerical_rank(matrix):
    return torch.norm(matrix, p=2).item()

# Test the function
matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print("Numerical rank:", numerical_rank(matrix))
