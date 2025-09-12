import torch

# Define a tensor
matrix = torch.tensor([[1, 2], [3, 4]])

# Compute the rank of the tensor
rank = torch.linalg.matrix_rank(matrix)

print(rank)
