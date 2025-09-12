import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges and nodes
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('C', 'D', 1),
    ('A', 'D', 4),
    ('B', 'D', 2)
]
G.add_weighted_edges_from(edges)

# Compute shortest paths from node 'A'
shortest_paths = nx.shortest_path(G, source='A', weight='weight')
shortest_path_lengths = nx.shortest_path_length(G, source='A', weight='weight')

# Display the results
print("Shortest paths from node A:")
for target, path in shortest_paths.items():
    print(f"To {target}: Path = {path}, Length = {shortest_path_lengths[target]}")
