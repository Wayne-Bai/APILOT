import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3)])

# Compute the HITS hub matrix
hits_matrix = nx.hits_centrality_matrix(G)

print(hits_matrix)
