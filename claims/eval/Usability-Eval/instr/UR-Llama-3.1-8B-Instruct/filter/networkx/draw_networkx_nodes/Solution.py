# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1, label="Node 1", weight=3)
G.add_node(2, label="Node 2", weight=5)
G.add_node(3, label="Node 3", weight=2)
G.add_node(4, label="Node 4", weight=6)

# Add edges to the graph
G.add_edge(1, 2, weight=7)
G.add_edge(2, 3, weight=8)
G.add_edge(3, 4, weight=9)
G.add_edge(4, 1, weight=1)

# Draw the nodes of the graph G
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=5000, node_color='lightblue')

# Draw the edges of the graph G
nx.draw_networkx_edges(G, pos, width=2, edge_color='black')

# Draw the labels of the graph G
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Display the graph
plt.axis('off')
plt.show()
