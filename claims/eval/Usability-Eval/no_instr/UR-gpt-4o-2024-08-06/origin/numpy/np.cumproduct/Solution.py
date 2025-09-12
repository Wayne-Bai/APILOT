import numpy as np

# Example array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate the cumulative product along a specific axis
# Set axis=0 for the cumulative product along columns
# Set axis=1 for the cumulative product along rows
cumulative_product = np.cumprod(array, axis=0)

print(cumulative_product)
