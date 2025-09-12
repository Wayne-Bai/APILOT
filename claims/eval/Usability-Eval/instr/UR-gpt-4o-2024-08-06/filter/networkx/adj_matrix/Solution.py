import networkx as nx
import numpy as np

def graph_to_adjacency_matrix(graph):
    # Get number of nodes
    num_nodes = graph.number_of_nodes()

    # Initialize a numpy matrix with zeros
    adj_matrix = np.zeros((num_nodes, num_nodes))

    # Use adjacency list to fill in the matrix
    for i, node in enumerate(graph.nodes()):
        for neighbor in graph.neighbors(node):
            j = list(graph.nodes()).index(neighbor)
            adj_matrix[i][j] = 1  # Assuming unweighted edges, use graph[node][neighbor]['weight'] for weighted

    return adj_matrix

# Example usage
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
adj_matrix = graph_to_adjacency_matrix(G)
print(adj_matrix)
