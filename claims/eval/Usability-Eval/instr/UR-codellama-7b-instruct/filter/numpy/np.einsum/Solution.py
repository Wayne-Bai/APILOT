import numpy as np

# Define the operands using NumPy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Apply Einstein summation convention to compute the dot product
dot_product = np.einsum('i, i', a, b)

print(f'Dot product: {dot_product}')