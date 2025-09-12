import networkx as nx

# Creating a sample undirected graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4), (2, 5)])

# Calculate the diameter of the graph
diameter = nx.diameter(G)
print("Diameter of the graph:", diameter)
