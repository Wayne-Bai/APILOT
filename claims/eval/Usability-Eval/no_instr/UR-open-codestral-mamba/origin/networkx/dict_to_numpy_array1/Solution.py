import numpy as np

# Create a 1D numpy array from a dictionary

def dict_to_array(dict_data, map_func=None):
    if map_func is not None:
        # Apply the mapping function to each value in the dictionary
        dict_data = {k: map_func(v) for k, v in dict_data.items()}

    array_data = np.array(list(dict_data.values()))
    return array_data

# Example usage:
data_dict = {1: 2, 2: 4, 3: 6, 4: 8}

# Simple mapping function to double each value
def double_value(value):
    return value * 2

# Use the function to convert the dictionary to a numpy array
array = dict_to_array(data_dict, double_value)
print(array)
