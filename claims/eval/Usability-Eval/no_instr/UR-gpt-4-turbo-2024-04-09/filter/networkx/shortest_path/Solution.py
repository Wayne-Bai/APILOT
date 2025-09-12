import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes and edges with weights
G.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1), (1, 4, 4), (2, 4, 2)])

# Compute shortest paths from every node to every other node
path_lengths = dict(nx.shortest_path_length(G, weight='weight'))

# Print the shortest path lengths
for node, paths in path_lengths.items():
    print(f'Shortest paths from node {node}:')
    for target, dist in paths.items():
        print(f'  to node {target} = {dist}')
