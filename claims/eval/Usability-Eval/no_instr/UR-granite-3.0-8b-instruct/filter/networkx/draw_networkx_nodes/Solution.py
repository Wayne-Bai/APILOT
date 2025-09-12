import networkx as nx
import matplotlib.pyplot as plt

# Assuming G is your graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Draw the nodes of the graph
nx.draw(G, with_labels=True)
plt.show()
