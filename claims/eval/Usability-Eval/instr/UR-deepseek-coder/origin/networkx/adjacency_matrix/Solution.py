import networkx as nx
import numpy as np

def get_adjacency_matrix(G):
    # Get the number of nodes in the graph
    num_nodes = G.number_of_nodes()
    
    # Initialize an empty adjacency matrix
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    
    # Iterate over each edge in the graph
    for u, v in G.edges():
        # Get the indices of the nodes
        u_idx = list(G.nodes()).index(u)
        v_idx = list(G.nodes()).index(v)
        
        # Set the corresponding entry in the adjacency matrix to 1
        adj_matrix[u_idx, v_idx] = 1
        adj_matrix[v_idx, u_idx] = 1  # For undirected graphs
    
    return adj_matrix

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])
adj_matrix = get_adjacency_matrix(G)
print(adj_matrix)
