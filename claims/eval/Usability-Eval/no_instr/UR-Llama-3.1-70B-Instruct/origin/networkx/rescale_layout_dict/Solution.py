import networkx as nx
import numpy as np

def scaled_positions(G, scale=1):
    """
    Return a dictionary of scaled positions keyed by node.

    Parameters
    ----------
    G : NetworkX graph
    scale : float (default=1)
        Scale factor for positions.

    Returns
    -------
    pos : dict
        A dictionary of positions keyed by node.
    """
    # Use spring layout to get the positions
    pos = nx.spring_layout(G)

    # Scale the positions
    for node in pos:
        pos[node] = np.array(pos[node]) * scale

    return pos

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

pos = scaled_positions(G, scale=100)

print(pos)
