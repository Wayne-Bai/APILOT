import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix

def graph_to_sparse_adjacency_matrix(G):
    # Get the adjacency matrix in dense format
    adjacency_matrix = nx.to_numpy_array(G)
    
    # Convert the dense adjacency matrix to a SciPy CSR sparse matrix
    sparse_matrix = csr_matrix(adjacency_matrix)
    
    return sparse_matrix

# Example: Create a simple graph and get its adjacency matrix as a sparse matrix
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])

sparse_adj_matrix = graph_to_sparse_adjacency_matrix(G)
print(sparse_adj_matrix)
