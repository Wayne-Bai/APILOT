import torch

# Let's create a 3x3 matrix
matrix = torch.tensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.]])

# Compute the rank of the matrix using torch.linalg.matrix_rank
rank = torch.linalg.matrix_rank(matrix)

print("The rank of the given matrix is:", rank)
