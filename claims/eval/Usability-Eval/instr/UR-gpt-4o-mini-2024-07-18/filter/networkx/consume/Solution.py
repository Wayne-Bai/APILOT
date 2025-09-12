import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Use an iterator to traverse through the graph edges
iterator = iter(G.edges())

# Consume the iterator entirely
edges = list(iterator)

# Output the consumed edges
print(edges)
