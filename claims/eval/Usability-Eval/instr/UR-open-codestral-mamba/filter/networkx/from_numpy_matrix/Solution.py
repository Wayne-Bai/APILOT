import numpy as np
import networkx as nx

# Let's suppose we have this numpy matrix as an adjacency matrix
adjacency_matrix = np.array([[0, 1, 1],
                             [1, 0, 1],
                             [1, 1, 0]])

# Create a graph
G = nx.from_numpy_array(adjacency_matrix)

# Display the nodes and edges of the graph
print('Nodes of graph: ')
print(G.nodes())
print('Edges of graph: ')
print(G.edges())
