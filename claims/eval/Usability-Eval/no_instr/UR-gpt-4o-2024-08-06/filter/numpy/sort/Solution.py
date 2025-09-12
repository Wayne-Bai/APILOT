import numpy as np

def sort_array(arr):
    # Ensure the input is a numpy array
    numpy_arr = np.array(arr)
    
    # Sort the array and return the sorted copy
    sorted_array = np.sort(numpy_arr)
    return sorted_array

# Example usage
example_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_example = sort_array(example_array)
print(sorted_example)
