import networkx as nx
import numpy as np

def numpy_matrix_to_graph(adjacency_matrix):
    # Create a directed graph from a given numpy adjacency matrix
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.Graph)
    return G

# Example usage:
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])

graph = numpy_matrix_to_graph(adjacency_matrix)

# To verify, print the edges of the generated graph
print(list(graph.edges))
