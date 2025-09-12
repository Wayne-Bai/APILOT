import networkx as nx

def get_scaled_positions(graph, scale=1.0):
    # Get the positions of the nodes using a layout algorithm
    positions = nx.spring_layout(graph)

    # Scale the positions
    scaled_positions = {node: (x * scale, y * scale) for node, (x, y) in positions.items()}

    return scaled_positions

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
scaled_positions_dict = get_scaled_positions(G, scale=2.0)
print(scaled_positions_dict)
