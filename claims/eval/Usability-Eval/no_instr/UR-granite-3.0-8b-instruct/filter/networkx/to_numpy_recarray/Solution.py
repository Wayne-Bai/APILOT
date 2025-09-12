import networkx as nx
import numpy as np

# Assuming G is your NetworkX graph
G = nx.Graph()
# Add nodes and edges to the graph

# Convert the graph to a NumPy recarray
adj_matrix = nx.to_numpy_recarray(G)
