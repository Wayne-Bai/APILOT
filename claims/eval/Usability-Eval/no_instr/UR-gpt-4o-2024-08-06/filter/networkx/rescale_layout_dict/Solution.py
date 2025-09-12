import networkx as nx

def get_scaled_positions(graph, scale=1):
    # Generate positions for each node in the graph
    positions = nx.spring_layout(graph)
    
    # Scale the positions
    scaled_positions = {node: (coords[0] * scale, coords[1] * scale) for node, coords in positions.items()}
    
    return scaled_positions

# Example usage:
if __name__ == "__main__":
    # Create a simple graph
    G = nx.path_graph(4)
    
    # Get scaled positions
    scaled_positions = get_scaled_positions(G, scale=2)
    
    print(scaled_positions)
