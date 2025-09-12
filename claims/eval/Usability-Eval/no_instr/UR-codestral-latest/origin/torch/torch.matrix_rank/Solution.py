import torch

def matrix_rank(mat):
    return torch.linalg.matrix_rank(mat).item()

# Example usage:
mat = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
print(matrix_rank(mat))
