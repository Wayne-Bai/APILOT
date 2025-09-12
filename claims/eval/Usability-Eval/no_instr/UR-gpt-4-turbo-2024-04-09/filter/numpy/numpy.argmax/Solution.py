import numpy as np

def indices_of_max_values(arr, axis=None):
    return np.argmax(arr, axis=axis)

# Example usage:
array_example = np.array([[1, 3, 5], [6, 2, 8]])
axis = 1  # Change as needed
print(indices_of_max_values(array_example, axis))
