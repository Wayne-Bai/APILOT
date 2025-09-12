import numpy as np

def all_elements_true(arr, axis=None):
    return np.all(arr, axis=axis)

# Example usage:
# arr = np.array([[True, True], [True, False]])
# result = all_elements_true(arr, axis=1)
# print(result)  # Output: [ True False]
