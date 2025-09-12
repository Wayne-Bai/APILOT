import numpy as np
import networkx as nx

def dict_of_dicts_to_2d_array(dict_of_dicts):
    # Convert the dictionary of dictionaries to a list of lists
    list_of_lists = [list(row.values()) for row in dict_of_dicts.items()]

    # Convert the list of lists to a 2d array
    array = np.array(list_of_lists)

    return array

# Example usage:
dict_of_dicts = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
array = dict_of_dicts_to_2d_array(dict_of_dicts)
print(array)
