# importing networkx
import networkx as nx

# importing numpy
import numpy as np

# create a new graph
G=nx.Graph()

# add nodes
G.add_node(1)
for i in range(2, 10):
    G.add_node(i)

# add edges
G.add_edge(1, 2)
G.add_edge(1, 7)
for i in range(2, 7):
    G.add_edge(i, i+1)

# Get adjacency matrix
adj_matrix = nx.adjacency_matrix(G)

# convert the sparse matrix to dense matrix
adj_matrix = adj_matrix.todense()

print(adj_matrix)
