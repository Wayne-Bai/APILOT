import networkx as nx

# Example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4)])

# Compute shortest paths
shortest_paths = dict(nx.shortest_path_length(G))

# Print shortest paths
for node, paths in shortest_paths.items():
    print(f"Shortest paths from node {node}: {paths}")
