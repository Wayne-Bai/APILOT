import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Compute the spectral ordering of the graph
spectral_ordering = nx.spectral_ordering(G)

# Print the spectral ordering
print(spectral_ordering)
