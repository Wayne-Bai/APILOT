import networkx as nx
import numpy as np

def hits_hub_matrix(G):
    # Compute the HITS algorithm
    hubs, authorities = nx.hits(G)
    
    # Convert the hubs dictionary to a numpy array
    hub_values = np.array(list(hubs.values()))
    
    # Create a matrix where each row corresponds to a node and each column is the hub score
    hub_matrix = np.diag(hub_values)
    
    return hub_matrix

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# hub_matrix = hits_hub_matrix(G)
# print(hub_matrix)
