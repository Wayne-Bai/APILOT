
import networkx as nx
import numpy as np

def dict_to_numpy_array(input_dict, mapping=None):
    if mapping is not None:
        mapped_values = [mapping[key] for key in input_dict.keys()]
        return np.array(mapped_values)
    else:
        return np.array(list(input_dict.values()))

# Example dictionary
input_dict = {0: 10, 1: 20, 2: 30}

# Convert dictionary to numpy array
result_array = dict_to_numpy_array(input_dict)

print(result_array)
