import networkx as nx
import numpy as np

def google_matrix(graph):
    # Convert the graph to an adjacency matrix
    adjacency_matrix = nx.adjacency_matrix(graph).todense()

    # Compute the inverse
    inverse_matrix = np.linalg.inv(adjacency_matrix)

    return inverse_matrix

# Example usage:
# Create a graph
G = nx.Graph()
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'E'), ('E', 'D')]
G.add_edges_from(edges)

# Compute the Google matrix
google_matrix_G = google_matrix(G)
print(google_matrix_G)
