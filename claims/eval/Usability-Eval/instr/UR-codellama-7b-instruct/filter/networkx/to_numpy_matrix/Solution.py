
import numpy as np
import networkx as nx

# Create a new empty graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (1, 3)])

# Return the graph adjacency matrix as a NumPy matrix
adjacency_matrix = np.array(nx.adjacency_matrix(G).todense())
print(adjacency_matrix)
