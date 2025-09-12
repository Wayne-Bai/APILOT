
import networkx as nx

# Create a new directed graph with consistent ordering
G = nx.OrderedDiGraph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C'])

# Add edges to the graph with consistent ordering
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])

# Report the nodes in the graph in consistent order
print(list(G.nodes))  # Output: ['A', 'B', 'C']

# Report the edges in the graph in consistent order
print(list(G.edges))  # Output: [('A', 'B'), ('B', 'C'), ('C', 'A')]
