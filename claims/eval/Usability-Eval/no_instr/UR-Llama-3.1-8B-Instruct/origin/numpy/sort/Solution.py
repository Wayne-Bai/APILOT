import numpy as np

def sorted_copy(arr):
    """
    Return a sorted copy of the input array.
    
    Parameters:
    arr (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: A sorted copy of the input array.
    """
    # Create a copy of the input array to avoid modifying the original array
    arr_copy = np.copy(arr)
    
    # Sort the copied array in ascending order
    arr_copy = np.sort(arr_copy)
    
    # Return the sorted copy of the array
    return arr_copy

# Example usage:
arr = np.array([64, 34, 25, 12, 22, 11, 90])
print("Original array:")
print(arr)

sorted_arr = sorted_copy(arr)
print("Sorted copy of the array:")
print(sorted_arr)
