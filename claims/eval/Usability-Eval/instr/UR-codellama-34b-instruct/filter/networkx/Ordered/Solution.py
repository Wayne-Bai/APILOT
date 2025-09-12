import networkx as nx

# Create a directed graph with consistent node and edge ordering
G = nx.OrderedDiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])

# Print the node ordering
print(G.node_order)  # ['A', 'B', 'C']

# Print the edge ordering
print(G.edge_order)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
