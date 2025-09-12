
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Adding nodes to the graph G
G.add_nodes_from([1, 2, 3, 4, 5])

# Drawing the nodes of the graph G
pos = nx.spring_layout(G)  # Position of nodes
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12)
plt.show()
