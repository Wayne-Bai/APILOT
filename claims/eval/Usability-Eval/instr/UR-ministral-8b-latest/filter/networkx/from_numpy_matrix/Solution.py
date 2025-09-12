import numpy as np
import networkx as nx

# Example of creating a numpy matrix
mat = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
])

# Create a graph from the numpy matrix
G = nx.from_numpy_matrix(mat)

# Visualize the graph (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
nx.draw(G)
plt.show()
