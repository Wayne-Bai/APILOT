import networkx as nx
import numpy as np

# Assuming G is a NetworkX graph
G = nx.Graph()

# Create nodes and edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

# Calculate adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Calculate degree vector
degree_vector = np.sum(adj_matrix, axis=0)

# Calculate SimRank matrix
sim_rank_matrix = np.zeros_like(adj_matrix)
for i in range(len(sim_rank_matrix)):
    for j in range(len(sim_rank_matrix[0])):
        if i == j:
            sim_rank_matrix[i][j] = 1
        else:
            sim_rank_matrix[i][j] = np.sum(adj_matrix[i] * adj_matrix[j]) / (np.sum(adj_matrix[i]) * np.sum(adj_matrix[j]))

# Print SimRank matrix
print(sim_rank_matrix)
