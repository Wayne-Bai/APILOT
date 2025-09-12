import numpy as np

def cumulative_product(arr, axis=0):
    return np.cumprod(arr, axis=axis)

# Example usage
array = np.array([[1, 2, 3], [4, 5, 6]])
result = cumulative_product(array, axis=0)
print(result)
