import networkx as nx
import numpy as np

def dict_to_numpy(data, mapping=None):
    """
    Convert a dictionary of dictionaries to a 2D NumPy array with optional mapping.

    Parameters:
    data (dict): The dictionary of dictionaries.
    mapping (dict, optional): Optional mapping from keys to integers. Defaults to None.

    Returns:
    np.ndarray: The 2D NumPy array.
    """

    # Get all nodes in the graph
    nodes = set()
    for key in data:
        nodes.add(key)
        for sub_key in data[key]:
            nodes.add(sub_key)

    # Create the graph
    G = nx.Graph()

    # Add edges and nodes to the graph
    for key, value in data.items():
        for sub_key, sub_value in value.items():
            G.add_edge(key, sub_key, weight=sub_value)

    # Get edge lists and their weights
    edges = list(G.edges())
    weights = [None] * len(edges)
    for i, edge in enumerate(edges):
        weights[i] = G.get_edge_data(*edge)['weight']

    # Create a 2D array of zeros
    array = np.zeros((len(nodes), len(nodes)), dtype=float)

    # Fill in the values based on the edges and weights
    for i, edge in enumerate(edges):
        array[list(nx.get_node_attributes(G, 'node_id').values()).index(edge[0])][list(nx.get_node_attributes(G, 'node_id').values()).index(edge[1])] = weights[i]

    # If mapping is provided, replace nodes with their corresponding labels
    if mapping:
        array = np.vectorize(lambda x: mapping[x] if x in mapping else x)(array)

    return array


# Test the function
data = {
    'A': {'X': 1, 'Y': 2},
    'B': {'Z': 3, 'W': 4}
}

mapping = {'A': 0, 'B': 1, 'X': 0, 'Y': 1, 'Z': 2, 'W': 3}

print(dict_to_numpy(data, mapping))
