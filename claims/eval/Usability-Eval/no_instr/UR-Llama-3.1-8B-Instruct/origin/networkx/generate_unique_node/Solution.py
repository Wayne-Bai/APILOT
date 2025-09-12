# Importing necessary packages
import networkx as nx
import uuid

# Creating a new graph
G = nx.Graph()

# Adding a node with a unique label
node_label = str(uuid.uuid4())
G.add_node(node_label)

# Printing the unique node label
print(node_label)
