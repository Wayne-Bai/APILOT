import networkx as nx
import uuid

# Create a graph
G = nx.Graph()

# Function to generate a unique node label
def generate_unique_node_label():
    return str(uuid.uuid4())

# Generate a unique label
unique_label = generate_unique_node_label()

# Add a node with the unique label to the graph
G.add_node(unique_label)

# Display the nodes in the graph
print(G.nodes())
