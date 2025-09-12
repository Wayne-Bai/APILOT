import numpy as np

def stack_arrays_vertically(*arrays):
    stack = np.vstack([arr for arr in arrays if hasattr(arr, '__len__') and hasattr(arr, '__getitem__')])
    return stack

# Example usage
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = stack_arrays_vertically(arr1, arr2)
print(result)
