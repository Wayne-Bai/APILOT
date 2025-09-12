import networkx as nx
import numpy as np

def communicability_all_pairs(G):
    # Compute the adjacency matrix
    A = nx.to_numpy_array(G)
    
    # Compute the exponential of the adjacency matrix
    expA = np.exp(A)
    
    # The communicability matrix is the element-wise product of the exponential of the adjacency matrix
    communicability = expA * expA.T
    
    return communicability

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])

communicability_matrix = communicability_all_pairs(G)
print(communicability_matrix)
