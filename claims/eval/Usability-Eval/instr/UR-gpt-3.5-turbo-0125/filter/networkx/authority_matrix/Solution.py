
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (3, 4), (4, 2)])

# Compute HITS algorithm to get hub and authority scores
hits_scores = nx.hits(G, max_iter=100)

# Extract authority scores
authority_matrix = hits_scores[1]

print("Authority matrix:")
print(authority_matrix)
