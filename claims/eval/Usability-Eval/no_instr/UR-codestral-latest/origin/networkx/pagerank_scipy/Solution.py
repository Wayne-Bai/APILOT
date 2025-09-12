import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print PageRank
print("PageRank of the nodes:")
for node, rank in pagerank.items():
    print(f'Node: {node}, PageRank: {rank}')
