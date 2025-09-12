import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges (links) between nodes
# For example:
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Calculate PageRank
pagerank = nx.pagerank(G, alpha=0.85)

print(pagerank)
