import networkx as nx
import matplotlib.pyplot as plt

# Create a simple graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)

# Draw the nodes of the graph
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), node_size=700)

# Customize and show the plot
plt.title("Nodes of Graph G")
plt.axis('off')
plt.show()
