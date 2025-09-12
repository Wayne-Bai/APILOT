import numpy as np

# Function to evaluate Einstein summation convention
def einstein_summation(a, b):
    # Reshape the operands to match the Einstein summation convention
    a = np.reshape(a, (a.shape[0], -1))
    b = np.reshape(b, (-1, b.shape[1]))

    # Perform the Einstein summation
    result = np.einsum('ij,jk->ik', a, b)

    return result

# Example usage:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(einstein_summation(a, b))
