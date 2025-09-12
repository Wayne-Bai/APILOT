import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Returns adjacency matrix of G.
adjacency_matrix = nx.to_numpy_array(G)
adjacency_matrix
