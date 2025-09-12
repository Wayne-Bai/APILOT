import networkx as nx
import numpy as np

def get_adjacency_matrix(G):
    # Get the list of nodes
    nodes = list(G.nodes())
    
    # Initialize an empty adjacency matrix with zeros
    adjacency_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
    
    # Populate the adjacency matrix
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if G.has_edge(node1, node2):
                adjacency_matrix[i, j] = 1
                
    return adjacency_matrix

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0)])
# matrix = get_adjacency_matrix(G)
# print(matrix)
