import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph (as an example)
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print the PageRank of the nodes
print(pagerank)
