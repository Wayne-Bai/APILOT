import networkx as nx
import numpy as np

# Create a numpy matrix (adjacency matrix)
adj_matrix = np.array([[0, 1, 0, 1],
                        [1, 0, 1, 0],
                        [0, 1, 0, 1],
                        [1, 0, 1, 0]])

# Create a graph using the numpy matrix
G = nx.from_numpy_array(adj_matrix)

# Print the graph
print(G.edges())
