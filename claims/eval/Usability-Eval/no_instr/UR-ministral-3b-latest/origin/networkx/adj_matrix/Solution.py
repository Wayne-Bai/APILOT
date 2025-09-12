import networkx as nx
import numpy as np

def get_adjacency_matrix(graph):
    adjacency_matrix = nx.to_numpy_array(graph)
    return adjacency_matrix

# Example usage:
G = nx.random_graphs.random_graph([5, 70, 0.5])
adj_matrix = get_adjacency_matrix(G)
print(adj_matrix)
