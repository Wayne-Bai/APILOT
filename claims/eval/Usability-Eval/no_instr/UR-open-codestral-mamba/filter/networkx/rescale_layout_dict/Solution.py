import networkx as nx
import matplotlib.pyplot as plt

# Creating a networkx graph
G = nx.Graph()

# Adding nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Calculating scaled positions
pos = nx.spring_layout(G)

# Display the graph
nx.draw(G, pos, with_labels = True)
plt.show()

# The 'pos' dictionary holds the positions of the nodes as tuples, keyed by node.
