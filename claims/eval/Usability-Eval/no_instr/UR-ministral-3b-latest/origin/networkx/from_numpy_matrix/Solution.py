import numpy as np
import networkx as nx

# Create a numpy adjacency matrix
adj_matrix = np.array([[0, 1, 0, 0],
                       [1, 0, 1, 0],
                       [0, 1, 0, 1],
                       [0, 0, 1, 0]])

# Convert the numpy matrix to a networkx graph
G = nx.from_numpy_matrix(adj_matrix)

# Display the graph
print(nx.info(G))
