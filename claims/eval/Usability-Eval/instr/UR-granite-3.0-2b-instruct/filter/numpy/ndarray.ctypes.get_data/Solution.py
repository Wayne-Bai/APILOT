import numpy as np

def get_array_pointer(arr):
    return arr.ctypes.data

# Example usage:
arr = np.array([1, 2, 3, 4, 5])
ptr = get_array_pointer(arr)
print(ptr)
