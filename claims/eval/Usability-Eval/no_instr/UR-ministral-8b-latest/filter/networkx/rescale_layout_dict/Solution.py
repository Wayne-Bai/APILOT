import networkx as nx

def get_scaled_positions(G, width, height):
    positions = {node: (nx.get_node_attributes(G, 'pos')[node][0], nx.get_node_attributes(G, 'pos')[node][1])
                 for node in G.nodes()}

    scaled_positions = {node: ((x * width) // len(G.nodes()), (y * height) // len(G.nodes()))
                        for node, (x, y) in positions.items()}
    return scaled_positions

# Example usage:
# Define a graph with positions for nodes
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
nx.set_node_attributes(G, {1: (5, 5), 2: (10, 2), 3: (15, 5)}, 'pos')

# Define width and height for scaling
width = 20
height = 20

# Get scaled positions
scaled_positions = get_scaled_positions(G, width, height)
print(scaled_positions)
