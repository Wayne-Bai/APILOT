import networkx as nx
import numpy as np

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Convert the graph to a NumPy matrix
adj_matrix = np.array(nx.to_numpy_array(G))
