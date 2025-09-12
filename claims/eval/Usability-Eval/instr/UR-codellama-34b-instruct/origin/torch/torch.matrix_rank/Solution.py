
import torch

# Create a random matrix
matrix = torch.rand(10, 10)

# Compute the SVD decomposition of the matrix
U, S, Vh = torch.svd(matrix)

# Compute the numerical rank of the matrix
rank = len(S[S > 1e-6])

print("The numerical rank of the matrix is:", rank)
