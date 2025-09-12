import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add nodes and edges to your graph

# Define a function to scale positions
def scale_positions(pos, scale_factor):
    return {node: {k: v * scale_factor for k, v in pos[node].items()} for node in pos}

# Scale positions of all nodes in the graph
scaled_pos = scale_positions(nx.get_node_attributes(G, 'pos'), 0.5)

# Print the scaled positions
for node, pos in scaled_pos.items():
    print(f"Node {node}: {pos}")
