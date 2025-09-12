# Import the numpy library
import numpy as np

# Define a function to return a sorted copy of an array
def sorted_array(arr):
    """
    Returns a sorted copy of the input array.
    
    Parameters:
    arr (numpy.ndarray): The input array to be sorted.
    
    Returns:
    numpy.ndarray: A sorted copy of the input array.
    """
    # Create a copy of the input array to avoid modifying the original array
    array_copy = arr.copy()
    
    # Use the np.sort function from numpy to sort the array copy
    sorted_copy = np.sort(array_copy)
    
    return sorted_copy

# Example usage:
arr = np.array([64, 34, 25, 12, 22, 11, 90])
print("Original array:", arr)
print("Sorted array:", sorted_array(arr))
