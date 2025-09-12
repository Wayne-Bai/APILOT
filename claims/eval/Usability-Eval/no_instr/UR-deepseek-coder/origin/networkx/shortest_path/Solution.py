import networkx as nx

# Example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)])

# Compute shortest paths from node 1 to all other nodes
shortest_paths = nx.shortest_path(G, source=1)

print("Shortest paths from node 1:", shortest_paths)
