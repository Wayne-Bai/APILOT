import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5)])

# Compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

# Print harmonic centrality for each node
for node in harmonic_centrality:
    print(f"Node {node}: Harmonic Centrality = {harmonic_centrality[node]}")

# Plot the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
