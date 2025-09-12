import networkx as nx

# Create an example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Iterate over the graph vertices
for vertex in nx.iter_vertices(G):
    print(vertex)
