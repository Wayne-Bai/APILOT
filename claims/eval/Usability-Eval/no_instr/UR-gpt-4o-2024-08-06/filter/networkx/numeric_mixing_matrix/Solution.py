import networkx as nx

def numeric_mixing_matrix(G, attribute, normalized=False):
    """
    Return the numeric mixing matrix for a given node attribute in a graph.

    Parameters:
    G : NetworkX graph
        The graph on which to compute the mixing matrix.
    attribute : str
        The node attribute key for which to compute the mixing matrix.
    normalized : bool, optional (default=False)
        If True, normalize the matrix.

    Returns:
    numpy.ndarray
        The numeric mixing matrix.
    """
    import numpy as np

    attr_dict = nx.get_node_attributes(G, attribute)
    values = list(attr_dict.values())
    unique_values = set(values)

    mapping = {val: i for i, val in enumerate(unique_values)}
    matrix_size = len(unique_values)
    mixing_matrix = np.zeros((matrix_size, matrix_size), dtype=float)

    for u, v in G.edges():
        if u in attr_dict and v in attr_dict:
            i = mapping[attr_dict[u]]
            j = mapping[attr_dict[v]]
            mixing_matrix[i, j] += 1

    if normalized:
        mixing_matrix /= mixing_matrix.sum()

    return mixing_matrix

# Example usage
if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from([(1, {'attr': 1}), (2, {'attr': 2}), (3, {'attr': 1}), (4, {'attr': 3})])
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])
    
    mmatrix = numeric_mixing_matrix(G, 'attr', normalized=True)
    print(mmatrix)
