import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
edges = [
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 1),
    (4, 5, 1),
    (5, 1, 1),
    (2, 5, 3),
    (3, 1, 4)
]
G.add_weighted_edges_from(edges)

# Define the target node
target = 5

# Compute shortest path lengths to the target from all reachable nodes
shortest_path_lengths = {}
for node in G.nodes:
    try:
        length = nx.shortest_path_length(G, node, target, weight='weight')
        shortest_path_lengths[node] = length
    except nx.NetworkXNoPath:
        continue

print("Shortest path lengths to the target node from all reachable nodes:")
print(shortest_path_lengths)
