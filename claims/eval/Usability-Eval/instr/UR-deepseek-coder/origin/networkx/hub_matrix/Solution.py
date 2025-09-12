import networkx as nx
import numpy as np

def hits_hub_matrix(G):
    # Compute the HITS algorithm
    hubs, authorities = nx.hits(G)
    
    # Create a hub matrix
    hub_matrix = np.zeros((len(G), len(G)))
    
    # Fill the hub matrix with hub scores
    for node, hub_score in hubs.items():
        hub_matrix[node, :] = hub_score
    
    return hub_matrix

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0)])
# hub_matrix = hits_hub_matrix(G)
# print(hub_matrix)
