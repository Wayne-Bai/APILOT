import networkx as nx

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in pagerank.items():
    print(f"Node {node}: {rank}")
