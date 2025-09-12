import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# Calculate the mixing matrix
M = nx.attribute_mixing_matrix(G, 'color')

# Print the mixing matrix
print(M)
