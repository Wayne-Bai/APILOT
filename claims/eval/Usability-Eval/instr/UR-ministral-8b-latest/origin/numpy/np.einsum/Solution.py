import numpy as np

# Define operands
A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
B = np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])

# Evaluating Einstein summation convention
result = np.einsum('ijk,ijk->ij', A, B)

print("Result of Einstein summation convention:")
print(result)
