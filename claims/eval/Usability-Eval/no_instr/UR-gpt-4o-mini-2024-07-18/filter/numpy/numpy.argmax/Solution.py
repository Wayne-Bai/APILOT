import numpy as np

def max_indices_along_axis(arr, axis):
    return np.argmax(arr, axis=axis)

# Example usage
array = np.array([[1, 3, 2], [4, 6, 5], [7, 0, 8]])
axis = 0  # Change to 1 to find indices along rows
max_indices = max_indices_along_axis(array, axis)
print(max_indices)
