Python
import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# We will create a graph with 5 nodes
G.add_nodes_from(range(1, 6))

# Add edges with their weights
edges = [(1, 2, {'weight':2}), (2, 3, {'weight':3}), (3, 4, {'weight':1}), (4, 5, {'weight':4}), (5, 1, {'weight':5})]
G.add_edges_from(edges)

# Conversion of adjacency matrix to a numpy matrix
adj_matrix = nx.adjacency_matrix(G)
adj_matrix = adj_matrix.todense()

print("Adjacency matrix as a numpy matrix: \n", adj_matrix)
