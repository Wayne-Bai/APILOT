import networkx as nx
import numpy as np

def dict_to_numpy_array(dict_of_dicts, mapping=None):
    if mapping is None:
        mapping = {key: idx for idx, key in enumerate(dict_of_dicts.keys())}
    
    size = len(dict_of_dicts)
    array = np.zeros((size, size))
    
    for i, outer_key in enumerate(dict_of_dicts):
        for inner_key, value in dict_of_dicts[outer_key].items():
            if inner_key in mapping:
                array[mapping[outer_key], mapping[inner_key]] = value

    return array

# Example usage:
dict_of_dicts = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'C': 3},
    'C': {'A': 2, 'B': 3}
}

result_array = dict_to_numpy_array(dict_of_dicts)
print(result_array)
