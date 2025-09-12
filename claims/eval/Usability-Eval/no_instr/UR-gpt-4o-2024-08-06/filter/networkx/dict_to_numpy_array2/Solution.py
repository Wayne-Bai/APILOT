import networkx as nx
import numpy as np

def dict_to_2d_array(dict_of_dicts, node_order=None):
    # Create a graph from the dictionary of dictionaries
    G = nx.from_dict_of_dicts(dict_of_dicts)

    # If no specific node order is provided, use the sorted nodes
    if node_order is None:
        node_order = sorted(G.nodes())

    # Create a mapping of node to index
    node_index = {node: i for i, node in enumerate(node_order)}

    # Initialize a 2D numpy array with zeros
    size = len(node_order)
    array_2d = np.zeros((size, size))

    # Fill the 2D array based on edges present in the graph
    for u, v, data in G.edges(data=True):
        if u in node_index and v in node_index:
            weight = data.get('weight', 1)  # Default weight to 1 if not specified
            array_2d[node_index[u], node_index[v]] = weight

    return array_2d

# Example usage:
dict_of_dicts = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'C': 3},
    'C': {'A': 2, 'B': 3}
}

result = dict_to_2d_array(dict_of_dicts)
print(result)
