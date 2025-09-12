import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add edges to the graph
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Compute HITS authority matrix
hits = nx.hits(G)

# Print HITS authority matrix
authority_matrix = hits[1]
print("HITS Authority Matrix:")
print(authority_matrix)
