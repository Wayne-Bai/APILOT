import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to generate a unique node label
def generate_node_label(node_id):
    return f"Node {str(node_id).zfill(5)}"

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
num_nodes = 10
node_ids = range(num_nodes)
G.add_nodes_from(node_ids)

# Generate unique node labels
labels = {node: generate_node_label(node) for node in G.nodes()}
print("Node Labels:")
print(labels)

# Add edges to the graph (simple example: connect each node to every other node)
G.add_edges_from([(i, j) for i in G.nodes for j in G.nodes if i!= j])

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, labels=labels)
plt.show()
