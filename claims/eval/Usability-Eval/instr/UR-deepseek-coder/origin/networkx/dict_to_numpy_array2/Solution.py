import networkx as nx
import numpy as np

def dict_to_numpy_array(dict_of_dicts, mapping=None):
    # Create a directed graph from the dictionary of dictionaries
    G = nx.DiGraph(dict_of_dicts)
    
    # If a mapping is provided, relabel the nodes
    if mapping:
        G = nx.relabel_nodes(G, mapping)
    
    # Get the adjacency matrix as a numpy array
    adj_matrix = nx.to_numpy_array(G)
    
    return adj_matrix

# Example usage:
dict_of_dicts = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 3, 'C': 4},
    'C': {'A': 5, 'B': 6}
}

mapping = {'A': 0, 'B': 1, 'C': 2}

result = dict_to_numpy_array(dict_of_dicts, mapping)
print(result)
