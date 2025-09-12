import networkx as nx

# Graph description is represented as a list of edges
graph_description = [(1, 2), (2, 3), (3, 1), (4, 5)]

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(graph_description)

# Now G is a small undirected graph described by the graph_description
