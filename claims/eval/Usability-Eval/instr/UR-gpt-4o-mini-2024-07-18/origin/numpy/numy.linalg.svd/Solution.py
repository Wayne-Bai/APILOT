import numpy as np

# Example matrix
A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

# Create a diagonal matrix for singular values
Sigma = np.zeros((U.shape[0], VT.shape[0]))
np.fill_diagonal(Sigma, S)

# Output the results
print("U matrix:")
print(U)
print("\nSingular values:")
print(S)
print("\nVT matrix:")
print(VT)
print("\nDiagonal matrix of singular values (Sigma):")
print(Sigma)
