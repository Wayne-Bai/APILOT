import networkx as nx

# Generate the graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5)])

# Calculate the HITS hub and authority scores
hits = nx.hits(G)

# Print the results
print("Hub scores:", hits[0])
print("Authority scores:", hits[1])
