import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add some nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Draw the graph
nx.draw(G, with_labels=True)

# Show the plot
plt.show()
