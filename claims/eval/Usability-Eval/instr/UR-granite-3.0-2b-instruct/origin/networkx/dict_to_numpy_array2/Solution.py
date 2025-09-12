import numpy as np
import networkx as nx

def dict_of_dicts_to_2d_numpy_array(d, mapping=None):
    # Create an empty list to store the 2D numpy arrays
    arrays = []

    # Iterate over each key-value pair in the dictionary
    for key, value in d.items():
        # If a mapping is provided, use it to index the value
        if mapping:
            value = value[mapping[key]]

        # Create a numpy array from the value
        array = np.array(value)

        # Append the array to the list
        arrays.append(array)

    # Concatenate all the arrays along the first axis to form a 2D numpy array
    result = np.concatenate(arrays, axis=0)

    return result
