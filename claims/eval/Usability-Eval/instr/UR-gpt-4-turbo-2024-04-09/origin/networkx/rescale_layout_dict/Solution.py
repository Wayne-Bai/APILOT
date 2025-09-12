import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)])

# Generate positions for each node using a layout algorithm
pos = nx.spring_layout(G, seed=42)  # Using a seed for reproducibility

# Define the scale function
def scale_positions(pos, scale=100):
    # Get max coordinates
    max_x = max(pos_value[0] for pos_value in pos.values())
    max_y = max(pos_value[1] for pos_value in pos.values())
    
    # Create scaled positions
    scaled_pos = {node: (pos_value[0] / max_x * scale, pos_value[1] / max_y * scale)
                  for node, pos_value in pos.items()}
    return scaled_pos

# Scale positions
scaled_pos = scale_positions(pos)

# Print scaled positions
for node, position in scaled_pos.items():
    print(f'Node {node}: Position {position}')
