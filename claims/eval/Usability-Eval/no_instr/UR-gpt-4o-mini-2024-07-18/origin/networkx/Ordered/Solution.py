import networkx as nx

# Create an ordered directed graph
ordered_digraph = nx.OrderedDiGraph()

# Adding nodes in a specific order
ordered_digraph.add_node(1)
ordered_digraph.add_node(2)
ordered_digraph.add_node(3)

# Adding edges; the order of edges does not have to match the order added
ordered_digraph.add_edge(1, 2)
ordered_digraph.add_edge(2, 3)
ordered_digraph.add_edge(1, 3)

# Display nodes and edges in the ordered directed graph
print("Nodes in the ordered directed graph:", ordered_digraph.nodes())
print("Edges in the ordered directed graph:", ordered_digraph.edges())
