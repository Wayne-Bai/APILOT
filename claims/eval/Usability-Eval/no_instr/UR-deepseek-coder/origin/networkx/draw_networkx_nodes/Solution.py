import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4])

# Draw the nodes of the graph
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), node_color='lightblue', node_size=500)

# Show the plot
plt.show()
