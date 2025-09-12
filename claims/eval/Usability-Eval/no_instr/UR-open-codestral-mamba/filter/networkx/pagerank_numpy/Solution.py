import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges (nodes A, B, and C are connected to D)
G.add_edge('A', 'D')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Compute the PageRank
pagerank = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in pagerank.items():
    print(f"{node}: {rank}")
