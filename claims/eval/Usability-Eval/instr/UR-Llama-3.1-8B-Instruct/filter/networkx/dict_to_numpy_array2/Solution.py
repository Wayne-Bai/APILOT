import networkx as nx
import numpy as np

def dict_to_array(data, mapping=None):
    """
    Convert a dictionary of dictionaries to a 2D numpy array with optional mapping.

    Args:
        data (dict): Dictionary of dictionaries.
        mapping (dict): Optional mapping of keys to integers.

    Returns:
        np.ndarray: 2D numpy array.
    """
    if mapping is None:
        # If no mapping is provided, use the dictionary keys as is
        mapping = {key: i for i, key in enumerate(data.keys())}

    # Initialize a 2D numpy array with zeros
    array = np.zeros((len(data), len(data[list(data.keys())[0]])))

    # Iterate over the dictionaries and fill in the array
    for i, (key, value) in enumerate(data.items()):
        for j, k in enumerate(value.keys()):
            if k in mapping:
                array[i, mapping[k]] = value[k]

    return array

# Example usage
data = {
    'A': {'x': 10, 'y': 20, 'z': 30},
    'B': {'x': 40, 'y': 50, 'z': 60},
    'C': {'x': 70, 'y': 80, 'z': 90}
}

mapping = {'x': 0, 'y': 1, 'z': 2}

array = dict_to_array(data, mapping)
print(array)
