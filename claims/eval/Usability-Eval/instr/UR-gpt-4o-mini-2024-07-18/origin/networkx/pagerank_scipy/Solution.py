import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph (example)
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3), (4, 2)])

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print the PageRank of each node
print(pagerank)
