
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4])

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Define the attribute for each node
node_attribute = {1: 'a', 2: 'b', 3: 'a', 4: 'c'}

# Calculate the mixing matrix for the attribute
mixing_matrix = nx.attribute_mixing_matrix(G, attribute='attribute')

# Print the mixing matrix
print(mixing_matrix)
