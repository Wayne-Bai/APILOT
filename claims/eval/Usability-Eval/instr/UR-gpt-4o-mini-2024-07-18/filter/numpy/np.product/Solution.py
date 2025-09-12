import numpy as np

def product_over_axis(arr, axis):
    return np.prod(arr, axis=axis)

# Example usage:
example_array = np.array([[1, 2, 3], [4, 5, 6]])
result = product_over_axis(example_array, axis=0)
print(result)  # Output: [ 4 10 18]
