import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node('Node 1')
G.add_node('Node 2')
G.add_node('Node 3')

# Add edges
G.add_edge('Node 1', 'Node 2')
G.add_edge('Node 1', 'Node 3')
G.add_edge('Node 2', 'Node 3')

# Calculate scaled positions for the nodes
scaled_pos = nx.spring_layout(G, scale=20)  # you can adjust the scale as per your requirements

# Visualize the graph
nx.draw(G, pos=scaled_pos, with_labels=True)
plt.show()
