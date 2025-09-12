import networkx as nx
import numpy as np

def dict_to_numpy_array(data_dict, mapping=None):
    # If a mapping is provided, apply it to the keys
    if mapping:
        data_dict = {mapping.get(k, k): v for k, v in data_dict.items()}
    
    # Create a weight matrix which will be a 2D array
    keys = list(data_dict.keys())
    size = len(keys)
    matrix = np.zeros((size, size))

    # Fill in the matrix with the values from the dictionary of dictionaries
    for i, key_i in enumerate(keys):
        for j, key_j in enumerate(keys):
            matrix[i, j] = data_dict.get(key_i, {}).get(key_j, 0)

    return matrix

# Example usage
data = {
    'a': {'a': 1, 'b': 2},
    'b': {'a': 3, 'b': 4},
}

mapping = {'a': 'A', 'b': 'B'}

numpy_array = dict_to_numpy_array(data, mapping)
print(numpy_array)
