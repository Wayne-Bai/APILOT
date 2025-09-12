import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Get an iterator of the edges
edge_iterator = iter(G.edges())

# Consume the iterator entirely
all_edges = list(edge_iterator)

# Print the consumed edges
print(all_edges)
