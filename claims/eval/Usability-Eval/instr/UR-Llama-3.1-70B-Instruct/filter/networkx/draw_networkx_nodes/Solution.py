import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Get the positions of the nodes
pos = nx.kamada_kawai_layout(G)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', node_shape='o')

# Draw the edges
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')

# Draw the labels of the nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Show the plot
plt.axis('off')
plt.show()
