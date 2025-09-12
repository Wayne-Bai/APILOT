import networkx as nx

def compute_scaled_positions(graph):
    """
    Compute a dictionary of scaled positions keyed by node.

    Parameters
    ----------
    graph : NetworkX graph
        The input graph.

    Returns
    -------
    dict
        A dictionary of scaled positions, where each position is a tuple of the form (x, y).
    """
    # Compute the layout using Spring Layout
    pos = nx.spring_layout(graph)

    # Scale the positions to fit within the range [0, 1]
    scaled_positions = {}
    for node in graph:
        x, y = pos[node]
        scaled_x = (x - min(pos.values(), key=lambda p: p[0])) / (max(pos.values(), key=lambda p: p[0]) - min(pos.values(), key=lambda p: p[0]))
        scaled_y = (y - min(pos.values(), key=lambda p: p[1])) / (max(pos.values(), key=lambda p: p[1]) - min(pos.values(), key=lambda p: p[1]))
        scaled_positions[node] = (scaled_x, scaled_y)

    return scaled_positions
