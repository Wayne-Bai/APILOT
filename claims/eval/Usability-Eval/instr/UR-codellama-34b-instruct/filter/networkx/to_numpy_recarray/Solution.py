
import numpy as np
import networkx as nx

# Define the graph structure
graph = nx.DiGraph()
graph.add_nodes_from(['A', 'B', 'C'])
graph.add_edges_from([('A', 'B'), ('B', 'C')])

# Get the adjacency matrix as a NumPy recarray
adjacency_matrix = nx.to_numpy_rec(nx.to_numpy_matrix(graph))
print(adjacency_matrix)
