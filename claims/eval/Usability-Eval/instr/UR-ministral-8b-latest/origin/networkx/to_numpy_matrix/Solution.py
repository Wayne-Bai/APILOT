import networkx as nx
import numpy as np

def graph_to_adjacency_matrix(G):
    # Get the edge list
    edges = G.edges()

    # Convert edge list to adjacency matrix format
    num_nodes = len(G.nodes())
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    return adj_matrix

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

# Convert to adjacency matrix
adj_matrix = graph_to_adjacency_matrix(G)
print(adj_matrix)
