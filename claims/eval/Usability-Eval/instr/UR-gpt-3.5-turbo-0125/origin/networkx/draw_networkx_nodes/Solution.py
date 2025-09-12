
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Adding nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Draw the nodes of the graph
pos = nx.spring_layout(G)  # Positions of the nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_color='black')
plt.show()
