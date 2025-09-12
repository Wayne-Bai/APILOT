import numpy as np
import networkx as nx

def dict_to_numpy_array(dict_of_dicts, mapping=None):
    # Check if the input is a dictionary of dictionaries
    if not isinstance(dict_of_dicts, dict) or not all(isinstance(v, dict) for v in dict_of_dicts.values()):
        raise ValueError("Input should be a dictionary of dictionaries")

    # Get the keys of the outermost dictionary
    keys = list(dict_of_dicts.keys())

    # Initialize an empty numpy array with the appropriate shape
    if mapping is None:
        array = np.zeros((len(keys), len(dict_of_dicts[keys[0]])))
    else:
        array = np.zeros((len(keys), len(mapping)))

    # Populate the numpy array with the values from the dictionary of dictionaries
    for i, key in enumerate(keys):
        for j, value in enumerate(dict_of_dicts[key].values()):
            if mapping is None:
                array[i, j] = value
            else:
                array[i, j] = mapping[value]

    return array
