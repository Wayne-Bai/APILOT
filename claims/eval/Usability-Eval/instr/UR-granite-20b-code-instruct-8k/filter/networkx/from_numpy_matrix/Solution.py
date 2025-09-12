import numpy as np
import networkx as nx

# Create a NumPy matrix
matrix = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])

# Create a graph from the matrix
graph = nx.from_numpy_matrix(matrix)

# Print the graph
print(graph.edges)
