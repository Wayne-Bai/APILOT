import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)

# Draw the nodes of the graph
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)

plt.show()
