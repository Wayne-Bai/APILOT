import numpy as np

# Define example arrays
A = np.random.rand(2, 3)
B = np.random.rand(3, 4)

# Use numpy's einsum to perform a summation
result = np.einsum('ik,kj->ij', A, B)

print("Array A:")
print(A)
print("\nArray B:")
print(B)
print("\nResult of Einstein Summation Convention:")
print(result)
