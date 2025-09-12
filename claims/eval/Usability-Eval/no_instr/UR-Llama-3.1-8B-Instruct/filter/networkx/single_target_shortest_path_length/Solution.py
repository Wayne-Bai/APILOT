import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add some edges to the graph (you can replace these with your actual data)
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Set a target node
target_node = 5

# Compute the shortest path lengths to the target node from all reachable nodes
shortest_path_lengths = nx.shortest_path_length(G, target_node=target_node)

# Print the shortest path lengths
print(shortest_path_lengths)
