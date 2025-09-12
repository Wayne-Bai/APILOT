import torch

# Fill in your matrix here
# For example, we'll use a standard 2x2 symmetric matrix
matrix = torch.tensor([[2., 1.], [1., 2.]])

# Perform eigenvalue decomposition
eig_values, eig_vectors = torch.symeig(matrix, eigenvectors=True)

# Eigenvalues are in non-increasing order
print("Eigenvalues: ", eig_values)

# Each column in 'eig_vectors' is the corresponding eigenvector
print("Eigenvectors: ", eig_vectors)
