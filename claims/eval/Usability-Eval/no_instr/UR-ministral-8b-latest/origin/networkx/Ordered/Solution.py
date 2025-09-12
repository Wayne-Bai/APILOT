import networkx as nx

# Create an ordered graph
ordered_graph = nx.OrderedGraph()

# Add nodes to the graph
ordered_graph.add_nodes_from([1, 2, 3, 4])

# Add edges to the graph
ordered_graph.add_edges_from([(1, 2), (2, 4), (4, 3), (3, 1)])

# Print nodes and edges in order
print("Nodes: ", ordered_graph.nodes)
print("Edges: ", ordered_graph.edges)
