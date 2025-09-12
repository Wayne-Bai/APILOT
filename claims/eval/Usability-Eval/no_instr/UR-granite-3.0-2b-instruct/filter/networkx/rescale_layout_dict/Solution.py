import networkx as nx

# Assuming G is your graph and pos is the initial position of nodes
# G = nx.Graph()
# pos = nx.spring_layout(G)

# Function to calculate scaled positions
def scaled_positions(pos, scale_factor=0.5):
    scaled_pos = {}
    for node, coord in pos.items():
        scaled_pos[node] = (coord[0] * scale_factor, coord[1] * scale_factor)
    return scaled_pos

# Generate scaled positions
scaled_pos = scaled_positions(pos)

# Print the scaled positions
for node, coord in scaled_pos.items():
    print(f"Node {node} has position {(coord[0], coord[1])}")
