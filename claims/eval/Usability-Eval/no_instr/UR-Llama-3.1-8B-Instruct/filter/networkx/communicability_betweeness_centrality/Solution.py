import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (3, 5)]
G.add_edges_from(edges)

# Calculate communicability matrix
communicability_matrix = nx.communicability_from_path_lengths(G)

# Convert the matrix to a numpy array for easier manipulation
communicability_matrix_array = np.array(communicability_matrix)

# Print the subgraph communicability for all pairs of nodes
print(communicability_matrix_array)
