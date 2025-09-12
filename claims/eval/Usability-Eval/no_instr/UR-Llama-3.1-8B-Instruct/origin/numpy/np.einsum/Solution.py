import numpy as np

# Define the operands
a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# Perform Einstein summation
c = np.einsum('ik,kj->ij', a, b)

# Print the result
print("The result of the Einstein summation is: ")
print(c)
