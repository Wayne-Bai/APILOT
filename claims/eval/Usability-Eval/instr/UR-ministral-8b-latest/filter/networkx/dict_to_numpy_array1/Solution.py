import networkx as nx
import numpy as np

def dictionary_to_ndarray(dictionary, mapping_func=None):
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary.")

    if mapping_func is None:
        mapping_func = lambda x: x

    # Convert values to numpy array
    values = np.array([mapping_func(val) for val in dictionary.values()])
    return values

# Example usage
original_dict = {"a": 1, "b": 2, "c": 3}
converted_array = dictionary_to_ndarray(original_dict)
print(converted_array)

# Example usage with mapping function
mapped_dict = {"a": 1, "b": 2, "c": 3}
mapped_array = dictionary_to_ndarray(mapped_dict, mapping_func=lambda x: x * 2)
print(mapped_array)
