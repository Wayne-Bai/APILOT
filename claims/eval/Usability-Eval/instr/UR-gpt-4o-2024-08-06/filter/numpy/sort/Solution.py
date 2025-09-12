import numpy as np

def sorted_copy(arr):
    return np.sort(arr)

# Example usage:
array = np.array([5, 2, 9, 1, 5, 6])
sorted_array = sorted_copy(array)
print("Original array:", array)
print("Sorted copy:", sorted_array)
