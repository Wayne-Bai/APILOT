
import networkx as nx
import numpy as np

# Define the numpy matrix representing the adjacency matrix of the graph
matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Create the graph from the adjacency matrix using networkx
graph = nx.from_numpy_matrix(matrix)
