import networkx as nx

# Create a graph
G = nx.Graph()

# Add some nodes
G.add_node(1)
G.add_nodes_from([2, 3])

# Add some edges
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])

# Print the number of nodes
print(G.number_of_nodes())
