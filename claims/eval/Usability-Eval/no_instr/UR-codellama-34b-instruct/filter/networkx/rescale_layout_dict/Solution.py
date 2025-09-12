import networkx as nx

def get_scaled_positions(G):
    # Get the nodes and their positions in the graph
    nodes = list(G.nodes)
    positions = {node: G.nodes[node]['pos'] for node in nodes}
    
    # Scale the positions to fit within a box of size (10, 10)
    max_x = max(position[0] for position in positions.values())
    min_x = min(position[0] for position in positions.values())
    max_y = max(position[1] for position in positions.values())
    min_y = min(position[1] for position in positions.values())
    
    # Get the scaling factor
    scale_x = 10 / (max_x - min_x)
    scale_y = 10 / (max_y - min_y)
    
    # Scale the positions
    for node in nodes:
        position = positions[node]
        positions[node] = [scale_x * (position[0] - min_x), scale_y * (position[1] - min_y)]
        
    return positions
