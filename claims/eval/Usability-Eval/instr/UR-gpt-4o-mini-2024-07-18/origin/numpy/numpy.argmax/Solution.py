import numpy as np

def get_max_indices(array, axis=None):
    return np.argmax(array, axis=axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
max_indices = get_max_indices(data, axis=0)
print(max_indices)  # Output will be the indices of the maximum values along axis 0
