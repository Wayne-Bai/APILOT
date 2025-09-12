import numpy as np

def cumulative_product(array, axis=None):
    return np.cumprod(array, axis=axis)

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
result = cumulative_product(data, axis=0)
print(result)
