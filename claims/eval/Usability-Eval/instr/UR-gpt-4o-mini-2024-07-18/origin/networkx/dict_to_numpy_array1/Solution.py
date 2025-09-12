import networkx as nx
import numpy as np

def dict_to_numpy_array(data_dict, mapping=None):
    if mapping is not None:
        mapped_dict = {mapping[key]: value for key, value in data_dict.items() if key in mapping}
    else:
        mapped_dict = data_dict

    return np.array(list(mapped_dict.values()))

# Example usage:
data = {'a': 1, 'b': 2, 'c': 3}
mapping = {'a': 'x', 'b': 'y'}
result = dict_to_numpy_array(data, mapping)
print(result)
