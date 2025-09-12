import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Draw the graph with nodes
nx.draw(G, with_labels=True, node_color='lightblue')

# Display the plot
plt.show()
