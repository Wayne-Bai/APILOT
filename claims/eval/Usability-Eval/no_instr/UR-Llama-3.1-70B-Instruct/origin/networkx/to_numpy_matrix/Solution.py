
import networkx as nx
import numpy as np

def get_adjacency_matrix(graph):
    """
    Returns the graph adjacency matrix as a NumPy matrix.

    Args:
        graph (nx.Graph): The graph to get the adjacency matrix of.

    Returns:
        np.ndarray: The adjacency matrix of the graph.
    """
    # Get the adjacency matrix using the adjacency_matrix function from networkx
    adj_matrix = nx.to_numpy_array(graph)

    return adj_matrix

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

# Get the adjacency matrix of the graph
adj_matrix = get_adjacency_matrix(G)

# Print the adjacency matrix
print(adj_matrix)
