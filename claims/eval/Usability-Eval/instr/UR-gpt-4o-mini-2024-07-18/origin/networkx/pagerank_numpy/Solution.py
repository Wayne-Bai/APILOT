import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])

# Compute PageRank
pagerank_scores = nx.pagerank(G)

# Print PageRank scores
print(pagerank_scores)
