import numpy as np
import networkx as nx

def convert_dict_to_2d_array(dictionary, mapping=None):
    # Create an empty undirected graph
    G = nx.Graph()

    # If a mapping is provided, apply it to the dictionary keys and values
    if mapping is not None:
        dictionary = {mapping[k]: {mapping[v]: Dictionary[k][v] for v in Dictionary[k]} for k in Dictionary}

    # Add nodes to the graph
    for node in dictionary.keys():
        G.add_node(node)

    # Add edges to the graph with their respective weights
    for node_u in dictionary.keys():
        for node_v in dictionary[node_u].keys():
            G.add_edge(node_u, node_v, weight=dictionary[node_u][node_v])

    # Compute the adjacency matrix of the graph
    adj_matrix = nx.adjacency_matrix(G)

    # Convert the adjacency matrix to a numpy array
    array_2d = np.array(adj_matrix.todense())

    return array_2d

# Example usage:
Dictionary = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 3},
    'C': {'A': 2, 'D': 4},
    'D': {'B': 3, 'C': 4}
}

mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
array_2d = convert_dict_to_2d_array(Dictionary, mapping)
print(array_2d)
