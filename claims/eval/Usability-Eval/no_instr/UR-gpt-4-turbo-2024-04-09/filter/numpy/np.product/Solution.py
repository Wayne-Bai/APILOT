import numpy as np

def product_of_elements(arr, axis=None):
    return np.prod(arr, axis=axis)

# Example usage:
array = np.array([[1, 2], [3, 4]])
result = product_of_elements(array, axis=0)
print("Product over axis 0:", result)
