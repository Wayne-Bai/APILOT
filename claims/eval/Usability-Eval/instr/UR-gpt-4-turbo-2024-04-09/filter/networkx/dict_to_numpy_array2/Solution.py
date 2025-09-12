import networkx as nx
import numpy as np

def dict_to_2darray(dict_of_dicts, mapping=None):
    G = nx.DiGraph(dict_of_dicts)
    
    if mapping:
        # Re-label nodes according to the mapping provided
        G = nx.relabel_nodes(G, mapping)

    # Get adjacency matrix as a numpy array
    adj_matrix = nx.to_numpy_array(G)
    return adj_matrix

# Example usage
dict_of_dicts = {
    0: {1: 1, 2: 3},
    1: {2: 2},
    2: {}
}

mapping = {0: 'a', 1: 'b', 2: 'c'}
matrix = dict_to_2darray(dict_of_dicts, mapping)
print(matrix)
