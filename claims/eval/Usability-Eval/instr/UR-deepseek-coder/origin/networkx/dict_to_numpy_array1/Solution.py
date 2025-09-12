import networkx as nx
import numpy as np

def dict_to_numpy_array(input_dict, mapping=None):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes and edges based on the input dictionary
    for key, value in input_dict.items():
        G.add_edge(key, value)
    
    # If a mapping is provided, use it to map the nodes
    if mapping:
        G = nx.relabel_nodes(G, mapping)
    
    # Extract the nodes and convert to a numpy array
    node_list = list(G.nodes())
    node_array = np.array(node_list)
    
    return node_array

# Example usage:
input_dict = {1: 2, 3: 4, 5: 6}
mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
result = dict_to_numpy_array(input_dict, mapping)
print(result)
