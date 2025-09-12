import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)

# Scale positions for each node by dividing the coordinate value by the node's degree
scaled_positions = {}
for node in G.nodes():
    degree = G.degree(node)
    if degree > 0:  # Avoid division by zero
        x, y = 1, 1  # initial position for scale test
        scaled_positions[node] = (x / degree, y)

# Print the scaled positions
for node, (x, y) in scaled_positions.items():
    print(f"Node {node}: x={x}, y={y}")
