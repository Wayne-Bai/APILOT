import networkx as nx
import numpy as np

def hits_authority_matrix(graph):
    # Run HITS algorithm
    hubs, authorities = nx.hits(graph)
    
    # Prepare a list of nodes for consistent ordering
    nodes = list(graph.nodes)
    n = len(nodes)
    
    # Create an empty authority matrix
    authority_matrix = np.zeros((n, n))
    
    # Populate the matrix with authority scores
    for i, node in enumerate(nodes):
        authority_matrix[i][i] = authorities[node]
    
    return authority_matrix

# Example usage:
# Create a directed graph
G = nx.DiGraph([(0, 1), (1, 2), (2, 0), (3, 2)])

# Get the HITS authority matrix
authority_matrix = hits_authority_matrix(G)
print(authority_matrix)
