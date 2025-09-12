import networkx as nx
import numpy as np

# create a directed graph
G = nx.DiGraph()

# add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# return adjacency matrix as a numpy matrix
adj_matrix = nx.to_numpy_matrix(G)
adj_matrix_np = np.array(adj_matrix)

print(adj_matrix_np)
