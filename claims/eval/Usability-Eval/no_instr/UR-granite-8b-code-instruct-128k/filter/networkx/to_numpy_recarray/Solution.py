
import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# Get the adjacency matrix as a NumPy recarray
adj_matrix = np.recarray.fromrecords(nx.to_numpy_recarray(G), formats=[('A', 'S1'), ('B', 'S1'), ('C', 'S1'), ('D', 'S1')])

print(adj_matrix)
