import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Node 1")
G.add_node("Node 2")
G.add_node("Node 3")

# Add edges to the graph
G.add_edge("Node 1", "Node 2")
G.add_edge("Node 2", "Node 3")

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
