
import networkx as nx

# Define the number of nodes and edges in the graph
num_nodes = 50
num_edges = 100

# Create a random graph with the specified number of nodes and edges
G = nx.gnp_random_graph(num_nodes, num_edges)

# Define the attributes for each node in the graph
attributes = [i % 5 for i in range(num_nodes)]

# Create a mixing matrix for the attributes
mixing_matrix = nx.attribute_mixing_matrix(G, attributes=attributes)

print(mixing_matrix)
