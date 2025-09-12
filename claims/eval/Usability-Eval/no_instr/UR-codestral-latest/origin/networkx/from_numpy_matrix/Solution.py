import networkx as nx
import numpy as np

# Assuming 'adj_matrix' is your numpy adjacency matrix
# If not, replace it with your matrix
# adj_matrix = np.array([...]) # replace with your matrix

def adjacency_matrix_to_graph(adj_matrix):
    G = nx.from_numpy_matrix(adj_matrix)
    return G

# Test the function
G = adjacency_matrix_to_graph(adj_matrix)
print(G.nodes)
print(G.edges)
