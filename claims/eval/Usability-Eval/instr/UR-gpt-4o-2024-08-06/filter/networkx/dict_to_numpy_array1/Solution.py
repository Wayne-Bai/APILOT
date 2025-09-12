import networkx as nx
import numpy as np

def dict_to_array(number_dict, mapping=None):
    # If a mapping is provided, apply it to the dictionary keys
    if mapping is not None:
        number_dict = {mapping[key]: value for key, value in number_dict.items() if key in mapping}

    # Convert values of the dictionary to a 1D numpy array
    array = np.array(list(number_dict.values()))

    return array

# Example usage:
# Define a dictionary of numbers
number_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Define an optional mapping (this will select and reorder elements)
mapping = {'a': 'x', 'c': 'z', 'b': 'y'}

# Convert the dictionary to a 1D array with the optional mapping
array = dict_to_array(number_dict, mapping)
print(array)  # Output would include elements 1, 2, 3 in the order defined by the mapping
