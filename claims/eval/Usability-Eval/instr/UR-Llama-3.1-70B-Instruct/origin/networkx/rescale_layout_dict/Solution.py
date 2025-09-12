import networkx as nx
import matplotlib.pyplot as plt

def scale_positions(graph, positions, scale=1):
    """
    Return a dictionary of scaled positions keyed by node.

    Parameters
    ----------
    graph : NetworkX graph
    positions : dictionary of node positions
    scale : float (default=1)

    Returns
    -------
    dict
        Dictionary of scaled positions keyed by node
    """
    scaled_positions = {}
    for node in graph.nodes():
        x, y = positions[node]
        scaled_positions[node] = (x * scale, y * scale)
    return scaled_positions

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Use circular layout for the graph
pos = nx.circular_layout(G)

# Scale the positions by a factor of 2
scaled_pos = scale_positions(G, pos, scale=2)

# Draw the graph with scaled positions
nx.draw_networkx(G, pos=scaled_pos, with_labels=True)
plt.show()
