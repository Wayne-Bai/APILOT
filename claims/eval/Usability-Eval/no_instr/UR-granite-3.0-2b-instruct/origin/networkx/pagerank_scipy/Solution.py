import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add nodes and edges to your graph

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print the PageRank of each node
for node, pr in pagerank.items():
    print(f"Node {node}: {pr}")
