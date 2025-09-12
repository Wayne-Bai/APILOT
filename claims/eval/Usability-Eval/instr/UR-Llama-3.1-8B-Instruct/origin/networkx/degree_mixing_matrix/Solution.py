import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=3)
G.add_edge('B', 'C', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'E', weight=6)

# Attribute matrix for node degrees
node_degrees = nx.degree(G)

# Create a matrix of node degrees to be used for mixing matrix calculation
degree_mat = np.zeros((G.number_of_nodes(), G.number_of_nodes()))
for i in range(G.number_of_nodes()):
    for j in range(G.number_of_nodes()):
        if i!= j:
            degree_mat[i, j] = np.exp(-((nx.degree(G, i) - nx.degree(G, j)) ** 2) / (2 * (nx.degree(G, i) ** 2)))

# Mixing matrix for attribute
mixing_mat = np.dot(node_degrees, np.transpose(degree_mat))

print("Mixing Matrix:", mixing_mat)
