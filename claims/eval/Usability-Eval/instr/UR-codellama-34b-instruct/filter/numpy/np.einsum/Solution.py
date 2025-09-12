import numpy as np

# Define the tensors
tensor1 = np.array([[1, 2], [3, 4]])
tensor2 = np.array([[5, 6], [7, 8]])

# Evaluate the Einstein summation convention on the two tensors
result = np.einsum('ijkl->ikl', tensor1, tensor2)

print(result)
