import numpy as np

# Example array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Axis along which to calculate cumulative product
axis = 1

# Cumulative product along the given axis
cumulative_product = np.cumprod(arr, axis=axis)

# Display the result
print(cumulative_product)
