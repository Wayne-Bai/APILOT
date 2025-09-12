import numpy as np
import networkx as nx

def dict_to_numpy_array(dict_of_dicts):
    """
    Convert a dictionary of dictionaries to a 2d numpy array.

    Parameters:
    dict_of_dicts (dict): A dictionary where each value is also a dictionary.

    Returns:
    numpy.ndarray: A 2d numpy array representing the adjacency matrix.
    """
    # Get all unique keys
    nodes = set(dict_of_dicts.keys())
    for sub_dict in dict_of_dicts.values():
        nodes.update(sub_dict.keys())

    # Create a mapping from node to index
    node_to_index = {node: i for i, node in enumerate(nodes)}

    # Initialize the numpy array
    array = np.zeros((len(nodes), len(nodes)))

    # Populate the numpy array
    for node1, sub_dict in dict_of_dicts.items():
        for node2, weight in sub_dict.items():
            array[node_to_index[node1], node_to_index[node2]] = weight

    return array, node_to_index

# Usage example:
dict_of_dicts = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'C': 3},
    'C': {'A': 2, 'B': 3}
}

array, mapping = dict_to_numpy_array(dict_of_dicts)
print("Adjacency Matrix:")
print(array)
print("Mapping:")
for node, index in mapping.items():
    print(f"{node}: {index}")

# Create a graph from the dictionary of dictionaries
G = nx.DiGraph()
for node1, sub_dict in dict_of_dicts.items():
    for node2, weight in sub_dict.items():
        G.add_edge(node1, node2, weight=weight)

# Print the graph's adjacency matrix for comparison
print("\nAdjacency Matrix from Networkx:")
print(nx.to_numpy_array(G))
