import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Create an adjacency matrix using numpy
adj_matrix = np.zeros((len(G.nodes()), len(G.nodes())))

for edge in G.edges():
    u, v = edge
    adj_matrix[u-1, v-1] = 1
    adj_matrix[v-1, u-1] = 1

print(adj_matrix)
