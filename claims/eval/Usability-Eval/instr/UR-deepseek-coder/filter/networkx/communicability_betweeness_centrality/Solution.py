import networkx as nx
import numpy as np
from scipy.linalg import expm

def communicability_all_pairs(G):
    # Compute the adjacency matrix of the graph
    A = nx.to_numpy_array(G)
    
    # Compute the exponential of the adjacency matrix
    expA = expm(A)
    
    # Convert the result to a dictionary of communicability values
    communicability = {(i, j): expA[i, j] for i in range(len(A)) for j in range(len(A))}
    
    return communicability

# Example usage:
G = nx.erdos_renyi_graph(10, 0.3)
communicability = communicability_all_pairs(G)
print(communicability)
