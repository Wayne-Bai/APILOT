import networkx as nx

# Define the graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Define the positions of the nodes
positions = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (2, 2),
    'D': (3, 3),
    'E': (4, 4)
}

# Scale the positions
scaled_positions = {node: (x * 2, y * 2) for node, (x, y) in positions.items()}

# Print the scaled positions
print(scaled_positions)
