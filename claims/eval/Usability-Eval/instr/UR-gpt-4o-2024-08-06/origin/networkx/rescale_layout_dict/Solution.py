import networkx as nx

def scale_positions(G, scale=1):
    # Use the spring layout for node positioning
    pos = nx.spring_layout(G)

    # Scale positions
    scaled_pos = {node: (scale * x, scale * y) for node, (x, y) in pos.items()}

    return scaled_pos

# Example Usage
G = nx.path_graph(5)
scaled_positions = scale_positions(G, scale=2)
print(scaled_positions)
