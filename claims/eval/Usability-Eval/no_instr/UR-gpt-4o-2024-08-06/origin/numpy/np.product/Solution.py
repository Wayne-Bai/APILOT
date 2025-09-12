import numpy as np

def product_of_elements(arr, axis=None):
    # Calculate and return the product of array elements over the specified axis
    return np.prod(arr, axis=axis)

# Example usage:
array = np.array([[1, 2, 3], [4, 5, 6]])
result = product_of_elements(array, axis=0)
print("Product over axis 0:", result)

result = product_of_elements(array, axis=1)
print("Product over axis 1:", result)

result = product_of_elements(array)  # Product of all elements
print("Product of all elements:", result)
