import networkx as nx

def scaled_positions(G, scale=1.0):
    # Generate positions with a spring layout
    pos = nx.spring_layout(G)
    # Scale positions
    pos_scaled = {node: (x * scale, y * scale) for node, (x, y) in pos.items()}
    return pos_scaled

# Example usage:
# Create a sample graph
G = nx.karate_club_graph()
# Get scaled positions
positions = scaled_positions(G, scale=2.0)
print(positions)
