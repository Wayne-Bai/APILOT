
import numpy as np

def unique_elements(arr):
    # Create a set to store the unique elements
    unique = set()
    
    # Iterate through the input array and add each element to the set
    for element in arr:
        unique.add(element)
        
    # Return the sorted unique elements
    return np.sort(list(unique))
