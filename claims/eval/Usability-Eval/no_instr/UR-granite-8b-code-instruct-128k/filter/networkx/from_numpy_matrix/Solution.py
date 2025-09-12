import networkx as nx
import numpy as np
# Create a numpy matrix
A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
# Convert the numpy matrix to a graph
G = nx.from_numpy_matrix(A)
# Draw the graph
nx.draw(G, with_labels=True)
