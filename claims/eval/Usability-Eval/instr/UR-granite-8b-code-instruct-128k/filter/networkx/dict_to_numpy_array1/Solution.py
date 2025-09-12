
import networkx as nx
import numpy as np

def convert_dict_to_numpy_array(dictionary, mapping=None):
    if mapping:
        values = [mapping[key] for key in dictionary.keys()]
    else:
        values = list(dictionary.values())
    return np.array(values)
