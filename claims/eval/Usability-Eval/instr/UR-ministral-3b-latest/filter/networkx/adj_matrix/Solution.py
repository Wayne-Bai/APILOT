import networkx as nx
import numpy as np

# Function to return adjacency matrix of a graph as a numpy matrix
def get_adj_matrix(graph):
    adj_matrix = nx.adjacency_matrix(graph).toarray()
    return adj_matrix

# Example usage:
G = nx.erdos_renyi_graph(5, 0.5)
adj_matrix = get_adj_matrix(G)
print(adj_matrix)
