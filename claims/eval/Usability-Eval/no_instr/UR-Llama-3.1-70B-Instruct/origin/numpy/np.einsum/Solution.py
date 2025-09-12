import numpy as np

# Define two 2D arrays
a = np.arange(4).reshape(2, 2)
b = np.arange(4).reshape(2, 2)

# Apply Einstein summation convention
# The following operation is equivalent to np.sum(a * b, axis=(0, 1))
result1 = np.einsum('ij,ij->', a, b)
print("Result 1: \n", result1)

# The following operation is equivalent to np.dot(a, b) or np.sum(a[:, None, :] * b[None, :, :], axis=-1)
result2 = np.einsum('ij,jk->ik', a, b)
print("Result 2: \n", result2)

# The following operation is equivalent to np.trace(np.dot(a, b)) or np.sum(np.diag(np.dot(a, b)))
result3 = np.einsum('ij,ji->', a, b)
print("Result 3: \n", result3)
