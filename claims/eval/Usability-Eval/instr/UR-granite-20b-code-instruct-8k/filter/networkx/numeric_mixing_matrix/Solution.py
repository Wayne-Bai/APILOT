import networkx as nx

# Generate a graph object
G = nx.Graph()

# Define the nodes
G.add_node("node1", attribute1=value1, attribute2=value2)
G.add_node("node2", attribute1=value3, attribute2=value4)
# Add more nodes as needed

# Define the edges
G.add_edge("node1", "node2", weight=0.5)
# Add more edges as needed

# Calculate the numeric mixing matrix for attribute
mixing_matrix = nx.attribute_mixing_matrix(G, attribute="attribute1")

# Print the mixing matrix
print(mixing_matrix)
