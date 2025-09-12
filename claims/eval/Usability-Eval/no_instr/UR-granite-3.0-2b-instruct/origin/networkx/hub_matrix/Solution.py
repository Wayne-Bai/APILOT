import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('E', 'F')
])

# Calculate HITS scores
hub_scores, authority_scores = nx.hits(G)

# Print the hub matrix
print("Hub Matrix:")
print(hub_scores)
