import networkx as nx
import numpy as np

def mixing_matrix(G, attr):
    # Create an adjacency matrix
    A = nx.to_numpy_array(G)

    # Initialize the mixing matrix
    mix = np.zeros_like(A, dtype=float)

    # Calculate the mixing matrix
    for i in range(len(A)):
        for j in range(len(A)):
            mix[i][j] = np.sum(A[i, :] * A[:, j]) / (np.sum(A[i, :]) * np.sum(A[:, j]))

    return mix

# Create a simple graph for testing
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
nx.set_node_attributes(G, {1: 'red', 2: 'blue', 3: 'red', 4: 'blue'}, 'color')

# Get the mixing matrix for the 'color' attribute
mixing_mat = mixing_matrix(G, 'color')
print("Mixing Matrix:\n", mixing_mat)
