import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4])

# Draw the nodes of the graph
pos = nx.spring_layout(G)  # Positioning the nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')

# Display the graph
plt.axis('off')
plt.show()
