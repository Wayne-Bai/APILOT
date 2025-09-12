
import networkx as nx

# Create a DiGraph
G = nx.DiGraph()

# Add a node with a unique label
node_label = 1
G.add_node(node_label)

# Print the created node label
print("Unique node label:", node_label)
