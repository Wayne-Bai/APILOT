import numpy as np

def array_product_over_axis(arr, axis=None):
    return np.prod(arr, axis=axis)

# Example usage:
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# result = array_product_over_axis(arr, axis=1)
# print(result)  # Output: [6, 120]
