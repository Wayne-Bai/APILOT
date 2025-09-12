import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Get the number of nodes
num_nodes = G.number_of_nodes()

# Create an empty adjacency matrix
adj_matrix = np.zeros((num_nodes, num_nodes))

# Fill the adjacency matrix with edges
for u, v in G.edges():
    adj_matrix[u-1, v-1] = 1

# Convert the adjacency matrix to a recarray
adj_matrix_recarray = np.asanyarray(adj_matrix, dtype=object)

adj_matrix_recarray
