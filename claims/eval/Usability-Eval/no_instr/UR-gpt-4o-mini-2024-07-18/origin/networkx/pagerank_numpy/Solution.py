import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 2)
])

# Compute PageRank
pagerank = nx.pagerank(G)

# Print PageRank values
print(pagerank)
