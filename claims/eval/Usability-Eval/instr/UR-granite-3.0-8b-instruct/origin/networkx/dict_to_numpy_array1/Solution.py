import networkx as nx
import numpy as np

def dict_to_array(dictionary, mapping=None):
    if mapping is None:
        mapping = {k: k for k in dictionary.keys()}
    array = np.zeros(len(dictionary))
    for i, key in enumerate(dictionary.keys()):
        array[i] = mapping[key]
    return array

# Example usage:
dictionary = {'a': 1, 'b': 2, 'c': 3}
mapping = {'a': 10, 'b': 20, 'c': 30}
array = dict_to_array(dictionary, mapping)
print(array)  # Output: [10 20 30]
