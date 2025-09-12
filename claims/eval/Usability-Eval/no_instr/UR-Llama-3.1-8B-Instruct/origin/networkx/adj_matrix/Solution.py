import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

# Create the adjacency matrix using the adjancency_matrix function from networkx
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
