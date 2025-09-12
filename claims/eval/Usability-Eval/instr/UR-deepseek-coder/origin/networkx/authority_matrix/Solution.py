import networkx as nx
import numpy as np

def hits_authority_matrix(G):
    # Compute the HITS authority scores
    hits = nx.hits(G)
    authority_scores = hits[1]
    
    # Create a matrix with the authority scores
    authority_matrix = np.zeros((len(G), 1))
    for node, idx in nx.get_node_attributes(G, 'id').items():
        authority_matrix[idx] = authority_scores[node]
    
    return authority_matrix

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# authority_matrix = hits_authority_matrix(G)
# print(authority_matrix)
