import networkx as nx
import numpy as np

# Assuming you have a scipy sparse matrix adjacency list
# Convert it to a list of tuples
adjacency_list = list(map(tuple, scipy_sparse_matrix.toarray().nonzero()))

# Create a graph from the adjacency list
graph = nx.from_edgelist(adjacency_list)

# If you want to create a directed graph, use the following line instead
# graph = nx.from_edgelist(adjacency_list, create_using=nx.DiGraph())
