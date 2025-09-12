import numpy as np

# Define the arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Use einsum to calculate the dot product
result = np.einsum('i,i->', a, b)  # Einstein summation convention

print(result)
