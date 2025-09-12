import numpy as np

def product_over_axis(array, axis=None):
    return np.prod(array, axis=axis)

# Example usage:
array = np.array([[1, 2], [3, 4]])
axis = 1  # Change axis as needed
result = product_over_axis(array, axis)
print("Product over axis:", result)
