import networkx as nx
import numpy as np

# Create a numpy matrix that represents an adjacency matrix for a graph
adj_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
])

# Create an empty graph
G = nx.Graph()

# Add edges to the graph based on the adjacency matrix
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)

# Print the created graph
print("Created Graph:")
print(G)

# Print the adjacency matrix of the created graph
print("\nAdjacency Matrix of the Created Graph:")
print(nx.to_numpy_array(G))
