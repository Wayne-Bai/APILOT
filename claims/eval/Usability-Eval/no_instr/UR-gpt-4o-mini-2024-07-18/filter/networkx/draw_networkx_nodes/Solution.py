import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=14, font_color='black')

# Show the plot
plt.show()
