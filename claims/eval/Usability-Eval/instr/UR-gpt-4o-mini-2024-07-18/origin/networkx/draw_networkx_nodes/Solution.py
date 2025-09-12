import networkx as nx
import matplotlib.pyplot as plt

# Create a graph G
G = nx.Graph()

# Add nodes and edges (example)
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
