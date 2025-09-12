import networkx as nx

def scaled_positions(G, scale=1.0):
    pos = nx.spring_layout(G)  # or any other layout function
    scaled_pos = {node: (x * scale, y * scale) for node, (x, y) in pos.items()}
    return scaled_pos

# Example usage:
# G = nx.path_graph(4)
# scaled_pos = scaled_positions(G, scale=2.0)
# print(scaled_pos)
