import numpy as np

def contains_true(arr, axis):
    # Flatten the array along the given axis
    flattened = np.ravel(arr, order='C') if axis < 0 else np.ravel(arr, order='F')

    # Check if any element evaluates to True
    return np.any(flattened)

# Example usage:
arr = np.array([[False, True], [False, False]])
axis = 0
print(contains_true(arr, axis))  # Outputs: True

axis = 1
print(contains_true(arr, axis))  # Outputs: True
