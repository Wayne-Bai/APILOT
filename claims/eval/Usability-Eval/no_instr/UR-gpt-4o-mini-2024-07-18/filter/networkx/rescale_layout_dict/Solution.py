import networkx as nx

def get_scaled_positions(graph, scale=1.0):
    # Get original positions using a layout
    pos = nx.spring_layout(graph)
    
    # Scale the positions
    scaled_pos = {node: (x * scale, y * scale) for node, (x, y) in pos.items()}
    
    return scaled_pos

# Example usage
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
    scaled_positions = get_scaled_positions(G, scale=2.0)
    print(scaled_positions)
