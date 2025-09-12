import numpy as np

def product_over_axis(array, axis=None):
    return np.prod(array, axis=axis)

# Example usage:
my_array = np.array([[1, 2, 3], [4, 5, 6]])
result = product_over_axis(my_array, axis=0)
print(result)  # Output: [ 4 10 18]
