import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges (example edges)
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('A', 'D')
G.add_edge('D', 'A')

# Compute the PageRank of each node
pagerank = nx.pagerank(G)

# Output the PageRank scores
print(pagerank)
