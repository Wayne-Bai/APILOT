import networkx as nx
import numpy as np

def dict_to_matrix(d: dict, node_mapping: dict = None):
    # Create a directed graph from the dictionary of dictionaries
    G = nx.DiGraph(d)

    # If a node mapping is provided, apply it
    if node_mapping:
        G = nx.relabel_nodes(G, node_mapping)

    # Find the number of nodes for matrix dimensions
    nodes = list(G.nodes)
    n = len(nodes)

    # Create an n by n numpy array initialized to zero
    matrix = np.zeros((n, n))

    # Fill the matrix with edges data
    for i, src in enumerate(nodes):
        for j, dst in enumerate(nodes):
            if G.has_edge(src, dst):
                matrix[i][j] = G[src][dst]['weight'] if 'weight' in G[src][dst] else 1

    return matrix

# Example Usage
example_dict = {
    'A': {'B': 2, 'C': 3},
    'B': {'C': 1},
    'C': {'A': 4}
}

node_mapping = {'A': 0, 'B': 1, 'C': 2}

matrix = dict_to_matrix(example_dict, node_mapping)
print(matrix)
