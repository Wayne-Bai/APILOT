import numpy as np

# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate cumulative product along axis=1 (rows)
cumulative_product = np.cumprod(arr, axis=1)

print(cumulative_product)
