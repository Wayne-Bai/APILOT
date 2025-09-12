import networkx as nx

# Create an empty Graph object
G = nx.Graph()

# Create an empty Cartesian product as a generator of edges
edges_generator = map(lambda x, y: (x, y), G.nodes, G.nodes)

# Print the graph structure
print(G.edges)

