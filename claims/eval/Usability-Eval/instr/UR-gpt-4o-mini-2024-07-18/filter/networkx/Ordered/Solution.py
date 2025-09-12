import networkx as nx

# Create an ordered directed graph
ordered_digraph = nx.OrderedDiGraph()

# Adding nodes
ordered_digraph.add_node(1)
ordered_digraph.add_node(2)
ordered_digraph.add_node(3)

# Adding edges
ordered_digraph.add_edge(1, 2)
ordered_digraph.add_edge(2, 3)
ordered_digraph.add_edge(1, 3)

# Displaying nodes in the order they were added
print("Nodes in the order added:")
print(list(ordered_digraph.nodes()))

# Displaying edges in the order they were added
print("Edges in the order added:")
print(list(ordered_digraph.edges()))
