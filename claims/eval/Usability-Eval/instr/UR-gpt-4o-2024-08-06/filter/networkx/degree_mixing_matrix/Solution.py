import networkx as nx
import numpy as np

def attribute_mixing_matrix(G, attribute, normalized=False):
    """
    Returns the mixing matrix for the given attribute.
    
    Parameters:
    - G: NetworkX graph
    - attribute: Node attribute key to calculate the mixing matrix for
    - normalized: If True, normalize the mixing matrix such that the sum of the matrix is 1
    
    Returns:
    - matrix: A 2D numpy array representing the mixing matrix
    """
    # Get all unique attribute values
    attribute_values = set(nx.get_node_attributes(G, attribute).values())
    attribute_map = {val: idx for idx, val in enumerate(attribute_values)}
    
    # Initialize the mixing matrix
    size = len(attribute_values)
    matrix = np.zeros((size, size), dtype=float)
    
    # Fill the mixing matrix
    for u, v in G.edges():
        attr_u = G.nodes[u].get(attribute)
        attr_v = G.nodes[v].get(attribute)
        if attr_u is not None and attr_v is not None:
            idx_u = attribute_map[attr_u]
            idx_v = attribute_map[attr_v]
            matrix[idx_u][idx_v] += 1
            matrix[idx_v][idx_u] += 1  # Since it's undirected, mirror entry

    # Optionally normalize the matrix
    if normalized:
        total = matrix.sum()
        if total > 0:
            matrix /= total
    
    return matrix
