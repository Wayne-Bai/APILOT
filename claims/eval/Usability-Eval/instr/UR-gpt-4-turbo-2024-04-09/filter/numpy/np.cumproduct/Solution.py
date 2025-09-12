import numpy as np

def cumulative_product(arr, axis=None):
    return np.cumprod(arr, axis=axis)

# Example usage
data = np.array([1, 2, 3, 4])
axis = 0
result = cumulative_product(data, axis)
print("Cumulative product along axis", axis, ":", result)
