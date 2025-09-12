import networkx as nx
import numpy as np
# Create a NumPy matrix representing an adjacency matrix
matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
# Create a graph from the NumPy matrix
graph = nx.from_numpy_matrix(matrix)
# Visualize the graph using NetworkX
nx.draw(graph, with_labels=True)
