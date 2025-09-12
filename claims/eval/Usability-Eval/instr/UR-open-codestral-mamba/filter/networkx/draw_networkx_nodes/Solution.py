import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Draw the nodes
plt.figure(figsize=(6, 4))
nx.draw_networkx(G, with_labels=True, node_color='lightblue', node_size=500)
plt.show()
