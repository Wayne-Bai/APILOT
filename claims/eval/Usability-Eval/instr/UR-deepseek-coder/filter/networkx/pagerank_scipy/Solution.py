import networkx as nx

# Create a sample graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 2)])

# Compute the PageRank of the nodes in the graph
pagerank = nx.pagerank(G)

# Print the PageRank values
for node, pr in pagerank.items():
    print(f"Node {node}: PageRank = {pr}")
