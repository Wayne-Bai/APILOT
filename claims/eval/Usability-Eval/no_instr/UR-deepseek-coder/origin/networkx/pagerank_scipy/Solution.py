import networkx as nx

# Example graph creation
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Compute PageRank
pagerank = nx.pagerank(G)

# Print PageRank values
for node, rank in pagerank.items():
    print(f"Node {node}: PageRank = {rank}")
