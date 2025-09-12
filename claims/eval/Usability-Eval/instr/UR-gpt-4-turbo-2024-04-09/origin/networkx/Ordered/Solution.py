import networkx as nx

# Creating an Ordered Graph
ordered_graph = nx.OrderedGraph()
ordered_graph.add_edges_from([(1, 2), (2, 3), (3, 4)])
for node in ordered_graph:
    print("Ordered Graph Node:", node)  # Nodes will appear in the order added: 1, 2, 3, 4

# Creating an Ordered DiGraph
ordered_digraph = nx.OrderedDiGraph()
ordered_digraph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
for node in ordered_digraph:
    print("Ordered DiGraph Node:", node)  # Nodes will appear in the order added: 1, 2, 3, 4

# Creating an Ordered MultiGraph
ordered_multigraph = nx.OrderedMultiGraph()
ordered_multigraph.add_edges_from([(1, 2), (2, 3), (1, 2), (2, 3)])
for node in ordered_multigraph:
    print("Ordered MultiGraph Node:", node)  # Nodes will appear in the order added: 1, 2, 3

# Creating an Ordered MultiDiGraph
ordered_multidigraph = nx.OrderedMultiDiGraph()
ordered_multidigraph.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 1)])
for node in ordered_multidigraph:
    print("Ordered MultiDiGraph Node:", node)  # Nodes will appear in the order added: 1, 2, 3
