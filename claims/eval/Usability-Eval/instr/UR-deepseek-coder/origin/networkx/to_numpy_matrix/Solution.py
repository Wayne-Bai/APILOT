import networkx as nx
import numpy as np

def adjacency_matrix_as_numpy(graph):
    # Get the adjacency matrix as a list of lists
    adj_matrix = nx.to_numpy_array(graph)
    return adj_matrix

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3)])
adj_matrix = adjacency_matrix_as_numpy(G)
print(adj_matrix)
