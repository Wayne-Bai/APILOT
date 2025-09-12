import networkx as nx

def return_scaled_positions(graph):
    """
    Return a dictionary of scaled positions keyed by node
    """
    positions = nx.spring_layout(graph)
    min_x, min_y = min(positions.values(), key=lambda x: x[0])
    max_x, max_y = max(positions.values(), key=lambda x: x[0])
    for node, pos in positions.items():
        positions[node] = (pos[0] - min_x, pos[1] - min_y)
    return positions
