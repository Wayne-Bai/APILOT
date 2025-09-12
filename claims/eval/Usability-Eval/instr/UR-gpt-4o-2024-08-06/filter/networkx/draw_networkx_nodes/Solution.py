import networkx as nx
import matplotlib.pyplot as plt

# Create a simple Graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph to connect nodes
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

# Create a layout for the nodes
pos = nx.kamada_kawai_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold', font_size=10)

# Show the plot
plt.show()
