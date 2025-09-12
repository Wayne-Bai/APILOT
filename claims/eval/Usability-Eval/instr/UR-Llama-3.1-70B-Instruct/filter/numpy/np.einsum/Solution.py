import numpy as np

# Define two 2-dimensional arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Evaluate the Einstein summation convention on the operands,
# where A and B are the input arrays, (1, 0) is the operand number for A
# and (0, 1) is the operand number for B.
result = np.tensordot(A, B, axes=(1, 0))

print("Array A:")
print(A)
print("\nArray B:")
print(B)
print("\nResult of Einstein summation convention:")
print(result)
