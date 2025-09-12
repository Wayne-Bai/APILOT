
import numpy as np
import networkx as nx

# create a random directed graph
G = nx.gn_random_graph(10, 0.5)

# return the adjacency matrix as a NumPy matrix
matrix = nx.to_numpy_matrix(G)
