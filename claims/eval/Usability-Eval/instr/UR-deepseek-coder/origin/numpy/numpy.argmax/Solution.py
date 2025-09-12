import numpy as np

def argmax_axis(arr, axis=None):
    if axis is None:
        # Flatten the array and find the index of the maximum value
        flat_index = np.argmax(arr)
        return np.unravel_index(flat_index, arr.shape)
    else:
        # Find the indices of the maximum values along the specified axis
        return np.argmax(arr, axis=axis)

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(argmax_axis(arr, axis=1))  # Output: [2 2 2]
print(argmax_axis(arr, axis=0))  # Output: [2 2 2]
print(argmax_axis(arr))          # Output: (2, 2)
