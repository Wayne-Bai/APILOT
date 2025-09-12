import numpy as np

def find_max_indices(arr):
    return np.argmax(arr, axis=0)

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(find_max_indices(arr))  # Output: [2 2 2]
