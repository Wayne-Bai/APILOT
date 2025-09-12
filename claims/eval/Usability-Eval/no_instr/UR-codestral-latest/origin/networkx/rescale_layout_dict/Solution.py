import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = ['Node1', 'Node2', 'Node3', 'Node4']
G.add_nodes_from(nodes)

# Add edges (connections) between nodes
G.add_edge('Node1', 'Node2')
G.add_edge('Node1', 'Node3')
G.add_edge('Node2', 'Node4')
G.add_edge('Node3', 'Node4')

# Compute the node positions using spring layout
pos = nx.spring_layout(G)

# Print the scaled positions
print("Scaled positions of nodes:")
for node, coords in pos.items():
    print(f"{node}: {coords}")

# Draw the graph with node positions
nx.draw(G, pos, with_labels=True)
plt.show()
