import networkx as nx
import numpy as np

def dict_to_2d_array(matrix_dict, mapping=None):
    # Convert the dictionary to a list of keys
    keys_list = list(matrix_dict.keys())
    rows, cols = len(keys_list), max(map(len, matrix_dict.values()))

    # Initialize the 2D array
    array_2d = np.zeros((len(keys_list), cols))

    # Iterate through the dictionary and fill the array
    for i, key in enumerate(keys_list):
        for j, value in enumerate(matrix_dict[key]):
            array_2d[i][j] = value

    # Apply any optional mapping if provided
    if mapping:
        for key, mapping_value in mapping.items():
            array_2d[mapping_value] = matrix_dict[key]

    return array_2d

# Example usage
example_matrix = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8]
}

example_mapping = {'A': 0, 'B': 1}

array_2d = dict_to_2d_array(example_matrix, example_mapping)
print(array_2d)
