import numpy as np

def get_array_memory_area(arr):
    """
    Returns the memory area of a numpy array as a Python integer.
    
    User Beware: The memory area may contain data that is not aligned, 
    or not in correct byte-order. The memory area may not even be writeable. 
    The array flags and data-type of this array should be respected when 
    passing this attribute to arbitrary C-code to avoid trouble that can 
    include Python crashing.
    """
    return arr.__array_interface__['data'][0]

# Example usage:
arr = np.array([1, 2, 3, 4, 5])
memory_area = get_array_memory_area(arr)
print(memory_area)
