import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (2, 4)])

# Compute PageRank
pagerank = nx.pagerank(G)

# Print PageRank values
for node, rank in pagerank.items():
    print(f"Node {node}: Rank {rank}")
