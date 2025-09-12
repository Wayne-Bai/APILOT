import networkx as nx
import numpy as np

# Create an undirected graph G
G = nx.erdos_renyi_graph(10, 0.5, seed=123)

# Compute betweenness centrality of the nodes
betweenness_centrality = nx.betweenness_centrality(G)

# Convert the dictionary to a list of (node, betweenness) tuples
bc_list = list(betweenness_centrality.items())

# Find the node with the highest betweenness centrality
max_bc = max(bc_list, key=lambda x: x[1])

# Print the result
print(f"The node with the highest betweenness centrality is {max_bc[0]} with value {max_bc[1]}")
