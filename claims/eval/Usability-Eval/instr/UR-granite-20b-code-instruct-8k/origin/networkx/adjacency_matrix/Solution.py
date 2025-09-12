
import networkx as nx

# Replace G with the graph object you want to get the adjacency matrix for
G = nx.Graph()

# Use the adjacency_matrix method to get the adjacency matrix of G
adj_matrix = nx.adjacency_matrix(G)

# Print the adjacency matrix
print(adj_matrix.todense())
