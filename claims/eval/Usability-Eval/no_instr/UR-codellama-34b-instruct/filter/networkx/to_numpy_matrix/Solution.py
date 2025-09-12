import numpy as np
import networkx as nx

# Create a list of edges for the graph
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]

# Create a NetworkX DiGraph from the edge list
G = nx.DiGraph(edges)

# Get the adjacency matrix of the graph as a NumPy array
adj_matrix = np.array(nx.to_numpy_matrix(G))

print(adj_matrix)
