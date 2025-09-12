
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add a node to the graph
G.add_node('A')

# Get the unique node label
unique_label = list(G.nodes)[0]

# Print the unique node label
print(unique_label)
