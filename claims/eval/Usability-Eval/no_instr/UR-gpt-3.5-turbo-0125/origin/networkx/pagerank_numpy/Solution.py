
import networkx as nx

# Create a DiGraph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Calculate PageRank
pagerank = nx.pagerank(G)

print(pagerank)
