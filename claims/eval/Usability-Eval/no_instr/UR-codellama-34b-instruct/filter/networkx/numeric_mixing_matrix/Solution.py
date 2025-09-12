import networkx as nx

def get_mixing_matrix(G, attr):
    """
    Returns a numeric mixing matrix for the specified attribute.

    Parameters:
        G (networkx.Graph): The graph to compute the mixing matrix for.
        attr (str): The name of the attribute to compute the mixing matrix for.

    Returns:
        ndarray: A 2D array representing the mixing matrix.
    """
    n = len(G.nodes)
    m = len(G.edges)
    M = np.zeros((n, n))
    for i in range(m):
        u, v = G.edges[i]
        a = G.node[u][attr]
        b = G.node[v][attr]
        M[u, v] += a * b
        M[v, u] += b * a
    return M
