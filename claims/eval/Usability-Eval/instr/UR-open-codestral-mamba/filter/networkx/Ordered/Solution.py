import networkx as nx

# Create Ordered DiGraph
ODG = nx.OrderedDiGraph()

# Add Nodes
ODG.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Check Nodes Order
print(list(ODG.nodes()))

# Add Edges
ODG.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])

# Check Edges Order
print(list(ODG.edges()))
