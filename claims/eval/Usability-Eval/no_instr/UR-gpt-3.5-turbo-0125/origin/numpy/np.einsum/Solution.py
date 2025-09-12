
import numpy as np

# Define the arrays a and b
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Evaluate the Einstein summation convention on the operands
result = np.einsum('ij,ij->ij', a, b)

print(result)
