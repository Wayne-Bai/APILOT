import networkx as nx
import numpy as np

def get_adjacency_matrix(G):
    # Get the number of nodes in the graph
    num_nodes = G.number_of_nodes()
    
    # Initialize an empty adjacency matrix
    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    
    # Fill the adjacency matrix based on the edges in the graph
    for edge in G.edges():
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1  # For undirected graphs
    
    return adjacency_matrix

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0)])
# adj_matrix = get_adjacency_matrix(G)
# print(adj_matrix)
