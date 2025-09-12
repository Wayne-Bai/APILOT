import numpy as np

def cumulative_product(arr, axis=None):
    return np.cumprod(arr, axis=axis)

# Usage
array = np.array([[1, 2, 3], [4, 5, 6]])
print(cumulative_product(array, axis=0))  # Computes the cumulative product along the rows
print(cumulative_product(array, axis=1))  # Computes the cumulative product along the columns
