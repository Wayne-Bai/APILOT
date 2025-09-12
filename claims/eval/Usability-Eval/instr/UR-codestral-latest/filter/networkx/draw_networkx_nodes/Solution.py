# Importing the necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Creating a new graph
G = nx.Graph()

# Adding nodes to the graph
G.add_nodes_from(["Node1", "Node2", "Node3"])

# Drawing the nodes
nx.draw(G, with_labels=True)

# Displaying the graph
plt.show()
