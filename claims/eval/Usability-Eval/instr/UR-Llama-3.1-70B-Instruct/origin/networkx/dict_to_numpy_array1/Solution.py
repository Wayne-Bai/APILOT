import networkx as nx
import numpy as np

def dictionary_to_numpy_array(dictionary, mapping=None):
    """
    Convert a dictionary of numbers to a 1D numpy array with optional mapping.

    Args:
    dictionary (dict): A dictionary where keys will be the indices of the output array and values will be the elements.
    mapping (dict, optional): A dictionary that maps old values to new values. Defaults to None.

    Returns:
    numpy.ndarray: A 1D numpy array.
    """
    
    # Find the maximum key to determine the size of the array
    max_key = max(dictionary.keys())
    
    # Initialize the array with zeros
    array = np.zeros(max_key + 1)
    
    # Populate the array with the dictionary values
    for key, value in dictionary.items():
        if mapping is not None:
            # Apply the mapping if provided
            array[key] = mapping.get(value, value)
        else:
            array[key] = value
    
    return array

# Example usage:

# Create a sample dictionary
dictionary = {0: 1, 2: 3, 4: 5}

# Convert the dictionary to a numpy array
array = dictionary_to_numpy_array(dictionary)
print(array)
# Output: [1. 0. 3. 0. 5.]

# Convert the dictionary to a numpy array with a custom mapping
mapping = {1: 10, 3: 30, 5: 50}
array_mapped = dictionary_to_numpy_array(dictionary, mapping)
print(array_mapped)
# Output: [10.  0. 30.  0. 50.]
