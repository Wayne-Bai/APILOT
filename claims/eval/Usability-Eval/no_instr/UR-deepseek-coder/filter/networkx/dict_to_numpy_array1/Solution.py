import networkx as nx
import numpy as np

def dict_to_numpy_array(input_dict, mapping=None):
    # Create a graph
    G = nx.Graph()
    
    # Add nodes with values from the dictionary
    for key, value in input_dict.items():
        G.add_node(key, value=value)
    
    # If mapping is provided, remap the nodes
    if mapping:
        G = nx.relabel_nodes(G, mapping)
    
    # Extract the values into a list
    values = [G.nodes[node]['value'] for node in sorted(G.nodes())]
    
    # Convert the list to a numpy array
    return np.array(values)

# Example usage:
input_dict = {1: 10, 2: 20, 3: 30}
mapping = {1: 0, 2: 1, 3: 2}
result = dict_to_numpy_array(input_dict, mapping)
print(result)  # Output: [10 20 30]
