import networkx as nx
import numpy as np

# Define an example numpy matrix as an adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 2],
    [0, 0, 1, 2, 0]
])

# Create a new empty graph
G = nx.Graph()

# Add edges from the adjacency matrix
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i, j] > 0:
            # The edge is directed if the value in matrix is not symmetric
            if i < j or adjacency_matrix[j, i]!= adjacency_matrix[i, j]:
                G.add_edge(i, j, weight=adjacency_matrix[i, j])
            # The edge is undirected if the value in matrix is symmetric
            else:
                G.add_edge(i, j, weight=adjacency_matrix[i, j])

# Print the graph
print(nx.info(G))
