import numpy as np

# Let's assume we have a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate cumulative product along axis 0
cumulative_product = np.cumprod(arr, axis=0)
print("Cumulative product along axis 0:\n", cumulative_product)

# Calculate cumulative product along axis 1
cumulative_product = np.cumprod(arr, axis=1)
print("Cumulative product along axis 1:\n", cumulative_product)
