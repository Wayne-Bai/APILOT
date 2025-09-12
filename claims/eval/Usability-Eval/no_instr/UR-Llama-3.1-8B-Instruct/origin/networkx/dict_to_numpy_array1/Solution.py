import networkx as nx
import numpy as np

def dict_to_array(dictionary, mapping=True):
    """
    Convert a dictionary of numbers to a 1d numpy array with optional mapping.

    Parameters:
    dictionary (dict): A dictionary containing numbers as values.
    mapping (bool): Optional flag to enable or disable the mapping process.

    Returns:
    np.array: A 1d numpy array.
    """

    # Get the keys from the dictionary
    keys = dictionary.keys()

    # If mapping is enabled, sort the keys
    if mapping:
        keys = sorted(keys)

    # Create a list to store the values in the correct order
    values = []

    # Iterate over the keys and append their corresponding values
    for key in keys:
        values.append(dictionary[key])

    # Create and return a 1d numpy array
    return np.array(values)

# Example usage:
data = {"zero": 0, "one": 1, "two": 2, "three": 3}
print(dict_to_array(data))  # without mapping
print(dict_to_array(data, mapping=True))  # with mapping
