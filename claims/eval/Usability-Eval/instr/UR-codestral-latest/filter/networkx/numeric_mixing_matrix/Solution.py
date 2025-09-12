import networkx as nx
import numpy as np

# Create a new graph
G = nx.Graph()

# Add nodes and attributes to the graph
G.add_nodes_from([
    (1, {'attribute': 0.5}),
    (2, {'attribute': 0.7}),
    (3, {'attribute': 0.2}),
    # Add more nodes and attributes here
])

# Extract the attribute values from the graph and return the numeric mixing matrix
attribute_values = [attr['attribute'] for node, attr in G.nodes(data=True)]
mixing_matrix = np.array(attribute_values)

print(mixing_matrix)
