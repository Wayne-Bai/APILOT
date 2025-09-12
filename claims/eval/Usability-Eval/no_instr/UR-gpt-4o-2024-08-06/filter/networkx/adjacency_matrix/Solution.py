import networkx as nx
import numpy as np

def get_adjacency_matrix(graph):
    return nx.adjacency_matrix(graph).todense()

# Example usage:
# Create a graph object
G = nx.Graph()

# Add some edges (or nodes and edges)
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

# Get the adjacency matrix
adj_matrix = get_adjacency_matrix(G)
print(adj_matrix)
