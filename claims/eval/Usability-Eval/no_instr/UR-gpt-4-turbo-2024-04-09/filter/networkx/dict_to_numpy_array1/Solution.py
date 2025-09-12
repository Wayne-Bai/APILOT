import numpy as np

def dict_to_numpy_array(data_dict, use_keys=False):
    """
    Converts a dictionary to a numpy array using either keys or values.

    Parameters:
    - data_dict (dict): The dictionary to convert.
    - use_keys (bool): If True, use the dictionary's keys, else use the values.

    Returns:
    - numpy.ndarray: Array formed from the dictionary.
    """
    if use_keys:
        array_data = np.array(list(data_dict.keys()))
    else:
        array_data = np.array(list(data_dict.values()))
    
    return array_data

# Example usage
data_dict = {1: 'a', 2: 'b', 3: 'c'}
array_from_values = dict_to_numpy_array(data_dict, use_keys=False)
array_from_keys = dict_to_numpy_array(data_dict, use_keys=True)

print("Array from values:", array_from_values)
print("Array from keys:", array_from_keys)
