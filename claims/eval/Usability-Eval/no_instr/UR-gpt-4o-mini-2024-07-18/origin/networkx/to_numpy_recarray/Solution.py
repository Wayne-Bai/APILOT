import networkx as nx
import numpy as np

def graph_to_adjacency_matrix(graph):
    adjacency_matrix = nx.to_numpy_array(graph)
    return adjacency_matrix

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
adjacency_matrix = graph_to_adjacency_matrix(G)
adjacency_recarray = np.recarray(adjacency_matrix.shape, dtype=[('data', adjacency_matrix.dtype)])

for i in range(adjacency_matrix.shape[0]):
    adjacency_recarray[i] = adjacency_matrix[i]

print(adjacency_recarray)
