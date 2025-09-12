import networkx as nx
import matplotlib.pyplot as plt

# Create an empty Graph
G = nx.Graph()

# Add nodes
G.add_node("Node 1")
G.add_node("Node 2")
G.add_node("Node 3")

# Add edges
G.add_edge("Node 1", "Node 2")
G.add_edge("Node 2", "Node 3")
G.add_edge("Node 3", "Node 1")

# Draw the nodes
nx.draw_networkx(G, with_labels=True)
plt.show()
