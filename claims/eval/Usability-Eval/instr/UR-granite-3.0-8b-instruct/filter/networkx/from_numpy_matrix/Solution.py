import numpy as np
import networkx as nx

# Assuming you have a numpy matrix
matrix = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]])

# Create a graph from the numpy matrix
G = nx.from_numpy_array(matrix)

# Print the graph
print(G.nodes())
print(G.edges())
