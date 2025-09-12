
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from([1, 2, 3])

# Add edges
G.add_edges_from([(1, 2), (2, 1), (2, 3), (3, 2)])

# Calculate PageRank
pagerank = nx.pagerank(G)

print("PageRank:", pagerank)
