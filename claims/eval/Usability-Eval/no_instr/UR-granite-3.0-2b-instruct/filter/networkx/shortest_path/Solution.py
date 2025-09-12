import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5)])

# Compute shortest paths
shortest_paths = nx.single_source_shortest_path_length(G, 1)

# Print the shortest paths
for node in G.nodes:
    print(f"Shortest path from 1 to {node}: {shortest_paths[node]}")
