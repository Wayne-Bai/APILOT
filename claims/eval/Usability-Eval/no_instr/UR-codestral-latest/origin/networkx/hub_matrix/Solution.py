import networkx as nx

# First, let's create a sample directed graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 1), (4, 5), (5, 4), (6, 4)])

# Now, calculate the HITS hub matrix
hits_hub, hits_authority = nx.hits(G)

# Print the HITS hub matrix
print("HITS Hub Matrix: ", hits_hub)
