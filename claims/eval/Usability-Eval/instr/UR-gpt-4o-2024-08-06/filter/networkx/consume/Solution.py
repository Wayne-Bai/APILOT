import networkx as nx

# Create a simple directed graph
G = nx.DiGraph()

# Add some edges
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Get an iterator over the edges of the graph
edge_iter = G.edges()

# Consume the iterator entirely
consumed_edges = list(edge_iter)

# Print the consumed edges
print(consumed_edges)
