import networkx as nx
import numpy as np

# Define the numpy matrix
matrix = np.array([[0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0]])

# Create a graph from the numpy matrix
graph = nx.from_numpy_matrix(matrix)

# Print the graph
print(graph.edges)
