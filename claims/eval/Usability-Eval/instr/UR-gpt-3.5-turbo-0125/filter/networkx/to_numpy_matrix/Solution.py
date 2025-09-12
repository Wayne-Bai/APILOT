
import numpy as np
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Get the nodes in the graph
nodes = list(G.nodes)

# Create an empty numpy matrix with zeros
adj_matrix = np.zeros((len(nodes), len(nodes)))

# Fill the adjacency matrix based on the edges
for edge in G.edges:
    row = nodes.index(edge[0])
    col = nodes.index(edge[1])
    adj_matrix[row, col] = 1
    adj_matrix[col, row] = 1

print(adj_matrix)
