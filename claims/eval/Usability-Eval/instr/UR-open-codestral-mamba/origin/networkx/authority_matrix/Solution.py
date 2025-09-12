import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph - replace 'edges' with your list of edges
G.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (4, 3)])

# Calculate the authority and hub scores
authority_scores, hub_scores = nx.hits(G)

# Print the results
print("Authority Scores:", authority_scores)
print("Hub Scores:", hub_scores)
