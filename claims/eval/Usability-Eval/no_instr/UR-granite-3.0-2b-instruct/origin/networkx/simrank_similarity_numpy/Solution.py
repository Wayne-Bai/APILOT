import networkx as nx
import numpy as np

# Create a graph G
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Calculate the adjacency matrix of G
adj_matrix = nx.to_numpy_array(G)

# Calculate the degree matrix of G
degree_matrix = np.diag(np.sum(adj_matrix, axis=1))

# Calculate the similarity matrix
similarity_matrix = np.dot(np.dot(adj_matrix, np.linalg.inv(degree_matrix)), adj_matrix)

# Calculate the SimRank of nodes in G
sim_rank = np.linalg.eigvalsh(similarity_matrix)

print(sim_rank)
