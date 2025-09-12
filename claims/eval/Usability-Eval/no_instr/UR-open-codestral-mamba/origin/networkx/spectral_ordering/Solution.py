import networkx as nx
import numpy as np
from scipy.sparse.linalg import eigsh

def compute_spectral_ordering(G):
    """
    Computes the spectral ordering of the given graph
    """
    # Convert the graph to its adjacency matrix
    adjacency_matrix = nx.to_numpy_array(G)

    # Compute the Fiedler vector
    fiedler_vector = compute_fiedler_vector(adjacency_matrix)

    # Compute the weakly connected components of the graph
    weakly_connected_components = list(nx.weakly_connected_components(G))

    # Create an empty list to store the spectral ordering
    spectral_ordering = []

    # Loop through each weakly connected component
    for component in weakly_connected_components:
        # Get the indices of the nodes in the current weakly connected component
        node_indices = [list(G.nodes()).index(node) for node in component]

        # Sort the node indices by their corresponding elements in the Fiedler vector
        sorted_indices = sorted(node_indices, key=lambda i: fiedler_vector[i])

        # Append the sorted node indices to the spectral ordering
        spectral_ordering.append(sorted_indices)

    return spectral_ordering

def compute_fiedler_vector(adjacency_matrix):
    """
    Computes the Fiedler vector of the given adjacency matrix
    """
    # Compute the eigenvalues and eigenvectors of the adjacency matrix
    eigenvalues, eigenvectors = eigsh(adjacency_matrix, k=2, which='SM')

    # Return the second eigenvector as the Fiedler vector
    return eigenvectors[:, 1]

# Create a sample graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 5)])

# Compute the spectral ordering of the graph
spectral_ordering = compute_spectral_ordering(G)
print("Spectral ordering:", spectral_ordering)
