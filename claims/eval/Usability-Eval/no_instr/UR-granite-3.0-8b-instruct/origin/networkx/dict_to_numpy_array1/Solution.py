import networkx as nx
import numpy as np

def dict_to_array(d, map_func=None):
    if map_func:
        return np.array([map_func(v) for v in d.values()])
    else:
        return np.array(list(d.values()))

# Example usage:
d = {'a': 1, 'b': 2, 'c': 3}
print(dict_to_array(d))  # Output: [1 2 3]
print(dict_to_array(d, map_func=lambda x: x**2))  # Output: [1 4 9]
